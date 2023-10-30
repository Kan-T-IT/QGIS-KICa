""" Module for Sentinel Hub API calls """
import requests
from functools import lru_cache

from utils.exceptions import AuthorizationError, HostError

REQUEST_TIMEOUT = 120


def get_token(client_id, client_secret):
    if not client_id or not client_secret:
        raise AuthorizationError('No se han configurado las credenciales de SentinelHub')

    url = 'https://services.sentinel-hub.com/oauth/token'

    headers = {
        'content-type': 'application/x-www-form-urlencoded',
    }

    data = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret,
    }

    try:
        response = requests.post(url, headers=headers, data=data)
        response.raise_for_status()
        if response.status_code == 200:
            data = response.json()
            if data:
                return data.get('access_token')

    except requests.exceptions.HTTPError as ex:
        raise AuthorizationError(f'Error al obtener el token.\n {ex}') from ex


@lru_cache(maxsize=None)
def get_collections(token):
    url = 'https://services.sentinel-hub.com/api/v1/catalog/1.0.0/collections'

    headers = {
        'Authorization': f'Bearer {token}',
        'Accept': 'application/json',
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    result = []
    if response.status_code == 200:
        data = response.json()
        if data:
            result = data['collections']

    return result


def get_catalog(token: str, host_name: str, search_params: dict) -> dict:
    """Get catalog data from Sentinel Hub API"""

    url = 'https://services.sentinel-hub.com/api/v1/catalog/1.0.0/search'
    headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}

    try:
        response = requests.request('POST', url, headers=headers, json=search_params, timeout=REQUEST_TIMEOUT)

        if response.status_code == 200:
            return response.json()
        if response.status_code == 542:
            raise AuthorizationError(f'El catálogo de {host_name} que intenta obtener es privado.')
        if response.status_code == 404:
            raise HostError(f'No fue posible obtener el catálogo de {host_name} solicitado.')

        response.raise_for_status()
    except requests.exceptions.HTTPError as ex:
        raise HostError(f'Error al obtener catalogos del host {host_name}.\n {ex}') from ex

    return {}


@lru_cache(maxsize=None)
def get_thumbnail(token: str, host_name: str, image_id: str):
    """Get catalog thumbnail from Sentinel Hub API"""

    return []


def get_quicklook(token: str, host_name: str, image_id: str):
    """Get catalog quicklook from Sentinel Hub API"""

    return []
