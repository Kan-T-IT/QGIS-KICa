""" Module for Up42 API calls """


import json
import requests
from functools import lru_cache

from services.utils import encode_base64
from utils.exceptions import AuthorizationError, HostError

REQUEST_TIMEOUT = 120
DOWNLOAD_URL = 'https://console.up42.com/catalog/new-order'


def get_token(project_id: str, api_key: str) -> str:
    """Get token from UP42 API"""
    url = 'https://api.up42.com/oauth/token'

    if not project_id or not api_key:
        raise AuthorizationError('UP42 credentials have not been configured.')

    encoded_value = encode_base64(f'{project_id}:{api_key}')
    headers = {
        'Accept': '*/*',
        'Authorization': f'Basic {encoded_value}',
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    payload = 'grant_type=client_credentials'

    try:
        response = requests.request('POST', url, data=payload, headers=headers, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()

        if response.status_code == 200:
            data = response.json().get('data')
            if data:
                return data.get('accessToken')

    except requests.exceptions.HTTPError as ex:
        raise AuthorizationError(f'There was an error getting the token.\n {ex}') from ex


@lru_cache(maxsize=None)
def get_collections():
    """Get collections from UP42 API"""
    url = 'https://api.up42.com/collections'

    response = requests.request('GET', url, timeout=REQUEST_TIMEOUT)
    response.raise_for_status()

    if response.status_code == 200:
        return response.json().get('data')


def get_catalog(token: str, host_name: str, search_params: dict) -> dict:
    """Get catalog data from UP42 API"""

    url = f'https://api.up42.com/catalog/hosts/{host_name}/stac/search'

    headers = {
        'accept': 'application/json, text/plain, */*',
        'authorization': f'Bearer {token}',
        'content-type': 'application/json',
    }

    payload = json.dumps(search_params)
    response = requests.request('POST', url, headers=headers, data=payload, timeout=REQUEST_TIMEOUT)

    if response.status_code == 200:
        return response.json()
    elif response.status_code == 542:
        raise AuthorizationError(f'The {host_name} catalog you are trying to get is private.')
    elif response.status_code == 404:
        raise HostError(f'It was not possible to get the requested {host_name} catalog.')
    else:
        raise HostError(f'Error getting catalogs from host {host_name}.\n {response.text}')



@lru_cache(maxsize=None)
def get_thumbnail(token: str, host_name: str, image_id: str):
    """Get catalog thumbnail from UP42 API"""

    url = f' https://api.up42.com/catalog/{host_name}/image/{image_id}/thumbnail'
    headers = {
        'accept': '*/*',
        'authorization': f'Bearer {token}',
    }

    response = requests.request('GET', url, headers=headers, timeout=REQUEST_TIMEOUT)
    response.raise_for_status()

    results = None
    if response.status_code == 200:
        results = response.content

    return results


def get_quicklook(token: str, host_name: str, image_id: str):
    """Get catalog quicklook from UP42 API"""
    url = f' https://api.up42.com/catalog/{host_name}/image/{image_id}/quicklook'
    headers = {
        'accept': '*/*',
        'authorization': f'Bearer {token}',
    }

    try:
        response = requests.request('GET', url, headers=headers, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()

        results = None
        if response.status_code == 200:
            results = response.content

        return results

    except requests.exceptions.HTTPError as ex:
        raise HostError(f'Error getting quicklook {image_id}.\n {ex}') from ex
