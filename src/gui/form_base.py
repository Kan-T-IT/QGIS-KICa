from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import (
    QDialog,
    QFrame,
    QHBoxLayout,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
)

from gui.helpers import forms
from utils.helpers import tr


class FormBase(QDialog):
    def __init__(
        self,
        parent=None,
        accept_btn=False,
        cancel_btn=False,
        close_btn=True,
        closing_plugin=None,
    ):
        super().__init__()

        self.setupUi(self)
        self.parent = parent
        self.setAttribute(Qt.WA_DeleteOnClose)

        try:
            self.closing_plugin = parent.closing_plugin
        except:  # noqa: E722
            self.closing_plugin = closing_plugin

        if self.closing_plugin is not None:
            self.closing_plugin.connect(self.close)

        forms.set_form_stylesheet(self)
        self.set_control_buttons(accept_btn, cancel_btn, close_btn)

    def set_control_buttons(self, accept_btn, cancel_btn, close_btn):
        if not accept_btn and not cancel_btn and not close_btn:
            return

        default_widget_size = QSize(110, 30)

        self.layout_control = QHBoxLayout()

        spacerItem = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.layout_control.addSpacerItem(spacerItem)

        if accept_btn:
            self.btn_accept = QPushButton(tr('Accept'))
            self.btn_accept.setObjectName('btn_accept')
            self.btn_accept.setFixedSize(default_widget_size)
            self.layout_control.addWidget(self.btn_accept)
            self.btn_accept.setGraphicsEffect(forms.get_shadow_effect())

        if cancel_btn:
            self.btn_cancel = QPushButton(tr('Cancel'))
            self.btn_cancel.setObjectName('btn_cancel')
            self.btn_cancel.setFixedSize(default_widget_size)
            self.layout_control.addWidget(self.btn_cancel)
            self.btn_cancel.setGraphicsEffect(forms.get_shadow_effect())

        if close_btn:
            self.btn_close = QPushButton(tr('Close'))
            self.btn_close.setObjectName('btn_close')
            self.btn_close.setFixedSize(default_widget_size)
            self.layout_control.addWidget(self.btn_close)
            self.btn_close.setGraphicsEffect(forms.get_shadow_effect())
            self.btn_close.clicked.connect(self.btn_close_click)

        self.layout_control.setSpacing(20)
        frame = QFrame()
        frame.setLayout(self.layout_control)
        frame.setFixedHeight(50)
        frame.setFrameShape(QFrame.NoFrame)
        frame.layout().setContentsMargins(10, 10, 10, 10)
        self.layout().addWidget(frame)

    def btn_close_click(self):
        self.close()
