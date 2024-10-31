"""Custom widgets module."""

import os

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget

from core import catalogs, results
from gui.form_catalog_info import FormCatalogInfo
from gui.helpers import forms
from gui.helpers.worker import WorkerThread
from ui.custom_widget_list_item import Ui_CustomWidgetListItem
from utils.exceptions import PluginError
from utils.general import get_plugin_dir
from utils.helpers import open_url, tr


class CustomWidgetListItem(QWidget, Ui_CustomWidgetListItem):
    """Custom widget for list item."""

    def __init__(
        self,
        parent=None,
        provider_name='',
        host_name='',
        collection_name='',
        feature_data=None,
        thumbnail=None,
        acquisition_date='',
        incidence_angle=0.0,
        cloud_coverage=None,
        image_id=None,
        feature_index=None,
        footprints_layer=None,
        closing_plugin=None,
    ):
        super().__init__(parent)
        self.setupUi(self)

        self.closing_plugin = closing_plugin
        self.parent = parent
        self.btn_download.clicked.connect(self.download_images)
        self.btn_view.clicked.connect(self.show_quicklook)
        self.btn_details.clicked.connect(self.view_details)

        self.thread_quicklooks = WorkerThread()
        self.thread_quicklooks.progress_updated.connect(self.create_quicklook_layer)

        self.provider = provider_name
        self.host = host_name
        self.feature_data = feature_data
        self.footprints_layer = footprints_layer
        self.image_id = image_id
        self.feature_index = feature_index

        self._name = f'{self.provider}_{collection_name}'
        self._acquisition_date = acquisition_date
        self._incidence_angle = incidence_angle
        self._cloud_coverage = cloud_coverage

        str_acquisition_date = str(acquisition_date[0:10]) if acquisition_date else '---'
        self.lbl_date_text.setText(str_acquisition_date)

        str_incidence_angle = f'{round(incidence_angle or 0.0, 2)}°' if incidence_angle is not None else '---'
        self.lbl_angle_text.setText(str_incidence_angle)

        str_cloud_coverage = f'{int(cloud_coverage or 0)}%' if cloud_coverage is not None else '---'
        self.lbl_cloud_coverage_text.setText(str_cloud_coverage)

        # set name in label
        name = f'<b>{self.provider[0:4].upper()}</b> {collection_name}'
        self.lbl_item_name.setText(name)
        forms.set_elided_text_to_label(self.lbl_item_name, name)

        self.set_thumbnail(thumbnail)
        self.key = incidence_angle

    @property
    def name(self):
        return self._name

    @property
    def acquisition_date(self):
        return self._acquisition_date

    @property
    def incidence_angle(self):
        return self._incidence_angle

    @property
    def cloud_coverage(self):
        return self._cloud_coverage

    def set_thumbnail(self, image_bytes):
        """Set thumbnail image in label."""
        if not image_bytes:
            default_image_path = ':/resources/image_not_found.png'
            pixmap = QPixmap(default_image_path)
        else:
            pixmap = QPixmap()
            pixmap.loadFromData(image_bytes)

        self.lbl_thumbnail.setPixmap(pixmap.scaled(60, 60))
        self.lbl_thumbnail.setAlignment(Qt.AlignCenter)

    # Buttons actions

    def download_images(self):
        """Download image action."""

        download_url = catalogs.get_download_url(self.provider)
        open_url(download_url)

    def view_details(self):
        """View details action."""

        frm = FormCatalogInfo(parent=self, data=self.feature_data, closing_plugin=self.closing_plugin)
        frm.exec()

    def show_quicklook(self):
        """Show quicklook action."""

        params = {
            'provider': self.provider,
            'host_name': self.host,
            'image_id': self.image_id,
            'feature_data': self.feature_data,
        }

        self.thread_quicklooks.start(self.get_quicklook_image, params)

    def get_quicklook_image(self, provider: str, host_name: str, image_id: str, feature_data: dict):
        """Get quicklook from host."""

        try:
            image_response = catalogs.get_quicklook(provider, host_name, image_id, feature_data)

            temp_directory = f'{get_plugin_dir()}/temp'
            if not os.path.isdir(temp_directory):
                os.makedirs(temp_directory)

            image_path = f'{temp_directory}/{image_id}.jpg'
            file = open(image_path, 'wb')
            file.write(image_response)
            file.close()

            progress_data = {'image_path': image_path, 'image_id': image_id, 'layer_name': image_id}
            self.thread_quicklooks.progress_updated.emit(progress_data)
        except PluginError as ex:
            self.thread_quicklooks.error_signal.emit(tr('Could not get a preview'), str(ex))

    def create_quicklook_layer(self, params: dict):
        """Create a layer with the quicklook."""

        image_path = params.get('image_path')
        image_id = params.get('image_id')
        layer_name = params.get('layer_name')
        new_layer = None

        try:
            new_layer = results.create_quicklook(image_path=image_path, image_id=image_id, layer_name=layer_name)
        except PluginError as ex:
            self.thread_quicklooks.error_signal.emit(tr('Could not get a preview'), str(ex))

        return new_layer
