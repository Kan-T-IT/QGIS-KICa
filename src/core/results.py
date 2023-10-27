"""This module contains the functions to create the results layers."""

import os
from time import sleep

from core import catalogs
from core.settings import PluginSettings
from utils import qgis_helper
from utils.constants import RESULTS_GROUP_NAME, RESULTS_LAYER_NAME
from utils.general import get_plugin_dir


def create_results_layers(provider_name, host, feature_data, layer_name, group_name, footprints_layer):
    """Create results layers."""

    crs = 'EPSG:4326'  # qgis_helper.get_current_crs()
    footprints_layer = qgis_helper.get_or_create_footprints_layer(layer_name, group_name)
    footprints_layer = qgis_helper.add_feature_to_layer(
        feature_data, feature_data['properties']['id'], footprints_layer
    )

    settings = PluginSettings()
    max_features_results = int(settings.max_features_results or 100)
    features_counter = 0
    for feature in footprints_layer.getFeatures():
        if len(feature.attributes()) == 0:
            continue

        if features_counter >= max_features_results:
            break

        image_id = feature.attributes()[0]
        quick_look_layer_name = image_id
        quick_look_layers = qgis_helper.get_layer_by_name(quick_look_layer_name)
        if quick_look_layers:
            continue

        image_response = catalogs.get_quicklook(provider_name, host, image_id)

        temp_directory = f'{get_plugin_dir()}/temp'
        if not os.path.isdir(temp_directory):
            os.makedirs(temp_directory)

        image_path = f'{temp_directory}/{image_id}.jpg'
        file = open(image_path, 'wb')
        file.write(image_response)
        file.close()
        sleep(0.2)

        qgis_helper.create_quicklook_layer(
            layer_name=quick_look_layer_name,
            group_name=group_name,
            feature=feature,
            layer_type='Polygon',
            crs=crs,
            image_path=image_path,
        )

        features_counter += 1

    return layer_name


def create_quicklook(provider_name, host, image_id, layer_name):
    """Create results layers."""

    # crs = qgis_helper.get_current_crs()
    crs = 'EPSG:4326'
    footprints_layer = qgis_helper.get_or_create_footprints_layer(RESULTS_LAYER_NAME, RESULTS_GROUP_NAME)

    feature_for_quicklook = None
    for _feature in footprints_layer.getFeatures():
        print(f'_feature: {_feature.attributes()}')
        if len(_feature.attributes()) > 0 and _feature.attributes()[0] == image_id:
            feature_for_quicklook = _feature
            break

    if not feature_for_quicklook:
        return False

    image_id = feature_for_quicklook.attributes()[0]
    image_response = catalogs.get_quicklook(provider_name, host, image_id)

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
        layer_type='Polygon',
        crs=crs,
        image_path=image_path,
    )

    return layer_name
