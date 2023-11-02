""" Providers module. """

from services import sentinel_hub, up42
from utils.exceptions import AuthorizationError


def check_credentials(provider: str, credentials: dict) -> bool:
    """Check credentials from a specific provider."""

    try:
        if provider == 'up42':
            token = up42.get_token(project_id=credentials['project_id'], api_key=credentials['api_key'])
            return token is not None

        if provider == 'sentinel_hub':
            token = sentinel_hub.get_token(
                client_id=credentials['client_id'], client_secret=credentials['client_secret']
            )
            return token is not None

        # if provider == "planet":
        #     return self._provider_settings.get("planet", {}).get("valid", False)
    except AuthorizationError:
        pass

    return False
