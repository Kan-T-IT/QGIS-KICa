""" Collections module. """

from services import up42

# from utils.exceptions import ProviderError


def get_collections(provider: str, search_params: dict = None) -> dict:
    """Get collections from a specific provider."""

    if provider == 'up42':
        return up42.get_collections()  # search_params=search_params)

    # if provider == 'planet':
    #     raise ProviderError('This provider is not available.')

    # if provider == 'sentinel_hub':
    #     raise ProviderError('This provider is not available.')

    # raise ProviderError('Provider not found')

    return []
