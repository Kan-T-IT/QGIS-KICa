""" Collections module. """


from core.settings import PluginSettings
from services import element84, microsoft, sentinel_hub, up42
from utils.exceptions import ProviderError
from utils.helpers import tr


def get_collections(provider: str, search_params: dict = None) -> dict:
    """Get collections from a specific provider."""

    settings = PluginSettings()
    provider_settings = settings.provider_settings.get(provider, {'project_id': '', 'api_key': ''})

    if provider == 'microsoft':
        collections = microsoft.get_collections()

        for collection in collections:
            collection['name'] = collection['id']
            collection['hostName'] = collection['providers'][0]['name']
        #     collection['sensor_type'] = 'Optical' if collection['isOptical'] else 'Non-Optical'
        #     collection['min_resolution'] = collection['resolutionValue'].get('minimum')

        return collections

    if provider == 'element84':
        collections = element84.get_collections()

        for collection in collections:
            collection['name'] = collection['id']
            collection['hostName'] = collection['providers'][0]['name']
        #     collection['sensor_type'] = 'Optical' if collection['isOptical'] else 'Non-Optical'
        #     collection['min_resolution'] = collection['resolutionValue'].get('minimum')

        return collections

    if provider == 'up42':
        collections = up42.get_collections()

        for collection in collections:
            collection['sensor_type'] = 'Optical' if collection['isOptical'] else 'Non-Optical'
            collection['min_resolution'] = collection['resolutionValue'].get('minimum')

        return collections

    if provider == 'sentinel_hub':
        token = sentinel_hub.get_token(
            client_id=provider_settings['client_id'],
            client_secret=provider_settings['client_secret'],
        )
        collections = sentinel_hub.get_collections(token=token)

        for collection in collections:
            collection['name'] = collection['id']
            collection['hostName'] = ''

            for provider in collection['providers']:
                if 'host' in provider['roles']:
                    collection['hostName'] = provider['name']
                    break

            collection['provider'] = provider
            collection['sensor_type'] = collection['summaries'].get('instrument')
            collection['min_resolution'] = ''

        return collections

    raise ProviderError(tr('Provider not found.'))
