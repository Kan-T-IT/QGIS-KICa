""" Module for Sentinel Hub API calls """

from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session


def get_token(client_id, client_secret):
    """Get token from Sentinel Hub API"""
    client = BackendApplicationClient(client_id=client_id)
    oauth = OAuth2Session(client=client)
    token = oauth.fetch_token(
        token_url="https://services.sentinel-hub.com/oauth/token",
        client_secret=client_secret,
    )
    return token


def get_token_info(client_id):
    """Get token info from Sentinel Hub API"""
    client = BackendApplicationClient(client_id=client_id)
    oauth = OAuth2Session(client=client)
    resp = oauth.get("https://services.sentinel-hub.com/oauth/tokeninfo")
    return resp.content


# def sentinelhub_compliance_hook(response):

#     client = BackendApplicationClient(client_id=client_id)
#     oauth = OAuth2Session(client=client)
#     response.raise_for_status()
#     return response


# oauth.register_compliance_hook('access_token_response', sentinelhub_compliance_hook)

# # Your client credentials
# client_id = '<client_id>'
# client_secret = '<secret>'

# # Create a session
# client = BackendApplicationClient(client_id=client_id)
# oauth = OAuth2Session(client=client)

# # Get token for the session
# token = oauth.fetch_token(token_url='https://services.sentinel-hub.com/oauth/token', client_secret=client_secret)

# # All requests using this session will have an access token automatically added
# resp = oauth.get('https://services.sentinel-hub.com/oauth/tokeninfo')
# print(resp.content)
