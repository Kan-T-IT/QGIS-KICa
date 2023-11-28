""" Worker thread class. """

from PyQt5.QtCore import QThread, pyqtSignal

from utils.exceptions import AuthorizationError, DataNotFoundError, HostError, PluginError, ProviderError, SettingsError
from utils.helpers import tr


class WorkerThread(QThread):
    """Worker thread class."""

    finished = pyqtSignal()
    progress_updated = pyqtSignal(dict)
    error_signal = pyqtSignal(str, str)
    warning_signal = pyqtSignal(str, str)
    info_signal = pyqtSignal(str, str)

    def start(self, process, dict_params):
        """Start thread."""
        self.process = process
        self.kwargs = dict_params
        super().start()

    def run(self):
        """Run thread."""
        try:
            self.process(**self.kwargs)
        except (ProviderError, SettingsError, DataNotFoundError, AuthorizationError) as ex:
            self.warning_signal.emit(tr('Warning'), str(ex))

        except (HostError, PluginError, Exception) as ex:
            self.error_signal.emit(tr('Error'), str(ex))

        self.finished.emit()
