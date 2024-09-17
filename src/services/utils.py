"""Module for API auxiliary functions"""

import base64
import requests

from utils.exceptions import AuthorizationError, HostError
from utils.helpers import tr

REQUEST_TIMEOUT = 120


def encode_base64(text_to_encode: str) -> str:
    """Encode a string to Base64"""

    text_to_encode_bytes = text_to_encode.encode('utf-8')
    base64_bytes = base64.b64encode(text_to_encode_bytes)
    result = base64_bytes.decode('utf-8')

    return result


def http_get(url, host_name='', headers={}, result_type='json'):
    response = requests.request('GET', url, timeout=REQUEST_TIMEOUT)

    if host_name:
        host_name = f': {host_name}'
    if response.status_code == 200:
        if result_type == 'content':
            return response.content
        elif result_type == 'text':
            return response.text
        else:
            return response.json()

    elif response.status_code == 403:
        message = tr('Check the credentials you are using for the provider')
        raise AuthorizationError(f'{message}{host_name}')
    elif response.status_code == 542:
        message = tr('The resource you are trying to get is private')
        raise AuthorizationError(f'{message}{host_name}.')
    elif response.status_code == 404:
        message = tr('It was not possible to get the requested resource')
        raise HostError(f'{message}{host_name}.')
    else:
        message = tr('Error getting results from host')
        raise HostError(f'{message}.\n {response.text}')


def http_post(url, host_name='', headers={}, payload={}, result_type='json', raise_for_status=False):
    response = requests.request('POST', url, headers=headers, data=payload, timeout=REQUEST_TIMEOUT)
    if raise_for_status:
        response.raise_for_status()

    if host_name:
        host_name = f': {host_name}'
    if response.status_code == 200:
        if result_type == 'content':
            return response.content
        elif result_type == 'text':
            return response.text
        else:
            return response.json()
    elif response.status_code == 403:
        message = tr('Check the credentials you are using for the provider')
        raise AuthorizationError(f'{message}{host_name}.')
    elif response.status_code == 542:
        message = tr('The resource you are trying to get is private')
        raise AuthorizationError(f'{message}{host_name}.')
    elif response.status_code == 404:
        message = tr('It was not possible to get the requested resource')
        raise HostError(f'{message}{host_name}.')
    else:
        message = tr('Error getting results from host')
        raise HostError(f'{message}{host_name}.\n {response.text}')
