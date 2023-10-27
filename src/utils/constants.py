from enum import Enum

DEBUG_MODE = True

RESULTS_GROUP_NAME = 'kan_imagery_catalog_preview'
RESULTS_LAYER_NAME = 'kan_imagery_catalog_footprints'


class CustomEnum(Enum):
    def __repr__(self) -> str:
        return self.value

    def __str__(self) -> str:
        return str(self.value)

    def __eq__(self, other):
        if isinstance(other, str):
            return self.value.lower() == other.lower()

        if isinstance(other, Enum):
            return self.value == other.value

        return False

    @classmethod
    def listar(cls):
        return [e for e in cls]

    @classmethod
    def to_dict(cls) -> dict:
        return {i.name: i.value for i in cls}

    @classmethod
    def to_key_value_list(cls) -> list:
        return [{'key': i.name, 'value': i.value} for i in cls]


class StyleVariables(CustomEnum):
    FONT_SIZE_DEFAULT = '12px'
    FONT_SIZE_SMALL = '8px'
    COLOR_MAIN_DARK = '#6597AF'
    COLOR_MAIN_LIGHT = '#F5F5F5'
    COLOR_TEXT_DEFAULT = '#2D2D2D'
    COLOR_TEXT_LIGHT = '#E8E8E8'
    COLOR_BACKGROUND_DEFAULT = '#E8E8E8'


class MessageType:
    INFO = 0  # "Info", 0  # Qgis.Info
    WARNING = 1  # "Warning", 1  # Qgis.Warning
    CRITICAL = 2  # "Error", 2  # Qgis.Critical
    SUCCESS = 3  # "Success", 3  # Qgis.Success
