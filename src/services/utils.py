""" Module for API auxiliary functions """

import base64


def encode_base64(text_to_encode: str) -> str:
    """Encode a string to Base64"""

    text_to_encode_bytes = text_to_encode.encode("utf-8")
    base64_bytes = base64.b64encode(text_to_encode_bytes)
    result = base64_bytes.decode("utf-8")

    return result
