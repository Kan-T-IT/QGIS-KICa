"""Module for Element84 API calls"""

import json

from services.utils import http_get, http_post

DOWNLOAD_URL = 'https://element84.com/'


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
