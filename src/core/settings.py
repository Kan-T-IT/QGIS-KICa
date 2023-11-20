"""PluginSettings module."""

import json
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

from utils import general, qgis_helper


@dataclass
class PluginSettings:
    """PluginSettings class."""

    language: str = 'english'
    back_days: int = 20
    cloud_coverage: int = 10
    max_catalog_results: int = 10
    max_features_results: int = 5
    download_path: str = './downloads'
    _last_cleaning_date: Optional[str] = None
    _provider_settings: dict = field(default_factory=dict)
    _selected_collections: list = field(default_factory=list)

    def __post_init__(self):
        """Init settings."""

        self.language = qgis_helper.read_setting('language', 'english')
        self.back_days = int(qgis_helper.read_setting('back_days', 20))
        self.cloud_coverage = int(qgis_helper.read_setting('cloud_coverage', 10))
        self.max_catalog_results = int(qgis_helper.read_setting('max_catalog_results', 10))
        self.max_features_results = int(qgis_helper.read_setting('max_features_results', 5))
        self.download_path = qgis_helper.read_setting('download_path', './downloads')
        self._last_cleaning_date = qgis_helper.read_setting('last_cleaning_date')

        default_provider_settings = "{'microsoft': {'valid': True}, 'element84': {'valid': True}}"
        self._provider_settings = qgis_helper.read_json_setting('provider_settings', default_provider_settings)
        self._selected_collections = qgis_helper.read_json_setting('selected_collections', '[]')

    def save(self):
        """Save settings."""

        qgis_helper.save_setting('language', self.language)
        qgis_helper.save_setting('back_days', self.back_days)
        qgis_helper.save_setting('cloud_coverage', self.cloud_coverage)
        qgis_helper.save_setting('max_catalog_results', self.max_catalog_results)
        qgis_helper.save_setting('max_features_results', self.max_features_results)
        qgis_helper.save_setting('download_path', self.download_path)

        qgis_helper.save_json_setting('provider_settings', self._provider_settings)
        qgis_helper.save_json_setting('selected_collections', self._selected_collections)

    def clean_temporary_files_if_needed(self):
        """Checks whether temporary files need to be deleted based on
        the days before the last activity date and delete files."""

        clean_temp_files = False
        if self.last_cleaning_date is None:
            clean_temp_files = True
        else:
            delta = datetime.now() - self.last_cleaning_date
            clean_temp_files = delta.days > 7

        if clean_temp_files:
            general.clean_temporary_files()
            self.update_last_cleaning_date()

    def update_last_cleaning_date(self):
        """Update last activity date."""

        last_cleaning_date = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S.%f')
        qgis_helper.save_setting('last_cleaning_date', last_cleaning_date)

    def get_active_providers(self) -> list:
        """Get active providers."""

        active_providers = []
        for provider, settings in self.provider_settings.items():
            if settings.get('valid', False):
                active_providers.append(provider)

        return active_providers

    @property
    def provider_settings(self) -> dict:
        self._provider_settings = qgis_helper.read_json_setting('provider_settings', '{}')
        return self._provider_settings

    @provider_settings.setter
    def provider_settings(self, value: dict) -> None:
        self._provider_settings = value

    @property
    def selected_collections(self) -> list:
        self._selected_collections = qgis_helper.read_json_setting('selected_collections', '{}')
        return self._selected_collections

    @selected_collections.setter
    def selected_collections(self, value: list) -> None:
        self._selected_collections = value

    @property
    def last_cleaning_date(self) -> datetime:
        _last_cleaning_date = datetime.now()
        try:
            _last_cleaning_date = datetime.strptime(self._last_cleaning_date, '%Y-%m-%d %H:%M:%S.%f')
        except TypeError:
            pass

        return _last_cleaning_date
