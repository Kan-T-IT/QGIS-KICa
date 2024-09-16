"""Module for MicrosoftPlanetary API calls"""

import json
from functools import lru_cache

from services.utils import http_get, http_post

DOWNLOAD_URL = 'https://planetarycomputer.microsoft.com/'


@lru_cache(maxsize=None)
def get_collections():
    """Get collections from MicrosoftPlanetary API"""
    url = 'https://planetarycomputer.microsoft.com/api/stac/v1/collections'

    json_response = http_get(url, host_name='MicrosoftPlanetary')
    return json_response.get('collections')


def get_catalog(search_params: dict) -> dict:
    """Get catalog data from MicrosoftPlanetary API"""

    url = 'https://planetarycomputer.microsoft.com/api/stac/v1/search'
    headers = {}
    payload = json.dumps(search_params)
    return http_post(url, host_name='MicrosoftPlanetary', headers=headers, payload=payload)


def get_thumbnail(collection_name: str, feature_data: dict):
    """Get catalog thumbnail from MicrosoftPlanetary API"""

    image_url = None
    preview_data = feature_data['assets'].get('rendered_preview')
    if preview_data:
        image_url = preview_data['href']

    results = None
    if image_url:
        results = http_get(image_url, host_name='MicrosoftPlanetary', result_type='content')

    return results


def get_quicklook(host_name: str, image_id: str, feature_data: dict):
    """Get catalog quicklook from MicrosoftPlanetary API"""

    image_url = None
    preview_data = feature_data['assets'].get('rendered_preview')
    if preview_data:
        image_url = preview_data['href']

    results = None
    if image_url:
        results = http_get(image_url, host_name='MicrosoftPlanetary', result_type='content')

    return results


# ------------ OLD ------------
#
# @lru_cache(maxsize=None)
# def get_collections():
#     """Get collections from MicrosoftPlanetary API"""
#     url = 'https://planetarycomputer.microsoft.com/api/stac/v1/collections'

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
#     """Get catalog data from MicrosoftPlanetary API"""

#     url = 'https://planetarycomputer.microsoft.com/api/stac/v1/search'
#     headers = {}
#     payload = json.dumps(search_params)

#     response = requests.request('POST', url, headers=headers, data=payload, timeout=REQUEST_TIMEOUT)
#     response.raise_for_status()

#     if response.status_code == 200:
#         return response.json()
#     elif response.status_code == 403:
#         raise AuthorizationError(f'{tr("Check the credentials you are using for the provider")}.')
#     elif response.status_code == 542:
#         raise AuthorizationError(tr('The catalog you are trying to get is private.'))
#     elif response.status_code == 404:
#         raise HostError(tr('It was not possible to get the requested catalog.'))
#     else:
#         raise HostError(f'{tr("Error getting catalogs from MicrosoftPlanetary API.")}\n{response.text}')


# def get_thumbnail(collection_name: str, feature_data: dict):
#     """Get catalog thumbnail from MicrosoftPlanetary API"""

#     image_url = None
#     preview_data = feature_data['assets'].get('rendered_preview')
#     if preview_data:
#         image_url = preview_data['href']

#     results = None
#     if image_url:
#         response = requests.request('GET', image_url, headers={}, timeout=REQUEST_TIMEOUT)
#         response.raise_for_status()
#         if response.status_code == 200:
#             results = response.content

#     return results


# def get_quicklook(host_name: str, image_id: str, feature_data: dict):
#     """Get catalog quicklook from MicrosoftPlanetary API"""

#     image_url = None
#     preview_data = feature_data['assets'].get('rendered_preview')
#     if preview_data:
#         image_url = preview_data['href']

#     results = None
#     if image_url:
#         response = requests.request('GET', image_url, headers={}, timeout=REQUEST_TIMEOUT)
#         response.raise_for_status()
#         if response.status_code == 200:
#             results = response.content

#     return results
