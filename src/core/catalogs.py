""" Catalogs module. """

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
            catalog['aux_date'] = catalog['properties']['datetime']
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


def get_download_url(provider: str):
    """Get catalog download url from a specific provider."""

    if provider == 'up42':
        return up42.DOWNLOAD_URL

    if provider == 'sentinel_hub':
        return sentinel_hub.DOWNLOAD_URL

    raise ProviderError(tr('Provider not found.'))
