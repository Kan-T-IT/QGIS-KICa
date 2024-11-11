"""Helper functions module."""

import webbrowser
from typing import Optional
from urllib import parse

from PyQt5.QtCore import QCoreApplication


def open_url(url: str, params: Optional[dict] = None) -> bool:
    """Open a URL in the browser."""

    url = url if not params else f'{url}?{parse.urlencode(params, doseq=False)}'
    return webbrowser.open(url=url, new=0, autoraise=True)


def tr(message):
    """Get the translation for a string using Qt translation API."""

    return QCoreApplication.translate('@default', message)


def normalize_text(text):
    """Remove accents from text."""

    accents_map = {
        'á': 'a',
        'é': 'e',
        'í': 'i',
        'ó': 'o',
        'ú': 'u',
        'à': 'a',
        'è': 'e',
        'ì': 'i',
        'ò': 'o',
        'ù': 'u',
        'â': 'a',
        'ê': 'e',
        'î': 'i',
        'ô': 'o',
        'û': 'u',
        'ä': 'a',
        'ë': 'e',
        'ï': 'i',
        'ö': 'o',
        'ü': 'u',
        'ã': 'a',
        'ñ': 'n',
        'õ': 'o',
        'ç': 'c',
        'å': 'a',
        'æ': 'ae',
        'ø': 'o',
        'ß': 'ss',
    }

    outputString = ''
    for char in text:
        if char in accents_map:
            outputString += accents_map[char]
        else:
            outputString += char

    return outputString
