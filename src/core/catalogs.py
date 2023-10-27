""" Catalogs module. """

from time import sleep

from core.settings import PluginSettings
from services import up42
from utils.exceptions import ProviderError


def get_catalog(provider: str, host_name: str, search_params: dict) -> dict:
    """Get catalog data from a specific provider."""

    settings = PluginSettings()
    provider_settings = settings.provider_settings.get(provider, {'project_id': '', 'api_key': ''})

    sleep(0.3)

    if provider == 'up42':
        token = up42.get_token(
            project_id=provider_settings['project_id'],
            api_key=provider_settings['api_key'],
        )
        return up42.get_catalog(token=token, host_name=host_name, search_params=search_params)

    if provider == 'planet':
        raise ProviderError('This provider is not available.')

    if provider == 'sentinel_hub':
        raise ProviderError('This provider is not available.')

    raise ProviderError('Provider not found')


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


def get_thumbnail(provider: str, host_name: str, image_id: str) -> dict:
    """Get catalog thumbnail from a specific provider."""

    settings = PluginSettings()
    provider_settings = settings.provider_settings.get(provider, {'project_id': '', 'api_key': ''})

    sleep(0.3)
    if provider == 'up42':
        token = up42.get_token(
            project_id=provider_settings['project_id'],
            api_key=provider_settings['api_key'],
        )
        return up42.get_thumbnail(token=token, host_name=host_name, image_id=image_id)

    if provider == 'planet':
        raise ProviderError('This provider is not available.')

    if provider == 'sentinel_hub':
        raise ProviderError('This provider is not available.')

    raise ProviderError('Provider not found')


def get_quicklook(provider: str, host_name: str, image_id: str) -> dict:
    """Get catalog quicklook from a specific provider."""

    settings = PluginSettings()
    provider_settings = settings.provider_settings.get(provider, {'project_id': '', 'api_key': ''})

    if provider == 'up42':
        token = up42.get_token(
            project_id=provider_settings['project_id'],
            api_key=provider_settings['api_key'],
        )
        return up42.get_quicklook(token=token, host_name=host_name, image_id=image_id)

    if provider == 'planet':
        raise ProviderError('This provider is not available.')

    if provider == 'sentinel_hub':
        raise ProviderError('This provider is not available.')

    raise ProviderError('Provider not found')


def get_download(provider: str, host_name: str, search_params: dict) -> dict:
    """Get catalog download from a specific provider."""

    sleep(0.3)
    settings = PluginSettings()
    provider_settings = settings.provider_settings.get(provider, {'project_id': '', 'api_key': ''})

    if provider == 'up42':
        token = up42.get_token(
            project_id=provider_settings['project_id'],
            api_key=provider_settings['api_key'],
        )
        return up42.get_catalog(token=token, host_name=host_name, search_params=search_params)

    if provider == 'planet':
        raise ProviderError('This provider is not available.')

    if provider == 'sentinel_hub':
        raise ProviderError('This provider is not available.')

    raise ProviderError('Provider not found')


def get_download_url(provider: str):
    """Get catalog download url from a specific provider."""

    if provider == 'up42':
        return up42.DOWNLOAD_URL

    if provider == 'planet':
        return 'https://www.planet.com/'

    if provider == 'sentinel_hub':
        return 'https://www.sentinel-hub.com/'

    raise ProviderError('Provider not found')
