""" Module for Up42 API calls """


import json
import requests
from functools import lru_cache

from utils.exceptions import AuthorizationError, HostError

REQUEST_TIMEOUT = 120
DOWNLOAD_URL = 'https://planetarycomputer.microsoft.com/'


@lru_cache(maxsize=None)
def get_collections():
    """Get collections from MicrosoftPlanetary API"""
    url = 'https://planetarycomputer.microsoft.com/api/stac/v1/collections'

    response = requests.request('GET', url, timeout=REQUEST_TIMEOUT)
    response.raise_for_status()

    if response.status_code == 200:
        return response.json().get('collections')


def get_catalog(search_params: dict) -> dict:
    """Get catalog data from MicrosoftPlanetary API"""

    url = 'https://planetarycomputer.microsoft.com/api/stac/v1/search'
    headers = {}
    payload = json.dumps(search_params)

    response = requests.request('POST', url, headers=headers, data=payload, timeout=REQUEST_TIMEOUT)
    response.raise_for_status()

    if response.status_code == 200:
        return response.json()
    elif response.status_code == 542:
        raise AuthorizationError('The catalog you are trying to get is private.')
    elif response.status_code == 404:
        raise HostError('It was not possible to get the requested catalog.')
    else:
        raise HostError(f'Error getting catalogs from MicrosoftPlanetary API.\n {response.text}')


def get_thumbnail(collection_name: str, feature_data: dict):
    """Get catalog thumbnail from MicrosoftPlanetary API"""

    image_url = None
    preview_data = feature_data['assets'].get('rendered_preview')
    if preview_data:
        image_url = preview_data['href']

    results = []
    if image_url:
        response = requests.request('GET', image_url, headers={}, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        if response.status_code == 200:
            results = response.content

    return results


def get_quicklook(host_name: str, image_id: str, feature_data: dict):
    """Get catalog quicklook from MicrosoftPlanetary API"""

    image_url = None
    preview_data = feature_data['assets'].get('rendered_preview')
    if preview_data:
        image_url = preview_data['href']

    results = []
    if image_url:
        response = requests.request('GET', image_url, headers={}, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        if response.status_code == 200:
            results = response.content

    return results
