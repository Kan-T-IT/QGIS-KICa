""" Constants module. """

from enum import Enum

DEBUG_MODE = True

RESULTS_GROUP_NAME = 'kan_imagery_catalog_preview'
RESULTS_LAYER_NAME = 'kan_imagery_catalog_footprints'

DEFAULT_CRS_SOURCE = 'EPSG:4326'
DEFAULT_CRS_TARGET = 'EPSG:3857'


class CustomEnum(Enum):
    """Custom Enum class."""

    def __repr__(self) -> str:
        """Override the default repr behavior."""
        return self.value

    def __str__(self) -> str:
        """Override the default str behavior."""

        return str(self.value)

    def __eq__(self, other):
        """Override the default eq behavior."""

        if isinstance(other, str):
            return self.value.lower() == other.lower()

        if isinstance(other, Enum):
            return self.value == other.value

        return False

    @classmethod
    def to_dict(cls) -> dict:
        """Convert enum to dict."""

        return {i.name: i.value for i in cls}


class StyleVariables(CustomEnum):
    """Style variables for qss stylesheet."""

    FONT_SIZE_DEFAULT = '12px'
    FONT_SIZE_SMALL = '8px'
    COLOR_MAIN_DARK = '#6597AF'
    COLOR_MAIN_LIGHT = '#F5F5F5'
    COLOR_TEXT_DEFAULT = '#2D2D2D'
    COLOR_TEXT_LIGHT = '#E8E8E8'
    COLOR_BACKGROUND_DEFAULT = '#E8E8E8'


class MessageType:
    """Qgis Message types."""

    INFO = 0  # "Info", 0  # Qgis.Info
    WARNING = 1  # "Warning", 1  # Qgis.Warning
    CRITICAL = 2  # "Error", 2  # Qgis.Critical
    SUCCESS = 3  # "Success", 3  # Qgis.Success
