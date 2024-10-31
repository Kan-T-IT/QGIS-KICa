"""This module contains the functions to create the results layers."""

from utils import qgis_helper
from utils.constants import RESULTS_GROUP_NAME, RESULTS_LAYER_NAME


def create_quicklook(image_path, image_id, layer_name):
    """Create results layers."""

    footprints_layer = qgis_helper.get_or_create_footprints_layer(RESULTS_LAYER_NAME, RESULTS_GROUP_NAME)

    feature_for_quicklook = None
    for _feature in footprints_layer.getFeatures():
        if len(_feature.attributes()) > 0 and _feature.attributes()[0] == image_id:
            feature_for_quicklook = _feature
            break

    if not feature_for_quicklook:
        return False

    new_layer = qgis_helper.create_quicklook_layer(
        footprints_crs=footprints_layer.crs().authid(),
        layer_name=layer_name,
        group_name=RESULTS_GROUP_NAME,
        feature=feature_for_quicklook,
        image_path=image_path,
    )

    return new_layer
