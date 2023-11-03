"""This module contains the functions to create the results layers."""

import os
from time import sleep

from core import catalogs
from core.settings import PluginSettings
from utils import qgis_helper
from utils.constants import RESULTS_GROUP_NAME, RESULTS_LAYER_NAME
from utils.general import get_plugin_dir


def create_quicklook(provider_name, host, image_id, layer_name, feature_data):
    """Create results layers."""
    footprints_layer = qgis_helper.get_or_create_footprints_layer(RESULTS_LAYER_NAME, RESULTS_GROUP_NAME)

    feature_for_quicklook = None
    for _feature in footprints_layer.getFeatures():
        if len(_feature.attributes()) > 0 and _feature.attributes()[0] == image_id:
            feature_for_quicklook = _feature
            break

    if not feature_for_quicklook:
        return False

    image_id = feature_for_quicklook.attributes()[0]
    image_response = catalogs.get_quicklook(provider_name, host, image_id, feature_data)


    temp_directory = f'{get_plugin_dir()}/temp'
    if not os.path.isdir(temp_directory):
        os.makedirs(temp_directory)

    image_path = f'{temp_directory}/{image_id}.jpg'
    file = open(image_path, 'wb')
    file.write(image_response)
    file.close()
    sleep(0.2)

    qgis_helper.create_quicklook_layer(
        layer_name=layer_name,
        group_name=RESULTS_GROUP_NAME,
        feature=feature_for_quicklook,
        image_path=image_path,
    )

    return layer_name
