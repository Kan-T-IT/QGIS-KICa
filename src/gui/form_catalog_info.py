""" Form Catalog Info Module. """

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidget

from gui.form_base import FormBase
from gui.helpers import forms
from ui.frm_catalog_info import Ui_frm_catalog_info
from utils.helpers import tr


class FormCatalogInfo(FormBase, Ui_frm_catalog_info):
    """Form Catalog Info Class."""

    def __init__(self, parent=None, data=None, closing_plugin=None):
        super().__init__(parent=parent, closing_plugin=closing_plugin)
        self.setAttribute(Qt.WA_DeleteOnClose)

        self.setWindowTitle(tr('Information about the selected view.'))

        data = self.normalize_dict_data(data['properties'])
        table_data = []
        for key, value in data.items():
            table_data.append({'key': key, 'value': value})

        self.load_data(table_data)

    def normalize_dict_data(self, data):
        """Normalize data to be loaded in table."""

        new_data = {}
        for key, value in data.items():
            if isinstance(value, dict):
                for key2, value2 in value.items():
                    new_data[f'{key}/{key2}'] = value2
            else:
                new_data[key] = value

        return new_data

    def load_data(self, data):
        """Load data in table."""

        headers = ['', 'Key', 'Value']
        columns = ['', 'key', 'value']

        forms.load_table_data(
            obj_table=self.tbl_catalog_info,
            data=data,
            headers=headers,
            cols_to_hide=[0],
            columns=columns,
            cols_to_stretch=[2],
            add_dict_object=True,
        )

        self.tbl_catalog_info.setSelectionBehavior(QTableWidget.SelectItems)
