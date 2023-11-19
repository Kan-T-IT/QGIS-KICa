import webbrowser
from typing import Optional
from urllib import parse

from PyQt5.QtCore import QCoreApplication


def open_url(url: str, params: Optional[dict] = None) -> bool:
    url = url if not params else f'{url}?{parse.urlencode(params, doseq=False)}'
    return webbrowser.open(url=url, new=0, autoraise=True)


def tr(message):
    return QCoreApplication.translate('@default', message)
