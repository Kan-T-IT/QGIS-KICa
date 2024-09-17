"""Module for Up42 API calls"""

import json
import requests
from functools import lru_cache

from services.utils import http_get, http_post
from utils.exceptions import AuthorizationError
from utils.helpers import tr

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
        json_response = http_post(url, host_name='UP42', headers=headers, payload=payload, raise_for_status=True)
        data = json_response.get('data')
        if data:
            return data.get('accessToken')

    except requests.exceptions.HTTPError as ex:
        message = tr('There was an error getting the token.')
        raise AuthorizationError(f'{message}\n{ex}') from ex


@lru_cache(maxsize=None)
def get_collections():
    """Get collections from UP42 API"""
    url = 'https://api.up42.com/collections'
    json_response = http_get(url)
    return json_response.get('data')


def get_catalog(token: str, host_name: str, search_params: dict) -> dict:
    """Get catalog data from UP42 API"""

    url = f'https://api.up42.com/catalog/hosts/{host_name}/stac/search'

    headers = {
        'accept': 'application/json, text/plain, */*',
        'authorization': f'Bearer {token}',
        'content-type': 'application/json',
    }

    payload = json.dumps(search_params)
    return http_post(url, headers=headers, host_name=f'UP42: {host_name}', payload=payload)


@lru_cache(maxsize=None)
def get_thumbnail(token: str, host_name: str, image_id: str):
    """Get catalog thumbnail from UP42 API"""

    url = f' https://api.up42.com/catalog/{host_name}/image/{image_id}/thumbnail'
    headers = {
        'accept': '*/*',
        'authorization': f'Bearer {token}',
    }

    return http_get(url, headers=headers, host_name=f'UP42: {host_name}', result_type='content')


def get_quicklook(token: str, host_name: str, image_id: str):
    """Get catalog quicklook from UP42 API"""

    url = f' https://api.up42.com/catalog/{host_name}/image/{image_id}/quicklook'
    headers = {
        'accept': '*/*',
        'authorization': f'Bearer {token}',
    }

    return http_get(url, headers=headers, host_name=f'UP42: {host_name}', result_type='content')
