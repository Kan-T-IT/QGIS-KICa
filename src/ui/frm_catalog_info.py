# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/fernando/proyectos_kan/plugins-qgis/kan-imagery-catalog/QGIS-KICa/src/ui/frm_catalog_info.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_frm_catalog_info(object):
    def setupUi(self, frm_catalog_info):
        frm_catalog_info.setObjectName("frm_catalog_info")
        frm_catalog_info.resize(827, 541)
        frm_catalog_info.setMinimumSize(QtCore.QSize(700, 220))
        frm_catalog_info.setMaximumSize(QtCore.QSize(999999, 999999))
        self.verticalLayout = QtWidgets.QVBoxLayout(frm_catalog_info)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_content = QtWidgets.QFrame(frm_catalog_info)
        self.frame_content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_content.setObjectName("frame_content")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_content)
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tbl_catalog_info = QtWidgets.QTableWidget(self.frame_content)
        self.tbl_catalog_info.setObjectName("tbl_catalog_info")
        self.tbl_catalog_info.setColumnCount(0)
        self.tbl_catalog_info.setRowCount(0)
        self.verticalLayout_2.addWidget(self.tbl_catalog_info)
        self.verticalLayout.addWidget(self.frame_content)

        self.retranslateUi(frm_catalog_info)
        QtCore.QMetaObject.connectSlotsByName(frm_catalog_info)

    def retranslateUi(self, frm_catalog_info):
        _translate = QtCore.QCoreApplication.translate
        frm_catalog_info.setWindowTitle(_translate("frm_catalog_info", "Settings"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    frm_catalog_info = QtWidgets.QWidget()
    ui = Ui_frm_catalog_info()
    ui.setupUi(frm_catalog_info)
    frm_catalog_info.show()
    sys.exit(app.exec_())
