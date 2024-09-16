"""Module for Sentinel Hub API calls"""

import requests
from functools import lru_cache

from services.utils import http_get, http_post
from utils.exceptions import AuthorizationError
from utils.helpers import tr

DOWNLOAD_URL = 'https://www.sentinel-hub.com/'


def get_token(client_id, client_secret):
    """Get token from Sentinel Hub API"""

    if not client_id or not client_secret:
        raise AuthorizationError(tr('SentinelHub credentials have not been configured.'))

    url = 'https://services.sentinel-hub.com/oauth/token'

    headers = {
        'content-type': 'application/x-www-form-urlencoded',
    }

    payload = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret,
    }

    try:
        headers = {}
        data = http_post(url, host_name='SentinelHub', headers=headers, payload=payload, raise_for_status=True)
        if data:
            return data.get('access_token')

    except requests.exceptions.HTTPError as ex:
        raise AuthorizationError(f'{tr("There was an error getting the token.")}\n{ex}') from ex


@lru_cache(maxsize=None)
def get_collections(token):
    """Get collections from Sentinel Hub API"""

    url = 'https://services.sentinel-hub.com/api/v1/catalog/1.0.0/collections'

    headers = {
        'Authorization': f'Bearer {token}',
        'Accept': 'application/json',
    }

    data = http_get(url, host_name='SentinelHub', headers=headers)
    result = []
    if data:
        result = data['collections']

    return result


def get_catalog(token: str, host_name: str, search_params: dict) -> dict:
    """Get catalog data from Sentinel Hub API"""

    url = 'https://services.sentinel-hub.com/api/v1/catalog/1.0.0/search'
    headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}

    return http_post(url, host_name='SentinelHub', headers=headers, payload=search_params)


def get_thumbnail(token: str, host_name: str, image_id: str):
    """Get catalog thumbnail from Sentinel Hub API"""

    return None


def get_quicklook(token: str, host_name: str, image_id: str):
    """Get catalog quicklook from Sentinel Hub API"""

    return None


# ------------ OLD ------------

# def get_token(client_id, client_secret):
#     """Get token from Sentinel Hub API"""

#     if not client_id or not client_secret:
#         raise AuthorizationError(tr('SentinelHub credentials have not been configured.'))

#     url = 'https://services.sentinel-hub.com/oauth/token'

#     headers = {
#         'content-type': 'application/x-www-form-urlencoded',
#     }

#     data = {
#         'grant_type': 'client_credentials',
#         'client_id': client_id,
#         'client_secret': client_secret,
#     }

#     try:
#         response = requests.post(url, headers=headers, data=data)
#         response.raise_for_status()
#         if response.status_code == 200:
#             data = response.json()
#             if data:
#                 return data.get('access_token')

#     except requests.exceptions.HTTPError as ex:
#         raise AuthorizationError(f'{tr("There was an error getting the token.")}\n{ex}') from ex


# @lru_cache(maxsize=None)
# def get_collections(token):
#     """Get collections from Sentinel Hub API"""

#     url = 'https://services.sentinel-hub.com/api/v1/catalog/1.0.0/collections'

#     headers = {
#         'Authorization': f'Bearer {token}',
#         'Accept': 'application/json',
#     }

#     response = requests.get(url, headers=headers)
#     response.raise_for_status()

#     result = []
#     if response.status_code == 200:
#         data = response.json()
#         if data:
#             result = data['collections']
#     elif response.status_code == 403:
#         raise AuthorizationError(tr('Check the credentials you are using for the provider'))
#     elif response.status_code == 404:
#         raise HostError(tr('It was not possible to get the requested collections'))
#     else:
#         raise HostError(f'{tr("Error getting collections from host")}.\n {response.text}')
#     return result


# def get_catalog(token: str, host_name: str, search_params: dict) -> dict:
#     """Get catalog data from Sentinel Hub API"""

#     url = 'https://services.sentinel-hub.com/api/v1/catalog/1.0.0/search'
#     headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}

#     response = requests.request('POST', url, headers=headers, json=search_params, timeout=REQUEST_TIMEOUT)

#     if response.status_code == 200:
#         return response.json()
#     elif response.status_code == 403:
#         raise AuthorizationError(f'{tr("Check the credentials you are using for the provider")}: {host_name}.')
#     elif response.status_code == 542:
#         raise AuthorizationError(f'{tr("The catalog you are trying to get is private:")} {host_name}.')
#     elif response.status_code == 404:
#         raise HostError(f'{tr("It was not possible to get the requested catalog")}: {host_name}.')
#     else:
#         raise HostError(f'{tr("Error getting catalogs from host")} {host_name}.\n {response.text}')


# @lru_cache(maxsize=None)
# def get_thumbnail(token: str, host_name: str, image_id: str):
#     """Get catalog thumbnail from Sentinel Hub API"""

#     return None


# def get_quicklook(token: str, host_name: str, image_id: str):
#     """Get catalog quicklook from Sentinel Hub API"""

#     return None
