""" Providers module. """

from services import up42
from utils.exceptions import AuthorizationError


def check_credentials(provider: str, credentials: dict) -> bool:
    """Check credentials from a specific provider."""

    try:
        if provider == 'up42':
            token = up42.get_token(project_id=credentials['project_id'], api_key=credentials['api_key'])
            return token is not None

        # elif provider == "sentinel":
        #     return self._provider_settings.get("sentinel", {}).get("valid", False)
        # elif provider == "planet":
        #     return self._provider_settings.get("planet", {}).get("valid", False)
    except AuthorizationError:
        return False
