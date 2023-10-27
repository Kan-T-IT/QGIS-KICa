"""General utilities for the KAN Imagery Catalog plugin."""

import os
from configparser import ConfigParser


def _get_plugin_name(missing='KAN Imagery Catalog'):
    """Get plugin name from metadata.txt file."""

    plugin_dir = get_plugin_dir()
    metadata_path = os.path.join(plugin_dir, 'metadata.txt')

    if not os.path.exists(metadata_path):
        return missing

    config = ConfigParser()
    config.read(metadata_path)
    return config['general']['name']


def get_plugin_dir():
    """Get plugin directory."""

    utils_dir = os.path.dirname(__file__)
    return os.path.abspath(os.path.join(utils_dir, '..')).replace('\\', '/')


PLUGIN_NAME = _get_plugin_name()


def clean_temporary_files():
    temp_dir = os.path.join(get_plugin_dir(), 'temp')

    if os.path.exists(temp_dir):
        for file in os.listdir(temp_dir):
            os.remove(f'{temp_dir}/{file}')
    else:
        os.mkdir(temp_dir)
