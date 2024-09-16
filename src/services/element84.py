"""Module for Element84 API calls"""

import json
from functools import lru_cache

from services.utils import http_get, http_post

DOWNLOAD_URL = 'https://element84.com/'


@lru_cache(maxsize=None)
def get_collections():
    """Get collections from Element84 API"""
    url = 'https://earth-search.aws.element84.com/v1/collections'

    json_response = http_get(url, host_name='Element84')
    return json_response.get('collections')


def get_catalog(search_params: dict) -> dict:
    """Get catalog data from Element84 API"""

    url = 'https://earth-search.aws.element84.com/v1/search'

    headers = {
        'accept': 'application/json, text/plain, */*',
        'content-type': 'application/json',
    }

    payload = json.dumps(search_params)
    return http_post(url, host_name='Element84', headers=headers, payload=payload)


def get_thumbnail(collection_name: str, image_id: str):
    """Get catalog thumbnail from Element84 API"""

    url = f'https://earth-search.aws.element84.com/v1/collections/{collection_name}/items/{image_id}/thumbnail'
    return http_get(url, host_name='Element84', result_type='content')


def get_quicklook(image_id: str, feature_data: dict):
    """Get catalog quicklook from Element84 API"""

    url = (
        f'https://earth-search.aws.element84.com/v1/collections/{feature_data["collection"]}/items/{image_id}/thumbnail'
    )
    return http_get(url, host_name='Element84', result_type='content')


# ------------ OLD ------------

# @lru_cache(maxsize=None)
# def get_collections():
#     """Get collections from Element84 API"""
#     url = 'https://earth-search.aws.element84.com/v1/collections'

#     response = requests.request('GET', url, timeout=REQUEST_TIMEOUT)
#     response.raise_for_status()

#     if response.status_code == 200:
#         return response.json().get('collections')
#     elif response.status_code == 403:
#         raise AuthorizationError(tr('Check the credentials you are using for the provider'))
#     elif response.status_code == 404:
#         raise HostError(tr('It was not possible to get the requested collections'))
#     else:
#         raise HostError(f'{tr("Error getting collections from host")}.\n {response.text}')


# def get_catalog(search_params: dict) -> dict:
#     """Get catalog data from Element84 API"""

#     url = 'https://earth-search.aws.element84.com/v1/search'

#     headers = {
#         'accept': 'application/json, text/plain, */*',
#         'content-type': 'application/json',
#     }

#     payload = json.dumps(search_params)
#     response = requests.request('POST', url, headers=headers, data=payload, timeout=REQUEST_TIMEOUT)

#     if response.status_code == 200:
#         return response.json()
#     elif response.status_code == 403:
#         raise AuthorizationError(f'{tr("Check the credentials you are using for the provider")}.')
#     elif response.status_code == 542:
#         raise AuthorizationError(tr('The catalog you are trying to get is private.'))
#     elif response.status_code == 404:
#         raise HostError(tr('It was not possible to get the requested catalog.'))
#     else:
#         raise HostError(f'{tr("Error getting catalogs from Element84 API.")}\n{response.text}')


# def get_thumbnail(collection_name: str, image_id: str):
#     """Get catalog thumbnail from Element84 API"""

#     url = f'https://earth-search.aws.element84.com/v1/collections/{collection_name}/items/{image_id}/thumbnail'
#     headers = {}

#     response = requests.request('GET', url, headers=headers, timeout=REQUEST_TIMEOUT)
#     response.raise_for_status()

#     results = None
#     if response.status_code == 200:
#         results = response.content

#     return results


# def get_quicklook(image_id: str, feature_data: dict):
#     """Get catalog quicklook from Element84 API"""

#     url = (
#         f'https://earth-search.aws.element84.com/v1/collections/{feature_data["collection"]}/items/{image_id}/thumbnail'
#     )
#     headers = {}

#     response = requests.request('GET', url, headers=headers, timeout=REQUEST_TIMEOUT)
#     response.raise_for_status()

#     results = None
#     if response.status_code == 200:
#         results = response.content

#     return results
