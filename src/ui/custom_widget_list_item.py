# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/fernando/proyectos_kan/plugins-qgis/kan-imagery-catalog/QGIS-KICa/src/ui/custom_widget_list_item.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CustomWidgetListItem(object):
    def setupUi(self, CustomWidgetListItem):
        CustomWidgetListItem.setObjectName("CustomWidgetListItem")
        CustomWidgetListItem.resize(297, 55)
        CustomWidgetListItem.setWindowTitle("")
        self.verticalLayout = QtWidgets.QVBoxLayout(CustomWidgetListItem)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_main = QtWidgets.QFrame(CustomWidgetListItem)
        self.frame_main.setMinimumSize(QtCore.QSize(0, 55))
        self.frame_main.setMaximumSize(QtCore.QSize(16777215, 55))
        self.frame_main.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_main.setObjectName("frame_main")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_main)
        self.horizontalLayout.setContentsMargins(6, 5, 6, 5)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lbl_thumbnail = QtWidgets.QLabel(self.frame_main)
        self.lbl_thumbnail.setMinimumSize(QtCore.QSize(40, 40))
        self.lbl_thumbnail.setMaximumSize(QtCore.QSize(40, 40))
        self.lbl_thumbnail.setText("TextLabel")
        self.lbl_thumbnail.setObjectName("lbl_thumbnail")
        self.horizontalLayout.addWidget(self.lbl_thumbnail)
        self.frame_data = QtWidgets.QFrame(self.frame_main)
        self.frame_data.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_data.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_data.setObjectName("frame_data")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_data)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.lbl_item_name = QtWidgets.QLabel(self.frame_data)
        self.lbl_item_name.setMinimumSize(QtCore.QSize(150, 20))
        self.lbl_item_name.setMaximumSize(QtCore.QSize(16777215, 20))
        self.lbl_item_name.setText("TextLabel")
        self.lbl_item_name.setObjectName("lbl_item_name")
        self.gridLayout.addWidget(self.lbl_item_name, 0, 0, 1, 1)
        self.frame_item_info = QtWidgets.QFrame(self.frame_data)
        self.frame_item_info.setMinimumSize(QtCore.QSize(0, 25))
        self.frame_item_info.setMaximumSize(QtCore.QSize(16777215, 25))
        self.frame_item_info.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_item_info.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_item_info.setObjectName("frame_item_info")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_item_info)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setHorizontalSpacing(3)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lbl_date_text = QtWidgets.QLabel(self.frame_item_info)
        self.lbl_date_text.setMinimumSize(QtCore.QSize(0, 20))
        self.lbl_date_text.setMaximumSize(QtCore.QSize(16777215, 20))
        self.lbl_date_text.setText("...")
        self.lbl_date_text.setObjectName("lbl_date_text")
        self.gridLayout_2.addWidget(self.lbl_date_text, 0, 1, 1, 1)
        self.lbl_angle_text = QtWidgets.QLabel(self.frame_item_info)
        self.lbl_angle_text.setMinimumSize(QtCore.QSize(0, 20))
        self.lbl_angle_text.setMaximumSize(QtCore.QSize(16777215, 20))
        self.lbl_angle_text.setText("...")
        self.lbl_angle_text.setObjectName("lbl_angle_text")
        self.gridLayout_2.addWidget(self.lbl_angle_text, 0, 3, 1, 1)
        self.lbl_angle_icon = QtWidgets.QLabel(self.frame_item_info)
        self.lbl_angle_icon.setMinimumSize(QtCore.QSize(16, 16))
        self.lbl_angle_icon.setMaximumSize(QtCore.QSize(16, 16))
        self.lbl_angle_icon.setText("")
        self.lbl_angle_icon.setPixmap(QtGui.QPixmap(":/resources/icons/triangle.svg"))
        self.lbl_angle_icon.setScaledContents(True)
        self.lbl_angle_icon.setObjectName("lbl_angle_icon")
        self.gridLayout_2.addWidget(self.lbl_angle_icon, 0, 2, 1, 1)
        self.lbl_date_icon = QtWidgets.QLabel(self.frame_item_info)
        self.lbl_date_icon.setMinimumSize(QtCore.QSize(16, 16))
        self.lbl_date_icon.setMaximumSize(QtCore.QSize(16, 16))
        self.lbl_date_icon.setText("")
        self.lbl_date_icon.setPixmap(QtGui.QPixmap(":/resources/icons/calendar.svg"))
        self.lbl_date_icon.setScaledContents(True)
        self.lbl_date_icon.setObjectName("lbl_date_icon")
        self.gridLayout_2.addWidget(self.lbl_date_icon, 0, 0, 1, 1)
        self.lbl_cloud_coverage_icon = QtWidgets.QLabel(self.frame_item_info)
        self.lbl_cloud_coverage_icon.setMinimumSize(QtCore.QSize(16, 16))
        self.lbl_cloud_coverage_icon.setMaximumSize(QtCore.QSize(16, 16))
        self.lbl_cloud_coverage_icon.setText("")
        self.lbl_cloud_coverage_icon.setPixmap(QtGui.QPixmap(":/resources/icons/cloud.svg"))
        self.lbl_cloud_coverage_icon.setScaledContents(True)
        self.lbl_cloud_coverage_icon.setObjectName("lbl_cloud_coverage_icon")
        self.gridLayout_2.addWidget(self.lbl_cloud_coverage_icon, 0, 4, 1, 1)
        self.lbl_cloud_coverage_text = QtWidgets.QLabel(self.frame_item_info)
        self.lbl_cloud_coverage_text.setMinimumSize(QtCore.QSize(0, 20))
        self.lbl_cloud_coverage_text.setMaximumSize(QtCore.QSize(16777215, 20))
        self.lbl_cloud_coverage_text.setText("...")
        self.lbl_cloud_coverage_text.setObjectName("lbl_cloud_coverage_text")
        self.gridLayout_2.addWidget(self.lbl_cloud_coverage_text, 0, 5, 1, 1)
        self.gridLayout_2.setColumnStretch(1, 1)
        self.gridLayout_2.setColumnStretch(3, 1)
        self.gridLayout_2.setColumnStretch(5, 1)
        self.gridLayout.addWidget(self.frame_item_info, 2, 0, 1, 2)
        self.frame_buttons = QtWidgets.QFrame(self.frame_data)
        self.frame_buttons.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_buttons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_buttons.setObjectName("frame_buttons")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_buttons)
        self.horizontalLayout_2.setContentsMargins(0, 0, 3, 0)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.btn_details = QtWidgets.QPushButton(self.frame_buttons)
        self.btn_details.setMinimumSize(QtCore.QSize(20, 20))
        self.btn_details.setMaximumSize(QtCore.QSize(20, 20))
        self.btn_details.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/resources/icons/info.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_details.setIcon(icon)
        self.btn_details.setIconSize(QtCore.QSize(16, 16))
        self.btn_details.setFlat(False)
        self.btn_details.setObjectName("btn_details")
        self.horizontalLayout_2.addWidget(self.btn_details)
        self.btn_view = QtWidgets.QPushButton(self.frame_buttons)
        self.btn_view.setMinimumSize(QtCore.QSize(20, 20))
        self.btn_view.setMaximumSize(QtCore.QSize(20, 20))
        self.btn_view.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/resources/icons/view.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_view.setIcon(icon1)
        self.btn_view.setIconSize(QtCore.QSize(16, 16))
        self.btn_view.setObjectName("btn_view")
        self.horizontalLayout_2.addWidget(self.btn_view)
        self.btn_download = QtWidgets.QPushButton(self.frame_buttons)
        self.btn_download.setMinimumSize(QtCore.QSize(20, 20))
        self.btn_download.setMaximumSize(QtCore.QSize(20, 20))
        self.btn_download.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/resources/icons/download.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_download.setIcon(icon2)
        self.btn_download.setIconSize(QtCore.QSize(16, 16))
        self.btn_download.setObjectName("btn_download")
        self.horizontalLayout_2.addWidget(self.btn_download)
        self.gridLayout.addWidget(self.frame_buttons, 0, 1, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.horizontalLayout.addWidget(self.frame_data)
        self.verticalLayout.addWidget(self.frame_main)

        self.retranslateUi(CustomWidgetListItem)
        QtCore.QMetaObject.connectSlotsByName(CustomWidgetListItem)

    def retranslateUi(self, CustomWidgetListItem):
        pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CustomWidgetListItem = QtWidgets.QWidget()
    ui = Ui_CustomWidgetListItem()
    ui.setupUi(CustomWidgetListItem)
    CustomWidgetListItem.show()
    sys.exit(app.exec_())
