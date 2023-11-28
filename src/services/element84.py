""" Module for Up42 API calls """


import json
import requests
from functools import lru_cache

from utils.exceptions import AuthorizationError, HostError
from utils.helpers import tr

REQUEST_TIMEOUT = 120
DOWNLOAD_URL = 'https://element84.com/'


@lru_cache(maxsize=None)
def get_collections():
    """Get collections from Element84 API"""
    url = 'https://earth-search.aws.element84.com/v1/collections'

    response = requests.request('GET', url, timeout=REQUEST_TIMEOUT)
    response.raise_for_status()

    if response.status_code == 200:
        return response.json().get('collections')


def get_catalog(search_params: dict) -> dict:
    """Get catalog data from Element84 API"""

    url = 'https://earth-search.aws.element84.com/v1/search'

    headers = {
        'accept': 'application/json, text/plain, */*',
        'content-type': 'application/json',
    }

    payload = json.dumps(search_params)
    response = requests.request('POST', url, headers=headers, data=payload, timeout=REQUEST_TIMEOUT)

    if response.status_code == 200:
        return response.json()
    elif response.status_code == 542:
        raise AuthorizationError(tr('The catalog you are trying to get is private.'))
    elif response.status_code == 404:
        raise HostError(tr('It was not possible to get the requested catalog.'))
    else:
        raise HostError(f'{tr("Error getting catalogs from Element84 API.")}\n{response.text}')


def get_thumbnail(collection_name: str, image_id: str):
    """Get catalog thumbnail from Element84 API"""

    url = f'https://earth-search.aws.element84.com/v1/collections/{collection_name}/items/{image_id}/thumbnail'
    headers = {}

    response = requests.request('GET', url, headers=headers, timeout=REQUEST_TIMEOUT)
    response.raise_for_status()

    results = None
    if response.status_code == 200:
        results = response.content

    return results


def get_quicklook(image_id: str, feature_data: dict):
    """Get catalog quicklook from Element84 API"""

    url = (
        f'https://earth-search.aws.element84.com/v1/collections/{feature_data["collection"]}/items/{image_id}/thumbnail'
    )
    headers = {}

    response = requests.request('GET', url, headers=headers, timeout=REQUEST_TIMEOUT)
    response.raise_for_status()

    results = None
    if response.status_code == 200:
        results = response.content

    return results
