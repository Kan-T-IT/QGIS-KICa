"""QGIS helper functions module."""

import json
import os

from osgeo import gdal
from PyQt5.QtCore import QVariant

from utils.constants import DEFAULT_MESSAGE_DURATION, DEFAULT_TARGET_CRS
from utils.exceptions import DataNotFoundError
from utils.general import PLUGIN_NAME
from utils.helpers import tr

try:
    from qgis.core import (
        Qgis,
        QgsCoordinateReferenceSystem,
        QgsCoordinateTransform,
        QgsFeature,
        QgsField,
        QgsFields,
        QgsFillSymbol,
        QgsGeometry,
        QgsLayerTreeGroup,
        QgsMapLayer,
        QgsPointXY,
        QgsProject,
        QgsRasterLayer,
        QgsSettings,
        QgsVectorLayer,
    )
    from qgis.utils import iface
except Exception as ex:  # noqa: E722    pylint: disable=bare-except
    message = tr('QGIS libraries could not be imported.')
    print(f'{message}\n{ex}')


def get_bounding_box_transformed(bbox, source_crs, target_crs):
    """Get bounding box from canvas and transform it if necessary to the default target CRS."""

    if source_crs.authid() != target_crs.authid():
        transform = QgsCoordinateTransform(source_crs, target_crs, QgsProject.instance())
        bbox = transform.transform(bbox)
        # bottom_left = transform.transform(bbox.xMinimum(), bbox.yMinimum())
        # top_right = transform.transform(bbox.xMaximum(), bbox.yMaximum())
        # bbox = QgsRectangle(bottom_left, top_right)

    return bbox


def get_bounding_box_canvas():
    """Get bounding box from canvas."""

    bbox = iface.mapCanvas().extent()

    source_crs = iface.mapCanvas().mapSettings().destinationCrs()
    api_crs = QgsCoordinateReferenceSystem(DEFAULT_TARGET_CRS)
    bbox = get_bounding_box_transformed(bbox, source_crs, api_crs)

    x_min = bbox.xMinimum()
    y_min = bbox.yMinimum()
    x_max = bbox.xMaximum()
    y_max = bbox.yMaximum()

    return {'x_min': x_min, 'y_min': y_min, 'x_max': x_max, 'y_max': y_max}


def get_selected_feature_bounding_box(layer_id, default_first=True):
    """Get bounding box from feature. By default, the first feature in the array is used if no feature is selected."""

    layer = QgsProject.instance().mapLayer(layer_id)
    if not layer:
        raise DataNotFoundError('Error', tr('The specified layer was not found.'))

    selected_feature = next((x for x in layer.getSelectedFeatures()), None)
    if selected_feature is None and default_first:
        selected_feature = next(layer.getFeatures())

    if selected_feature:
        # select the first feature in the layer
        iface.setActiveLayer(layer)
        layer.selectByIds([selected_feature.id()])
        zoom_selected_features(layer)

        bbox = selected_feature.geometry().boundingBox()

        source_crs = layer.crs()
        api_crs = QgsCoordinateReferenceSystem(DEFAULT_TARGET_CRS)
        bbox = get_bounding_box_transformed(bbox, source_crs, api_crs)

        x_min = bbox.xMinimum()
        y_min = bbox.yMinimum()
        x_max = bbox.xMaximum()
        y_max = bbox.yMaximum()

        return {'x_min': x_min, 'y_min': y_min, 'x_max': x_max, 'y_max': y_max}

    raise DataNotFoundError(tr('There are no features selected on the specified layer.'))


def get_valid_project_layers_to_search():
    """Get vector layers names from current project excluding the ones in the results group."""

    def is_in_group(project, layer, group_name):
        """Check if layer is included in a group with the specified name."""

        layer_tree_layer = project.layerTreeRoot().findLayer(layer.id())
        parent = layer_tree_layer.parent() if layer_tree_layer else None

        while parent is not None:
            if parent.name() == group_name:
                return True
            parent = parent.parent()

        return False

    layer_list = []

    _project = QgsProject.instance()
    _excluded_group = 'kan_imagery_catalog_preview'

    all_layers = _project.mapLayers().values()

    layer_list = [
        (_layer.id(), _layer.name())
        for _layer in all_layers
        if not is_in_group(_project, _layer, _excluded_group) and _layer.type() == QgsMapLayer.VectorLayer
    ]

    return layer_list


def save_setting(setting_name, value):
    """Save setting."""

    settings = QgsSettings()
    settings.setValue(f'{PLUGIN_NAME}/{setting_name}', value)


def read_setting(setting_name, default_value=None):
    """Read setting."""

    settings = QgsSettings()
    return settings.value(f'{PLUGIN_NAME}/{setting_name}', default_value)


def save_json_setting(setting_name, value):
    """Save json setting."""

    json_setting = json.dumps(value)
    settings = QgsSettings()
    settings.setValue(f'{PLUGIN_NAME}/{setting_name}', json_setting)


def read_json_setting(setting_name, default_value=None):
    """Read json setting."""
    settings = QgsSettings()
    json_setting = settings.value(f'{PLUGIN_NAME}/{setting_name}', default_value)

    value = {}
    try:
        if json_setting is not None:
            value = json.loads(json_setting)
    except Exception:
        pass

    return value


# 0: Info
# 1: Warning
# 2: Critical
# 3: Success


def error_message(title, text):
    """Show error message."""

    iface.messageBar().pushMessage(title, text, level=Qgis.Critical)


def warning_message(title, text):
    """Show warning message."""

    iface.messageBar().pushMessage(title, text, level=Qgis.Warning, duration=DEFAULT_MESSAGE_DURATION)


def info_message(title, text):
    """Show info message."""

    iface.messageBar().pushMessage(title, text, level=Qgis.Info, duration=DEFAULT_MESSAGE_DURATION)


def success_message(title, text):
    """Show success message."""

    iface.messageBar().pushMessage(title, text, level=Qgis.Success, duration=DEFAULT_MESSAGE_DURATION)


def get_or_create_group(group_name):
    """Get or create group."""

    root = QgsProject.instance().layerTreeRoot()
    results_group = None
    for child in root.children():
        # Use of casefold is to avoid problems with special characters specially on windows
        if isinstance(child, QgsLayerTreeGroup) and child.name().casefold() == group_name.casefold():
            results_group = child
            break

    if results_group is None:
        results_group = root.insertGroup(0, group_name)

    return results_group


def get_layer_by_name(layer_name):
    """Get layer by name."""

    layers = QgsProject.instance().mapLayersByName(layer_name)
    if layers:
        return layers[0]

    return None


def get_or_create_footprints_layer(layer_name, group_name):
    """Get or create footprints layer."""

    layer_type = 'Polygon'
    layers = QgsProject.instance().mapLayersByName(layer_name)
    if layers:
        footprints_layer = layers[0]
    else:
        results_group = get_or_create_group(group_name)
        footprints_layer = QgsVectorLayer(f'{layer_type}?crs={DEFAULT_TARGET_CRS}', layer_name, 'memory')

        symbol = QgsFillSymbol.createSimple(
            {
                'color': '155,55,55,15',
                'outline_color': 'dark_gray',
                'outline_width': '0.1',
            }
        )
        footprints_layer.renderer().setSymbol(symbol)

        pr = footprints_layer.dataProvider()
        # Add layer fields
        fields = QgsFields()
        fields.append(QgsField(name='ID', type=QVariant.String))
        pr.addAttributes(fields)
        footprints_layer.updateFields()
        footprints_layer.triggerRepaint()

        QgsProject.instance().addMapLayer(footprints_layer, False)
        results_group.addLayer(footprints_layer)

    return footprints_layer


def add_feature_to_layer(coordinates, feature_id, layer):
    """Add feature to layer."""

    points = [QgsPointXY(point[0], point[1]) for point in coordinates]
    polygon = QgsGeometry.fromPolygonXY([points])

    feature = QgsFeature()
    feature.setGeometry(polygon)
    feature.setAttributes([feature_id])

    pr = layer.dataProvider()
    pr.addFeature(feature)
    return layer


def get_georeferenced_image(feature, image_path):
    """Get georeferenced image from feature and image path."""
    image_filename = os.path.basename(image_path)
    image_name = os.path.splitext(image_filename)[0]
    temp_dir = os.path.dirname(image_path)

    input_image_path = f'{temp_dir}/{image_filename}'
    output_image_path = f'{temp_dir}/georef_{image_name}.tif'

    bbox = feature.geometry().boundingBox()
    xmin = bbox.xMinimum()
    ymin = bbox.yMinimum()
    xmax = bbox.xMaximum()
    ymax = bbox.yMaximum()

    # FIX: bbox with x inverted to match the image (temporal solution)
    gdal.Translate(
        output_image_path,
        input_image_path,
        outputSRS=DEFAULT_TARGET_CRS,
        noData=0,
        outputBounds=[xmin, ymax, xmax, ymin],
    )

    return output_image_path


def create_quicklook_layer(
    footprints_crs,
    layer_name,
    group_name,
    feature,
    image_path=None,
):
    """Create a layer with a quicklook image."""

    results_group = get_or_create_group(group_name)
    image_filename = os.path.basename(image_path)
    image_name = os.path.splitext(image_filename)[0]
    tif_image = get_georeferenced_image(feature=feature, image_path=image_path)
    new_layer = QgsRasterLayer(tif_image, image_name)
    new_layer.triggerRepaint()

    QgsProject.instance().addMapLayer(new_layer, False)
    results_group.addLayer(new_layer)
    iface.mapCanvas().refresh()


def zoom_selected_features(layer):
    """Zoom to selected features in layer."""

    if layer is not None:
        source_bbox = layer.boundingBoxOfSelected()
        bbox = get_bounding_box_transformed(source_bbox, layer.crs(), QgsCoordinateReferenceSystem(DEFAULT_TARGET_CRS))
        margin = 1
        bbox.scale(1 + margin)
        canvas = iface.mapCanvas()
        canvas.setExtent(bbox)
        canvas.refresh()
