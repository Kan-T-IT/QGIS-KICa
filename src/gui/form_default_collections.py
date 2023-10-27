""" Collection selection form module."""

from PyQt5.QtCore import Qt

from core.collections import get_collections
from core.settings import PluginSettings
from gui.form_base import FormBase
from gui.helpers import forms
from ui.frm_default_collections import Ui_frm_default_collections
from utils import qgis_helper


class FormDefaultCollections(FormBase, Ui_frm_default_collections):
    """Collection selection form class."""

    def __init__(self, parent=None, closing_plugin=None):
        super().__init__(parent=parent, accept_btn=True, closing_plugin=closing_plugin)

        self.setWindowTitle('Selección de catálogos')

        self.btn_accept.clicked.connect(self.btn_accept_clicked)
        self.btn_filter_results.clicked.connect(self.btn_filter_results_clicked)
        self.btn_add_selected.clicked.connect(self.btn_add_selected_clicked)
        self.btn_remove_selected.clicked.connect(self.btn_remove_selected_clicked)

        self.btn_filter_results.setGraphicsEffect(forms.get_shadow_effect())
        self.btn_add_selected.setGraphicsEffect(forms.get_shadow_effect())
        self.btn_remove_selected.setGraphicsEffect(forms.get_shadow_effect())

        self.settings = PluginSettings()
        self.selected_collections = self.settings.selected_collections or []
        self.providers = []
        for provider_name, provider_settings in self.settings.provider_settings.items():
            if provider_settings['valid']:
                self.providers.append(provider_name)

        self.btn_filter_results_clicked()
        self.load_selected_collections()

    # TODO: Agregar las selecciones a la configuración
    def btn_accept_clicked(self):
        """Event handler for accept button click."""

        self.settings.selected_collections = self.selected_collections
        self.settings.save()
        self.close()

    def btn_add_selected_clicked(self):
        """Event handler for add selected button click."""

        for row in range(self.tbl_provider_collections.rowCount()):
            check_selected = self.tbl_provider_collections.item(row, 1)
            if check_selected.checkState() == Qt.Checked:
                data = self.tbl_provider_collections.item(row, 0).data(Qt.UserRole)
                self.selected_collections.append(data)

        self.btn_filter_results_clicked()
        self.load_selected_collections()

    def btn_remove_selected_clicked(self):
        """Event handler for remove selected button click."""

        self.selected_collections = []

        for row in range(self.tbl_selected_collections.rowCount()):
            check_selected = self.tbl_selected_collections.item(row, 1)
            if check_selected.checkState() != Qt.Checked:
                data = self.tbl_selected_collections.item(row, 0).data(Qt.UserRole)
                data['selected'] = False
                self.selected_collections.append(data)

        self.btn_filter_results_clicked()
        self.load_selected_collections()

    def btn_filter_results_clicked(self):
        """Event handler for filter results button click."""

        self.frame_content.setDisabled(True)
        self.btn_filter_results.setText('Consultando colecciones...')

        if len(self.providers) == 0:
            qgis_helper.warning_message(
                'Atención',
                'Debe definir las credenciales válidas de al menos un proveedor en la ventana de configuración.',
            )
            return

        search_text = self.txt_search.text().strip()

        results = []
        for provider in self.providers:
            data = get_collections(provider, {})
            for collection in data:
                is_selected = False
                for selected_collection in self.selected_collections:
                    if (
                        selected_collection['provider'] == provider
                        and selected_collection['name'] == collection['name']
                    ):
                        is_selected = True
                        break

                if is_selected:
                    continue

                if (
                    search_text != ''
                    and search_text.lower() not in collection['title'].lower() + collection['hostName'].lower()
                ):
                    continue

                collection['provider'] = provider
                collection['sensor_type'] = 'Optical' if collection['isOptical'] else 'Non-Optical'
                collection['min_resolution'] = collection['resolutionValue'].get('minimum')
                collection['selected'] = any(
                    col['provider'] == provider and col['name'] == collection['name']
                    for col in self.selected_collections
                )

                results.append(collection)

        self.load_filtered_collections(results)

        self.btn_filter_results.setText('Filtrar')
        self.frame_content.setDisabled(False)

    def load_filtered_collections(self, data):
        """Load filtered collections in table."""

        headers = [
            '',
            '',
            'Proveedor',
            'Nombre',
            'Tipo',
            'Resolución',
            'Descripción',
        ]
        columns = [
            '',
            'selected',
            'provider',
            'title',
            'sensor_type',
            'min_resolution',
            'description',
        ]

        forms.load_table_data(
            obj_table=self.tbl_provider_collections,
            data=data,
            headers=headers,
            checkable_columns=[1],
            cols_to_hide=[0],
            columns=columns,
            cols_to_stretch=[],
            add_dict_object=True,
        )

    def load_selected_collections(self):
        """Load selected collections in table."""

        headers = [
            '',
            '',
            'Proveedor',
            'Nombre',
            'Tipo',
            'Resolución',
            'Descripción',
        ]
        columns = [
            '',
            'selected',
            'provider',
            'title',
            'sensor_type',
            'min_resolution',
            'description',
        ]

        forms.load_table_data(
            obj_table=self.tbl_selected_collections,
            data=self.selected_collections,
            headers=headers,
            checkable_columns=[1],
            cols_to_hide=[0],
            columns=columns,
            cols_to_stretch=[],
            add_dict_object=True,
        )
