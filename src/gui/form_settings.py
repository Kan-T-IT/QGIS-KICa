""" Form settings module. """

from PyQt5.QtGui import QIntValidator

from core import providers
from core.settings import PluginSettings
from gui.form_base import FormBase
from gui.helpers import forms
from ui.frm_settings import Ui_frm_settings
from utils.helpers import tr


class FormSettings(FormBase, Ui_frm_settings):
    """Form PluginSettings Class."""

    def __init__(self, parent=None, closing_plugin=None):
        super().__init__(parent=parent, accept_btn=True, closing_plugin=closing_plugin)

        self.setWindowTitle(tr('Plugin settings'))

        int_validator = QIntValidator()
        self.txt_default_back_days.setValidator(int_validator)
        self.txt_default_back_days.textChanged.connect(self.txt_default_back_days_text_changed)

        self.txt_max_catalog_results.setValidator(int_validator)
        self.txt_max_catalog_results.textChanged.connect(self.txt_max_catalog_results_text_changed)

        self.txt_max_features_results.setValidator(int_validator)
        self.txt_max_features_results.textChanged.connect(self.txt_max_features_results_text_changed)

        self.slider_cloud_coverage.valueChanged.connect(self.update_cloud_coverage_label)
        self.btn_accept.clicked.connect(self.btn_accept_clicked)

        self.btn_up42_check_credentials.clicked.connect(self.btn_up42_check_credentials_clicked)
        self.btn_up42_check_credentials.setGraphicsEffect(forms.get_shadow_effect())

        self.btn_sentinelhub_check_credentials.clicked.connect(self.btn_sentinelhub_check_credentials_clicked)
        self.btn_sentinelhub_check_credentials.setGraphicsEffect(forms.get_shadow_effect())
        self.btn_download_dir.setGraphicsEffect(forms.get_shadow_effect())

        languages = [
            # {'key': 'spanish', 'value': 'Español'},
            # {'key': 'portuguese', 'value': 'Portugûese'},
            {'key': 'english', 'value': 'English'},
        ]

        forms.load_combobox(self.cbo_language, 'key', 'value', languages)

        self.settings = PluginSettings()

        self.cbo_language.setCurrentIndex(self.cbo_language.findData(self.settings.language))
        self.txt_default_back_days.setText(str(self.settings.back_days or 0))
        self.slider_cloud_coverage.setValue(int(self.settings.cloud_coverage or 0))
        self.txt_max_catalog_results.setText(str(self.settings.max_catalog_results or 0))
        self.txt_max_features_results.setText(str(self.settings.max_features_results or 0))
        self.txt_download_path.setText(self.settings.download_path)

        self.up42_settings = self.settings.provider_settings.get('up42', {})
        self.sentinelhub_settings = self.settings.provider_settings.get('sentinel_hub', {})
        self.planet_settings = self.settings.provider_settings.get('planet', {})

        self.up42_is_valid = self.up42_settings.get('valid', False)
        self.sentinelhub_is_valid = self.sentinelhub_settings.get('valid', False)
        self.planet_is_valid = self.planet_settings.get('valid', False)

        self.txt_up42_api_key.setText(self.up42_settings.get('api_key'))
        self.txt_up42_project_id.setText(self.up42_settings.get('project_id'))
        self.lbl_up42_check_credentials.setText('')

        self.txt_sentinelhub_client_id.setText(self.sentinelhub_settings.get('client_id'))
        self.txt_sentinelhub_client_secret.setText(self.sentinelhub_settings.get('client_secret'))
        self.lbl_sentinelhub_check_credentials.setText('')

    def update_cloud_coverage_label(self):
        """Update cloud coverage label text."""

        max_cloud_coverage_text = tr('Default max cloud coverage')
        self.lbl_cloud_coverage.setText(f'{max_cloud_coverage_text} ({self.slider_cloud_coverage.value()} %)  ')

    def btn_accept_clicked(self):
        """Event handler for accept button click."""

        self.btn_up42_check_credentials_clicked()
        self.btn_sentinelhub_check_credentials_clicked()

        self.settings.language = self.cbo_language.currentData()
        self.settings.back_days = int(self.txt_default_back_days.text())
        self.settings.cloud_coverage = int(self.slider_cloud_coverage.value())
        self.settings.download_path = self.txt_download_path.text()

        self.settings.max_catalog_results = int(self.txt_max_catalog_results.text())
        self.settings.max_features_results = int(self.txt_max_features_results.text())

        provider_settings = self.settings.provider_settings
        provider_settings['microsoft'] = {
            'valid': True,
        }
        provider_settings['up42'] = {
            'api_key': self.txt_up42_api_key.text(),
            'project_id': self.txt_up42_project_id.text(),
            'valid': self.up42_is_valid,
        }

        provider_settings['sentinel_hub'] = {
            'client_id': self.txt_sentinelhub_client_id.text(),
            'client_secret': self.txt_sentinelhub_client_secret.text(),
            'valid': self.sentinelhub_is_valid,
        }

        self.settings.provider_settings = provider_settings
        self.settings.save()
        self.close()

    def txt_default_back_days_text_changed(self):
        """Event handler for default back days text changed."""

        forms.check_int_not_empty(self.txt_default_back_days)

    def txt_max_catalog_results_text_changed(self):
        """Event handler for max catalog results text changed."""

        forms.check_int_not_empty(self.txt_max_catalog_results)

    def txt_max_features_results_text_changed(self):
        """Event handler for max features results text changed."""

        forms.check_int_not_empty(self.txt_max_features_results)

    def btn_up42_check_credentials_clicked(self):
        """Event handler for check credentials button click."""

        project_id = self.txt_up42_project_id.text()
        api_key = self.txt_up42_api_key.text()
        self.up42_is_valid = providers.check_credentials('up42', {'project_id': project_id, 'api_key': api_key})

        self.lbl_up42_check_credentials.setText(
            tr('The credentials are valid.') if self.up42_is_valid else tr('Verify the credentials entered.')
        )

    def btn_sentinelhub_check_credentials_clicked(self):
        """Event handler for check credentials button click."""

        client_id = self.txt_sentinelhub_client_id.text()
        client_secret = self.txt_sentinelhub_client_secret.text()
        self.sentinelhub_is_valid = providers.check_credentials(
            'sentinel_hub', {'client_id': client_id, 'client_secret': client_secret}
        )

        self.lbl_sentinelhub_check_credentials.setText(
            tr('The credentials are valid.') if self.sentinelhub_is_valid else tr('Verify the credentials entered.')
        )
