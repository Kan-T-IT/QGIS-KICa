""" QGIS helper functions module. """

import json

from PyQt5.QtCore import QVariant

from utils.constants import DEFAULT_CRS_SOURCE, DEFAULT_CRS_TARGET
from utils.exceptions import DataNotFoundError
from utils.general import PLUGIN_NAME

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
        QgsPointXY,
        QgsProject,
        QgsProperty,
        QgsRasterFillSymbolLayer,
        QgsSettings,
        QgsSymbolLayer,
        QgsUnitTypes,
        QgsVectorLayer,
    )
    from qgis.utils import iface
except Exception as ex:  # noqa: E722    pylint: disable=bare-except
    print('QGIS libraries could not be imported.\n', ex)


def get_bounding_box_canvas():
    """Get bounding box from canvas."""

    active_layer = iface.activeLayer()
    if not active_layer:
        raise DataNotFoundError('Must have at least one active layer.')

    crs_transform = QgsCoordinateReferenceSystem(DEFAULT_CRS_SOURCE)
    transform = QgsCoordinateTransform(active_layer.crs(), crs_transform, QgsProject.instance())

    bbox = iface.mapCanvas().extent()
    bbox_transformed = transform.transform(bbox)

    x_min = bbox_transformed.xMinimum()
    y_min = bbox_transformed.yMinimum()
    x_max = bbox_transformed.xMaximum()
    y_max = bbox_transformed.yMaximum()

    return {'x_min': x_min, 'y_min': y_min, 'x_max': x_max, 'y_max': y_max}


def get_bounding_box_selected_feature(layer_name):
    """Get bounding box from selected feature."""

    layers = QgsProject.instance().mapLayersByName(layer_name)
    if not layers:
        raise DataNotFoundError('Error', 'The specified layer was not found.')

    layer = layers[0]
    if layer.selectedFeatureCount() > 0:
        selected_feature = layer.selectedFeatures()[0]
        bbox = selected_feature.geometry().boundingBox()

        crs_transform = QgsCoordinateReferenceSystem(DEFAULT_CRS_SOURCE)
        transform = QgsCoordinateTransform(iface.activeLayer().crs(), crs_transform, QgsProject.instance())

        bbox_transformed = transform.transform(bbox)

        x_min = bbox_transformed.xMinimum()
        y_min = bbox_transformed.yMinimum()
        x_max = bbox_transformed.xMaximum()
        y_max = bbox_transformed.yMaximum()

        return {'x_min': x_min, 'y_min': y_min, 'x_max': x_max, 'y_max': y_max}

    raise DataNotFoundError('There are no features selected on the specified layer.')


def get_single_polygon_layers():
    """Get single polygon layers from current project."""

    layer_list = []
    for layer in QgsProject.instance().mapLayers().values():
        if isinstance(layer, QgsVectorLayer) and layer.wkbType() == 3:
            layer_list.append(layer.name())

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

    if json_setting is not None:
        value = json.loads(json_setting)
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

    iface.messageBar().pushMessage(title, text, level=Qgis.Warning)


def info_message(title, text):
    """Show info message."""

    iface.messageBar().pushMessage(title, text, level=Qgis.Info)


def success_message(title, text):
    """Show success message."""

    iface.messageBar().pushMessage(title, text, level=Qgis.Success)


def get_or_create_group(group_name):
    """Get or create group."""

    root = QgsProject.instance().layerTreeRoot()
    results_group = None
    for child in root.children():
        # Use of casefold is to avoid problems with special characters specially on windows
        if child.name().casefold() == group_name.casefold():

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
        footprints_layer = QgsVectorLayer(f'{layer_type}?crs={DEFAULT_CRS_TARGET}', layer_name, 'memory')

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
        fields.append(QgsField('ID', QVariant.String))
        pr.addAttributes(fields)
        footprints_layer.updateFields()
        footprints_layer.triggerRepaint()

        QgsProject.instance().addMapLayer(footprints_layer, False)
        results_group.addLayer(footprints_layer)

    return footprints_layer


def add_feature_to_layer(coordinates, feature_id, layer):
    """Add feature to layer."""

    source_crs = QgsCoordinateReferenceSystem(DEFAULT_CRS_SOURCE)
    transform = QgsCoordinateTransform(source_crs, layer.crs(), QgsProject.instance())
    points = [transform.transform(QgsPointXY(point[0], point[1])) for point in coordinates]
    polygon = QgsGeometry.fromPolygonXY([points])

    feature = QgsFeature()
    feature.setGeometry(polygon)
    feature.setAttributes([feature_id])

    pr = layer.dataProvider()
    pr.addFeature(feature)
    return layer


def create_quicklook_layer(
    layer_name,
    group_name,
    feature,
    image_path=None,
):
    """Create a layer with a quicklook image."""

    layer_type = 'Polygon'
    results_group = get_or_create_group(group_name)

    new_layer = QgsVectorLayer(f'{layer_type}?crs={DEFAULT_CRS_TARGET}', layer_name, 'memory')
    new_layer_data_provider = new_layer.dataProvider()
    new_layer_data_provider.addFeatures([feature])

    symbol = QgsFillSymbol.createSimple(
        {
            'color': '255,0,0,0',
            'outline_color': 'transparent',
            'outline_width': '0',
        }
    )

    symbol_layer = QgsRasterFillSymbolLayer(image_path)
    symbol_layer.setWidthUnit(QgsUnitTypes.RenderMapUnits)

    data_defined = QgsProperty.fromExpression('bounds_width(@geometry)')
    symbol_layer.setDataDefinedProperty(QgsSymbolLayer.PropertyWidth, data_defined)

    symbol.appendSymbolLayer(symbol_layer)
    new_layer.renderer().setSymbol(symbol)
    new_layer.triggerRepaint()

    QgsProject.instance().addMapLayer(new_layer, False)
    results_group.addLayer(new_layer)
