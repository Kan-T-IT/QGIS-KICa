"""Module for MicrosoftPlanetary API calls"""

import json

from services.utils import http_get, http_post

DOWNLOAD_URL = 'https://planetarycomputer.microsoft.com/'


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
