"""Module for Up42 API calls"""

import json
import requests
from urllib.parse import urlencode

from services.utils import http_get, http_post
from utils.exceptions import AuthorizationError
from utils.helpers import tr

DOWNLOAD_URL = 'https://console.up42.com/catalog/new-order'


def get_token(username: str, password: str) -> str:
    """Get token from UP42 API"""

    url = 'https://auth.up42.com/realms/public/protocol/openid-connect/token'

    if not username or not password:
        raise AuthorizationError(tr('UP42 credentials have not been configured.'))

    headers = {
        'Accept': '*/*',
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    data = {
        'grant_type': 'password',
        'client_id': 'up42-api',
        'username': username,
        'password': password,
    }

    payload = urlencode(data)

    # Codifica correctamente el payload
    data = {
        'grant_type': 'password',
        'client_id': 'up42-api',
        'username': username,
        'password': password,
    }

    payload = urlencode(data)

    try:
        json_response = http_post(url, host_name='UP42', headers=headers, payload=payload, raise_for_status=True)
        token = json_response.get('access_token')
        if not token:
            raise AuthorizationError(tr('There was an error getting the token.'))

        return token

    except requests.exceptions.HTTPError as ex:
        raise AuthorizationError(f'{tr("There was an error getting the token.")}\n{ex}') from ex


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


def get_thumbnail(token: str, host_name: str, image_id: str):
    """Get catalog thumbnail from UP42 API"""

    url = f'https://api.up42.com/catalog/{host_name}/image/{image_id}/thumbnail'
    headers = {
        'accept': '*/*',
        'authorization': f'Bearer {token}',
    }

    return http_get(url, headers=headers, host_name=f'UP42: {host_name}', result_type='content')


def get_quicklook(token: str, host_name: str, image_id: str):
    """Get catalog quicklook from UP42 API"""

    url = f'https://api.up42.com/catalog/{host_name}/image/{image_id}/quicklook'
    headers = {
        'accept': '*/*',
        'authorization': f'Bearer {token}',
    }

    return http_get(url, headers=headers, host_name=f'UP42: {host_name}', result_type='content')
