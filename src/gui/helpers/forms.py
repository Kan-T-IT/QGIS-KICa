""" Form helpers functions module."""

import decimal
import os

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QFontMetrics, QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import (
    QAbstractItemView,
    QComboBox,
    QGraphicsDropShadowEffect,
    QHeaderView,
    QLineEdit,
    QTableWidgetItem,
)

from utils.constants import StyleVariables
from utils.exceptions import PluginError
from utils.general import get_plugin_dir
from utils.helpers import tr


def load_combobox(obj_combobox, key_member, value_member, lst_data, block_signals=False):
    """Load a QComboBox with provided data."""

    if block_signals:
        obj_combobox.blockSignals(True)

    obj_combobox.clear()
    items_array = []

    for d in lst_data:
        default_value = str(d)
        if not isinstance(d, dict):
            d = d.__dict__

        key = d[key_member]
        value = d[value_member] if value_member else default_value
        items_array.append((str(value), str(key), d))

    model = QStandardItemModel(0, 1)
    for value, key, data in items_array:
        item = QStandardItem(value)
        item.setData(key, Qt.UserRole)
        item.setData(data, Qt.UserRole + 1)
        model.appendRow(item)

    obj_combobox.setModel(model)
    if block_signals:
        obj_combobox.blockSignals(False)


def set_form_stylesheet(parent):
    """Set stylesheet to a form."""

    plugin_dir = get_plugin_dir()
    qss_path = os.path.join(plugin_dir, 'styles.qss')

    with open(qss_path, 'r') as qss_file:
        _style = qss_file.read()

    for key, value in StyleVariables.to_dict().items():
        # print(f'set_form_stylesheet -> key: @{key} value: {value}')
        _style = _style.replace(f'@{key}', value)

    parent.setStyleSheet(_style)


def set_elided_text_to_label(label, text):
    """Set elided text to a QLabel if the text is too long."""

    label.setToolTip(text)
    metrix = QFontMetrics(label.font())
    width = label.width() - 2

    aux_margin = 30
    clipped_text = text
    if metrix.width(text) - aux_margin > width:
        clipped_text = metrix.elidedText(text, Qt.ElideRight, width)

    label.setText(clipped_text)


def set_tooltips(form):
    """Set tooltips to all QLineEdit widgets in a form."""

    for w in form.findChildren(QLineEdit):
        w.setToolTip(w.text())


def get_shadow_effect():
    """Get shadow effect for widgets."""

    shadow = QGraphicsDropShadowEffect()
    shadow.setBlurRadius(5)
    shadow.setXOffset(2)
    shadow.setYOffset(3)
    # shadow.setColor(Qt.lightGray)
    shadow.setColor(QColor(210, 210, 210))
    return shadow


def init_tableview(obj_tableview, column_count, row_count, headers, default_row_height=25):
    """Initialize tableview with provided data, headers and columns."""

    obj_tableview.setColumnCount(column_count)
    obj_tableview.setRowCount(row_count)
    obj_tableview.setHorizontalHeaderLabels(headers)
    obj_tableview.setEditTriggers(QAbstractItemView.NoEditTriggers)
    obj_tableview.setSelectionBehavior(QAbstractItemView.SelectRows)
    obj_tableview.setSelectionMode(QAbstractItemView.SingleSelection)
    obj_tableview.setAlternatingRowColors(True)
    obj_tableview.setShowGrid(True)
    obj_tableview.setGridStyle(Qt.SolidLine)
    obj_tableview.setSortingEnabled(True)

    obj_tableview.horizontalHeader().setHighlightSections(False)

    v_header = obj_tableview.verticalHeader()
    v_header.setVisible(False)
    v_header.setDefaultSectionSize(default_row_height)

    return obj_tableview


def load_table_data(  # noqa: C901
    obj_table,
    data,
    headers=None,
    columns=[],
    fn_custom_items=[],
    cols_to_stretch=[],
    cols_width=[],
    cols_to_hide=[],
    add_dict_object=False,
    literal_values=False,
    default_row_height=25,
    default_alignment=None,
    checkable_columns=[],
    num_decimals=2,
):
    """Load table with provided data, headers and columns."""

    if not isinstance(data, list):
        raise PluginError(tr('The data parameter must be a list'))

    row_count = len(data)

    if len(headers) != len(columns):
        message_part_a = tr('Number of columns for')
        message_part_b = tr('does not match headers')
        message = f"{message_part_a} '{obj_table.objectName()}' {message_part_b}."
        raise PluginError(message)

    if not headers:
        headers = columns

    column_count = len(columns)

    init_tableview(obj_table, column_count, row_count, headers, default_row_height)
    obj_table.setTextElideMode(Qt.TextElideMode.ElideRight)
    header = obj_table.horizontalHeader()

    if not default_alignment:
        default_alignment = Qt.AlignLeft | Qt.AlignVCenter

    for col in range(len(columns)):
        if col in cols_to_hide:
            obj_table.setColumnHidden(col, True)

        # Columns to stretch to fill the container width
        if col in cols_to_stretch:
            header.setSectionResizeMode(col, QHeaderView.Stretch)
            continue

        # Set width or adjust width to content
        col_adjust_width = [i for i in cols_width if i[0] == col]
        if len(col_adjust_width) > 0:
            mi_col = col_adjust_width[0]
            obj_table.setColumnWidth(mi_col[0], mi_col[1])
        else:
            header.setSectionResizeMode(col, QHeaderView.ResizeToContents)

    idx_row = 0
    for obj_data in data:
        # If data is not a dict we convert it to dict
        if not isinstance(obj_data, dict):
            if getattr(obj_data, 'get_properties_as_dict', None):
                fila_data = obj_data.get_properties_as_dict(columns)
            else:
                fila_data = obj_data.__dict__
        else:
            fila_data = obj_data

        idx_col = 0
        for col in columns:
            if isinstance(col, tuple):
                value = fila_data[col[0]]
                for i in range(1, len(col)):
                    value = value[col[i]]
            else:
                if literal_values:
                    value = str(fila_data.get(col))
                else:
                    value = fila_data.get(col)

            # custom item?
            item_custom = None
            for fn_custom in fn_custom_items:
                if fn_custom[0] == idx_col:
                    item_custom = fn_custom[1](fila_data)
                    obj_table.setCellWidget(idx_row, idx_col, item_custom)
                    break

            if item_custom and isinstance(item_custom, QComboBox):
                # If item is QComboBox, gets selected value
                selected_index = item_custom.findData(value)
                item_custom.setCurrentIndex(selected_index)

            # Adds checkbox to column
            is_checkable = idx_col in checkable_columns
            if is_checkable:
                chk_box_item = QTableWidgetItem()
                chk_box_item.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
                check_state = Qt.Checked if value else Qt.Unchecked
                chk_box_item.setCheckState(check_state)
                obj_table.setItem(idx_row, idx_col, chk_box_item)

            if (item_custom or is_checkable) and add_dict_object and idx_col == 0:
                # Is not allowed to save the dictionary in a column that is checkable or custom,
                # in this case an additional empty column can be added as index 0 and hide it.
                raise PluginError(
                    tr('The load_table method does not support set a dictionary in a custom item cell.')  # noqa: E501
                )

            if not item_custom and not is_checkable:
                value = value if value is not None else ''

                # Default format for float values
                if isinstance(value, (decimal.Decimal, float)):
                    # value = "{:,.2f}".format(value)
                    value = f'{value:,.{num_decimals}f}'
                    alignment = Qt.AlignRight | Qt.AlignVCenter
                else:
                    value = str(value)
                    alignment = default_alignment

                item = QTableWidgetItem(value)
                item.setTextAlignment(alignment)
                item.setToolTip(value)

                if add_dict_object and idx_col == 0:  # Save the object in the first column to simplify the selection
                    item.setData(Qt.UserRole, obj_data)

                obj_table.setItem(idx_row, idx_col, item)

            idx_col = idx_col + 1
        idx_row = idx_row + 1


def check_int_not_empty(txt_widget):
    """Check if the value is an integer and greater than 0 in a QLineEdit."""

    value = None
    try:
        value = int(txt_widget.text())
    except:  # noqa: E722
        pass

    if value is not None and value > 0:
        txt_widget.setStyleSheet('')
    else:
        txt_widget.setStyleSheet('background-color: red;')
