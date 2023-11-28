""" Module for Up42 API calls """


import json
import requests
from functools import lru_cache

from utils.exceptions import AuthorizationError, DataNotFoundError, HostError
from utils.helpers import tr

REQUEST_TIMEOUT = 120
DOWNLOAD_URL = 'https://console.up42.com/catalog/new-order'


def get_token(username: str, password: str) -> str:
    """Get token from UP42 API"""
    url = 'https://api.up42.com/oauth/token'

    if not username or not password:
        raise AuthorizationError(tr('UP42 credentials have not been configured.'))

    headers = {
        'Accept': '*/*',
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    payload = f'grant_type=password&username={username}&password={password}'

    try:
        response = requests.request('POST', url, data=payload, headers=headers, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()

        if response.status_code == 200:
            data = response.json().get('data')
            if data:
                return data.get('accessToken')

    except requests.exceptions.HTTPError as ex:
        raise AuthorizationError(f"{tr('There was an error getting the token.')}\n {ex}") from ex


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
        raise AuthorizationError(f'{tr("The catalog you are trying to get is private:")} {host_name}.')
    elif response.status_code == 404:
        raise HostError(f'{tr("It was not possible to get the requested catalog")}: {host_name}.')
    else:
        raise HostError(f'{tr("Error getting catalogs from host")} {host_name}.\n {response.text}')


@lru_cache(maxsize=None)
def get_thumbnail(token: str, host_name: str, image_id: str):
    """Get catalog thumbnail from UP42 API"""

    url = f' https://api.up42.com/catalog/{host_name}/image/{image_id}/thumbnail'
    headers = {
        'accept': '*/*',
        'authorization': f'Bearer {token}',
    }

    response = requests.request('GET', url, headers=headers, timeout=REQUEST_TIMEOUT)
    results = None
    if response.status_code == 200:
        results = response.content
    elif response.status_code == 404:
        raise DataNotFoundError(f'{tr("It was not possible to get the requested thumbnail")}: {image_id}.')

    response.raise_for_status()
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
        raise HostError(f'{tr("Error getting quicklook")} {image_id}.\n {ex}') from ex
