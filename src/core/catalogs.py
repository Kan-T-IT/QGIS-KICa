"""Catalogs module."""

import math
from datetime import date, datetime, timedelta
from time import sleep

from core.settings import PluginSettings
from services import element84, microsoft, sentinel_hub, up42
from utils.exceptions import ProviderError
from utils.helpers import tr


def get_custom_query(provider: str, max_cloud_coverage: int) -> dict:
    """Get custom query for a specific provider."""

    query = {}

    if provider == 'up42':
        query = {'cloudCoverage': {'LTE': max_cloud_coverage}}

    if provider == 'sentinel_hub':
        query = f'eo:cloud_cover<{max_cloud_coverage}'

    return query


def get_catalog(
    provider: str, host_name: str, search_params: dict, max_cloud_coverage: int, collection_names: list
) -> dict:
    """Get catalog data from a specific provider."""

    settings = PluginSettings()
    provider_settings = settings.provider_settings.get(provider, {'project_id': '', 'api_key': ''})
    custom_query = get_custom_query(provider=provider, max_cloud_coverage=max_cloud_coverage)
    sleep(0.3)

    if provider == 'element84':
        # if custom_query:
        #     search_params['query'] = custom_query

        catalogs = []

        catalogs_features = element84.get_catalog(search_params=search_params)
        for catalog in catalogs_features['features']:
            catalog['aux_date'] = catalog['properties']['datetime']
            catalog['aux_angle'] = None
            catalog['aux_cloud_coverage'] = None  # catalog['properties']['cloudCoverage']
            catalog['aux_collection_name'] = catalog['collection']
            catalog['aux_image_id'] = catalog['id']
            catalog['aux_coordinates'] = catalog['geometry']['coordinates'][0]

        catalogs += catalogs_features['features']

        return catalogs

    if provider == 'microsoft':
        # if custom_query:
        #     search_params['query'] = custom_query

        catalogs = []

        catalogs_features = microsoft.get_catalog(search_params=search_params)
        for catalog in catalogs_features['features']:
            catalog['aux_date'] = catalog['properties']['datetime']
            catalog['aux_angle'] = None
            catalog['aux_cloud_coverage'] = None  # catalog['properties']['cloudCoverage']
            catalog['aux_collection_name'] = catalog['collection']
            catalog['aux_image_id'] = catalog['id']
            catalog['aux_coordinates'] = catalog['geometry']['coordinates'][0]

        catalogs += catalogs_features['features']

        return catalogs

    if provider == 'up42':
        token = up42.get_token(
            username=provider_settings['username'],
            password=provider_settings['password'],
        )

        if custom_query:
            search_params['query'] = custom_query

        catalogs = up42.get_catalog(token=token, host_name=host_name, search_params=search_params)
        for catalog in catalogs['features']:
            catalog['aux_date'] = catalog['properties']['acquisitionDate']
            catalog['aux_angle'] = float(catalog['properties']['providerProperties'].get('incidenceAngle', 0))
            catalog['aux_cloud_coverage'] = catalog['properties']['cloudCoverage']
            catalog['aux_collection_name'] = collection_names.get(catalog['properties']['collection'])
            catalog['aux_image_id'] = catalog['properties']['id']
            catalog['aux_coordinates'] = catalog['geometry']['coordinates'][0]

        return catalogs['features']

    if provider == 'sentinel_hub':
        token = sentinel_hub.get_token(
            client_id=provider_settings['client_id'],
            client_secret=provider_settings['client_secret'],
        )

        if custom_query:
            search_params['filter'] = custom_query

        all_catalogs = []
        aux_collections = search_params['collections']

        # Get catalog from each collection, because the API does not allow to search in multiple collections
        for collection_name in aux_collections:
            search_params['collections'] = [collection_name]

            # TODO: get available filters by collection, cloud coverage is not available for sentinel-1-grd
            if collection_name == 'sentinel-1-grd':
                search_params.pop('filter')

        col_catalogs = sentinel_hub.get_catalog(token=token, host_name=host_name, search_params=search_params)
        for catalog in col_catalogs['features']:
            # Get date from properties
            catalog['aux_date'] = catalog['properties']['datetime']
            if not catalog['aux_date']:
                catalog['aux_date'] = catalog['properties']['start_datetime']
            if not catalog['aux_date']:
                catalog['aux_date'] = catalog['properties']['end_datetime']

            catalog['aux_angle'] = None
            catalog['aux_cloud_coverage'] = catalog['properties'].get('eo:cloud_cover')
            catalog['aux_collection_name'] = catalog['collection']
            catalog['aux_image_id'] = catalog['id']
            catalog['aux_coordinates'] = catalog['geometry']['coordinates'][0][0]

        all_catalogs += col_catalogs['features']

        return all_catalogs

    raise ProviderError(tr('Provider not found.'))


def get_catalogs_from_collection(collections: list, provider: str, search_params: dict) -> list:
    """Get catalog list from a specific provider."""

    result_features = []
    for collection in collections:
        catalog = get_catalog(
            provider=provider,
            host_name=collection['hostName'],
            search_params=search_params,
        )
        for feature in catalog['features']:
            result_features.append(feature)

    return result_features


def get_thumbnail(provider: str, collection_name: str, host_name: str, image_id: str, feature_data: dict) -> dict:
    """Get catalog thumbnail from a specific provider."""

    settings = PluginSettings()
    provider_settings = settings.provider_settings.get(provider, {'project_id': '', 'api_key': ''})

    sleep(0.3)

    thumbnail = None
    if provider == 'microsoft':
        thumbnail = microsoft.get_thumbnail(collection_name=collection_name, feature_data=feature_data)

    if provider == 'element84':
        thumbnail = element84.get_thumbnail(collection_name=collection_name, image_id=image_id)

    if provider == 'up42':
        token = up42.get_token(
            username=provider_settings['username'],
            password=provider_settings['password'],
        )

        thumbnail = up42.get_thumbnail(token=token, host_name=host_name, image_id=image_id)

    if provider == 'sentinel_hub':
        token = sentinel_hub.get_token(
            client_id=provider_settings['client_id'],
            client_secret=provider_settings['client_secret'],
        )
        thumbnail = sentinel_hub.get_thumbnail(token=token, host_name=host_name, image_id=image_id)

    return thumbnail


def get_quicklook(provider: str, host_name: str, image_id: str, feature_data: dict) -> dict:
    """Get catalog quicklook from a specific provider."""

    settings = PluginSettings()
    provider_settings = settings.provider_settings.get(provider, {'project_id': '', 'api_key': ''})

    if provider not in ['microsoft', 'up42', 'element84']:
        raise ProviderError(tr('It is not possible to obtain a preview from this provider.'))

    quicklook = None

    if provider == 'microsoft':
        quicklook = microsoft.get_quicklook(host_name=host_name, image_id=image_id, feature_data=feature_data)

    if provider == 'element84':
        quicklook = element84.get_quicklook(image_id=image_id, feature_data=feature_data)

    if provider == 'up42':
        token = up42.get_token(
            username=provider_settings['username'],
            password=provider_settings['password'],
        )

        quicklook = up42.get_quicklook(token=token, host_name=host_name, image_id=image_id)

    if not quicklook:
        raise ProviderError(tr('It is not possible to obtain a preview from this catalog.'))
    return quicklook


def get_download(provider: str, host_name: str, search_params: dict) -> dict:
    """Get catalog download from a specific provider."""

    sleep(0.3)
    settings = PluginSettings()
    provider_settings = settings.provider_settings.get(provider, {'project_id': '', 'api_key': ''})

    if provider == 'up42':
        token = up42.get_token(
            username=provider_settings['username'],
            password=provider_settings['password'],
        )

        return up42.get_catalog(token=token, host_name=host_name, search_params=search_params)

    if provider == 'planet':
        raise ProviderError(tr('This provider is not available.'))

    if provider == 'sentinel_hub':
        raise ProviderError(tr('This provider is not available.'))

    raise ProviderError(tr('Provider not found.'))


def get_download_url(**kwargs):
    """Get catalog download url from a specific provider."""

    provider = kwargs.get('provider')
    params = None
    if provider == 'up42':
        catalog_view = 'overview'
        # product_type = None
        str_bbox = None
        collection_name = None
        cloud_coverage = None
        start_date = None
        end_date = None

        feature_data = kwargs.get('feature_data')
        if feature_data:
            bbox = feature_data.get('bbox', [])  # [::-1]

            # date range
            aux_date = feature_data.get('aux_date')

            start_date = None
            end_date = None
            if aux_date:
                str_date = aux_date[:10]
                start_date = datetime.strptime(str_date, '%Y-%m-%d').date()

                # Adds one day from the start date to complete the range required by the API
                end_date = datetime.strptime(str_date, '%Y-%m-%d') + timedelta(days=1)
                end_date = end_date.date()

            # Cloud coverage
            try:
                _cloud_coverage = float(feature_data.get('aux_cloud_coverage', 0))
                if _cloud_coverage < 1:
                    _cloud_coverage = _cloud_coverage * 100

                # cloud_coverage is rounded up to the upper value.
                _cloud_coverage = math.ceil(_cloud_coverage or 0)

            except (TypeError, ValueError):
                _cloud_coverage = 0

            cloud_coverage = int(_cloud_coverage)

            if 'properties' in feature_data:
                properties = feature_data['properties']
                collection_name = properties.get('collection')
                # product_type = properties['providerProperties'].get('productType')

        x_min, ymin, xmax, ymax = map(float, bbox)
        x_center = round((x_min + xmax) / 2, 5)
        y_center = round((ymin + ymax) / 2, 5)
        center = f'{x_center},{y_center}'
        str_bbox = ','.join(map(str, bbox))

        params = {
            # 'productType': product_type,
            'catalogView': catalog_view,
            'bbox': str_bbox,
            'collections': collection_name,
            'cloudCoverage': cloud_coverage,
            'startDate': start_date,
            'center': center,
            'z': 10,
        }

        if end_date > start_date and end_date < date.today():
            params['endDate'] = end_date

        # print(f'UP42: download_url -> {up42.DOWNLOAD_URL} params: {params}')
        return up42.DOWNLOAD_URL, params

    if provider == 'sentinel_hub':
        return sentinel_hub.DOWNLOAD_URL, params

    if provider == 'microsoft':
        return microsoft.DOWNLOAD_URL, params

    if provider == 'element84':
        return element84.DOWNLOAD_URL, params

    raise ProviderError(tr('Provider not found.'))
