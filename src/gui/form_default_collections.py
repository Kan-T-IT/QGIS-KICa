""" Collection selection form module."""

from PyQt5.QtCore import Qt

from core.collections import get_collections
from core.settings import PluginSettings
from gui.form_base import FormBase
from gui.helpers import forms
from ui.frm_default_collections import Ui_frm_default_collections
from utils import qgis_helper
from utils.exceptions import ProviderError


class FormDefaultCollections(FormBase, Ui_frm_default_collections):
    """Collection selection form class."""

    def __init__(self, parent=None, closing_plugin=None):
        super().__init__(parent=parent, accept_btn=True, closing_plugin=closing_plugin)

        self.setWindowTitle('Catalog selection')

        self.btn_accept.clicked.connect(self.btn_accept_clicked)
        self.btn_filter_results.clicked.connect(self.btn_filter_results_clicked)
        self.btn_add_selected.clicked.connect(self.btn_add_selected_clicked)
        self.btn_remove_selected.clicked.connect(self.btn_remove_selected_clicked)

        self.btn_filter_results.setGraphicsEffect(forms.get_shadow_effect())
        self.btn_add_selected.setGraphicsEffect(forms.get_shadow_effect())
        self.btn_remove_selected.setGraphicsEffect(forms.get_shadow_effect())

        self.settings = PluginSettings()
        self.selected_collections = self.settings.selected_collections or []
        self.providers = self.settings.get_active_providers()

        print(f'providers: {self.providers}')
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
        self.btn_filter_results.setText('Getting collections...')

        if len(self.providers) == 0:
            qgis_helper.warning_message(
                'Warning', 'You must set valid credentials for at least one provider in the plugin settings.'
            )
            return

        search_text = self.txt_search.text().strip()

        results = []
        for provider in self.providers:
            try:
                data = get_collections(provider, {})
            except ProviderError as ex:
                qgis_helper.warning_message('Warning', f'{provider}: {ex.message}')
                continue

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
                    and search_text.lower()
                    not in provider.lower() + collection['title'].lower() + collection['hostName'].lower()
                ):
                    continue

                collection['provider'] = provider
                collection['selected'] = any(
                    col['provider'] == provider and col['name'] == collection['name']
                    for col in self.selected_collections
                )

                results.append(collection)

        self.load_filtered_collections(results)

        self.btn_filter_results.setText('Filter results')
        self.frame_content.setDisabled(False)

    def load_filtered_collections(self, data):
        """Load filtered collections in table."""

        headers = [
            '',
            '',
            'Provider',
            'Name',
            'Type',
            'Resolution',
            'Description',
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
            'Provider',
            'Name',
            'Type',
            'Resolution',
            'Description',
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
