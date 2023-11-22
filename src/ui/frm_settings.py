# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/fernando/proyectos_kan/plugins-qgis/kan-imagery-catalog/github/QGIS-KICa/src/ui/frm_settings.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_frm_settings(object):
    def setupUi(self, frm_settings):
        frm_settings.setObjectName("frm_settings")
        frm_settings.resize(645, 600)
        frm_settings.setMinimumSize(QtCore.QSize(535, 600))
        frm_settings.setMaximumSize(QtCore.QSize(800, 650))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(frm_settings)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_content = QtWidgets.QFrame(frm_settings)
        self.frame_content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_content.setObjectName("frame_content")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_content)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.frame_content)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_8.setContentsMargins(-1, -1, -1, 20)
        self.gridLayout_8.setVerticalSpacing(6)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.btn_download_dir = QtWidgets.QPushButton(self.frame_2)
        self.btn_download_dir.setMinimumSize(QtCore.QSize(30, 30))
        self.btn_download_dir.setMaximumSize(QtCore.QSize(30, 30))
        self.btn_download_dir.setText("...")
        self.btn_download_dir.setObjectName("btn_download_dir")
        self.gridLayout_8.addWidget(self.btn_download_dir, 3, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setObjectName("label")
        self.gridLayout_8.addWidget(self.label, 3, 0, 1, 1)
        self.frame_6 = QtWidgets.QFrame(self.frame_2)
        self.frame_6.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_cloud_coverage = QtWidgets.QFrame(self.frame_6)
        self.frame_cloud_coverage.setMinimumSize(QtCore.QSize(160, 40))
        self.frame_cloud_coverage.setMaximumSize(QtCore.QSize(999, 40))
        self.frame_cloud_coverage.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_cloud_coverage.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_cloud_coverage.setObjectName("frame_cloud_coverage")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_cloud_coverage)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 2, 0, 1, 1)
        self.frame_percentage = QtWidgets.QFrame(self.frame_cloud_coverage)
        self.frame_percentage.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.frame_percentage.setFont(font)
        self.frame_percentage.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_percentage.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_percentage.setObjectName("frame_percentage")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_percentage)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lbl_0_percent = QtWidgets.QLabel(self.frame_percentage)
        self.lbl_0_percent.setText("0%")
        self.lbl_0_percent.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbl_0_percent.setObjectName("lbl_0_percent")
        self.horizontalLayout_4.addWidget(self.lbl_0_percent)
        self.lbl_25_percent = QtWidgets.QLabel(self.frame_percentage)
        self.lbl_25_percent.setText("25%")
        self.lbl_25_percent.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_25_percent.setObjectName("lbl_25_percent")
        self.horizontalLayout_4.addWidget(self.lbl_25_percent)
        self.lbl_50_percent = QtWidgets.QLabel(self.frame_percentage)
        self.lbl_50_percent.setText("50%")
        self.lbl_50_percent.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_50_percent.setObjectName("lbl_50_percent")
        self.horizontalLayout_4.addWidget(self.lbl_50_percent)
        self.lbl_75_percent = QtWidgets.QLabel(self.frame_percentage)
        self.lbl_75_percent.setText("75%")
        self.lbl_75_percent.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_75_percent.setObjectName("lbl_75_percent")
        self.horizontalLayout_4.addWidget(self.lbl_75_percent)
        self.lbl_100_percent = QtWidgets.QLabel(self.frame_percentage)
        self.lbl_100_percent.setText("100%")
        self.lbl_100_percent.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_100_percent.setObjectName("lbl_100_percent")
        self.horizontalLayout_4.addWidget(self.lbl_100_percent)
        self.gridLayout_3.addWidget(self.frame_percentage, 1, 0, 1, 1)
        self.frame_slider = QtWidgets.QFrame(self.frame_cloud_coverage)
        self.frame_slider.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_slider.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_slider.setObjectName("frame_slider")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_slider)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.slider_cloud_coverage = QtWidgets.QSlider(self.frame_slider)
        self.slider_cloud_coverage.setMinimumSize(QtCore.QSize(0, 35))
        self.slider_cloud_coverage.setMaximumSize(QtCore.QSize(16777215, 35))
        self.slider_cloud_coverage.setMaximum(100)
        self.slider_cloud_coverage.setSingleStep(25)
        self.slider_cloud_coverage.setPageStep(25)
        self.slider_cloud_coverage.setOrientation(QtCore.Qt.Horizontal)
        self.slider_cloud_coverage.setInvertedAppearance(False)
        self.slider_cloud_coverage.setInvertedControls(False)
        self.slider_cloud_coverage.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider_cloud_coverage.setObjectName("slider_cloud_coverage")
        self.horizontalLayout.addWidget(self.slider_cloud_coverage)
        self.gridLayout_3.addWidget(self.frame_slider, 0, 0, 1, 1)
        self.horizontalLayout_3.addWidget(self.frame_cloud_coverage)
        spacerItem1 = QtWidgets.QSpacerItem(71, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.gridLayout_8.addWidget(self.frame_6, 2, 1, 1, 2)
        self.lbl_cloud_coverage = QtWidgets.QLabel(self.frame_2)
        self.lbl_cloud_coverage.setMinimumSize(QtCore.QSize(260, 0))
        self.lbl_cloud_coverage.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lbl_cloud_coverage.setObjectName("lbl_cloud_coverage")
        self.gridLayout_8.addWidget(self.lbl_cloud_coverage, 2, 0, 1, 1)
        self.txt_default_back_days = QtWidgets.QLineEdit(self.frame_2)
        self.txt_default_back_days.setMinimumSize(QtCore.QSize(100, 30))
        self.txt_default_back_days.setMaximumSize(QtCore.QSize(100, 30))
        self.txt_default_back_days.setMaxLength(3)
        self.txt_default_back_days.setObjectName("txt_default_back_days")
        self.gridLayout_8.addWidget(self.txt_default_back_days, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout_8.addWidget(self.label_2, 4, 0, 1, 1)
        self.lbl_language = QtWidgets.QLabel(self.frame_2)
        self.lbl_language.setMinimumSize(QtCore.QSize(150, 0))
        self.lbl_language.setMaximumSize(QtCore.QSize(150, 16777215))
        self.lbl_language.setObjectName("lbl_language")
        self.gridLayout_8.addWidget(self.lbl_language, 0, 0, 1, 1)
        self.cbo_language = QtWidgets.QComboBox(self.frame_2)
        self.cbo_language.setMinimumSize(QtCore.QSize(200, 30))
        self.cbo_language.setMaximumSize(QtCore.QSize(200, 30))
        self.cbo_language.setObjectName("cbo_language")
        self.gridLayout_8.addWidget(self.cbo_language, 0, 1, 1, 1)
        self.txt_download_path = QtWidgets.QLineEdit(self.frame_2)
        self.txt_download_path.setMinimumSize(QtCore.QSize(0, 30))
        self.txt_download_path.setMaximumSize(QtCore.QSize(16777215, 30))
        self.txt_download_path.setMaxLength(1024)
        self.txt_download_path.setObjectName("txt_download_path")
        self.gridLayout_8.addWidget(self.txt_download_path, 3, 1, 1, 1)
        self.lbl_days_after = QtWidgets.QLabel(self.frame_2)
        self.lbl_days_after.setMinimumSize(QtCore.QSize(0, 0))
        self.lbl_days_after.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lbl_days_after.setObjectName("lbl_days_after")
        self.gridLayout_8.addWidget(self.lbl_days_after, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout_8.addWidget(self.label_3, 5, 0, 1, 1)
        self.txt_max_features_results = QtWidgets.QLineEdit(self.frame_2)
        self.txt_max_features_results.setMinimumSize(QtCore.QSize(100, 30))
        self.txt_max_features_results.setMaximumSize(QtCore.QSize(100, 30))
        self.txt_max_features_results.setMaxLength(3)
        self.txt_max_features_results.setObjectName("txt_max_features_results")
        self.gridLayout_8.addWidget(self.txt_max_features_results, 5, 1, 1, 1)
        self.txt_max_catalog_results = QtWidgets.QLineEdit(self.frame_2)
        self.txt_max_catalog_results.setMinimumSize(QtCore.QSize(100, 30))
        self.txt_max_catalog_results.setMaximumSize(QtCore.QSize(100, 30))
        self.txt_max_catalog_results.setMaxLength(3)
        self.txt_max_catalog_results.setObjectName("txt_max_catalog_results")
        self.gridLayout_8.addWidget(self.txt_max_catalog_results, 4, 1, 1, 1)
        self.verticalLayout.addWidget(self.frame_2)
        self.tabWidget = QtWidgets.QTabWidget(self.frame_content)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_up42 = QtWidgets.QWidget()
        self.tab_up42.setObjectName("tab_up42")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_up42)
        self.gridLayout_6.setObjectName("gridLayout_6")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem2, 2, 0, 1, 1)
        self.frame_up42_credentials = QtWidgets.QFrame(self.tab_up42)
        self.frame_up42_credentials.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_up42_credentials.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_up42_credentials.setObjectName("frame_up42_credentials")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_up42_credentials)
        self.gridLayout_7.setVerticalSpacing(10)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.lbl_up42_project_id = QtWidgets.QLabel(self.frame_up42_credentials)
        self.lbl_up42_project_id.setObjectName("lbl_up42_project_id")
        self.gridLayout_7.addWidget(self.lbl_up42_project_id, 0, 0, 1, 1)
        self.txt_up42_project_id = QtWidgets.QLineEdit(self.frame_up42_credentials)
        self.txt_up42_project_id.setMinimumSize(QtCore.QSize(0, 30))
        self.txt_up42_project_id.setMaximumSize(QtCore.QSize(16777215, 30))
        self.txt_up42_project_id.setMaxLength(512)
        self.txt_up42_project_id.setObjectName("txt_up42_project_id")
        self.gridLayout_7.addWidget(self.txt_up42_project_id, 0, 1, 1, 1)
        self.lbl_up42_api_key = QtWidgets.QLabel(self.frame_up42_credentials)
        self.lbl_up42_api_key.setObjectName("lbl_up42_api_key")
        self.gridLayout_7.addWidget(self.lbl_up42_api_key, 1, 0, 1, 1)
        self.txt_up42_api_key = QtWidgets.QLineEdit(self.frame_up42_credentials)
        self.txt_up42_api_key.setMinimumSize(QtCore.QSize(0, 30))
        self.txt_up42_api_key.setMaximumSize(QtCore.QSize(16777215, 30))
        self.txt_up42_api_key.setMaxLength(512)
        self.txt_up42_api_key.setObjectName("txt_up42_api_key")
        self.gridLayout_7.addWidget(self.txt_up42_api_key, 1, 1, 1, 1)
        self.gridLayout_6.addWidget(self.frame_up42_credentials, 0, 0, 1, 1)
        self.frame_up42_check_credentials = QtWidgets.QFrame(self.tab_up42)
        self.frame_up42_check_credentials.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_up42_check_credentials.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_up42_check_credentials.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_up42_check_credentials.setObjectName("frame_up42_check_credentials")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.frame_up42_check_credentials)
        self.gridLayout_9.setContentsMargins(-1, 6, 6, 6)
        self.gridLayout_9.setHorizontalSpacing(6)
        self.gridLayout_9.setVerticalSpacing(10)
        self.gridLayout_9.setObjectName("gridLayout_9")
        spacerItem3 = QtWidgets.QSpacerItem(195, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem3, 1, 0, 1, 1)
        self.btn_up42_check_credentials = QtWidgets.QPushButton(self.frame_up42_check_credentials)
        self.btn_up42_check_credentials.setMinimumSize(QtCore.QSize(200, 30))
        self.btn_up42_check_credentials.setMaximumSize(QtCore.QSize(200, 30))
        self.btn_up42_check_credentials.setObjectName("btn_up42_check_credentials")
        self.gridLayout_9.addWidget(self.btn_up42_check_credentials, 1, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(194, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem4, 1, 2, 1, 1)
        self.lbl_up42_check_credentials = QtWidgets.QLabel(self.frame_up42_check_credentials)
        self.lbl_up42_check_credentials.setText("TextLabel")
        self.lbl_up42_check_credentials.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_up42_check_credentials.setObjectName("lbl_up42_check_credentials")
        self.gridLayout_9.addWidget(self.lbl_up42_check_credentials, 0, 0, 1, 3)
        self.gridLayout_6.addWidget(self.frame_up42_check_credentials, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_up42, "Up42")
        self.tab_sentinel = QtWidgets.QWidget()
        self.tab_sentinel.setObjectName("tab_sentinel")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_sentinel)
        self.gridLayout_5.setObjectName("gridLayout_5")
        spacerItem5 = QtWidgets.QSpacerItem(20, 56, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem5, 2, 0, 1, 1)
        self.frame_sentinelhub_check_credentials = QtWidgets.QFrame(self.tab_sentinel)
        self.frame_sentinelhub_check_credentials.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_sentinelhub_check_credentials.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_sentinelhub_check_credentials.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_sentinelhub_check_credentials.setObjectName("frame_sentinelhub_check_credentials")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.frame_sentinelhub_check_credentials)
        self.gridLayout_11.setContentsMargins(-1, 6, 6, 6)
        self.gridLayout_11.setHorizontalSpacing(6)
        self.gridLayout_11.setVerticalSpacing(10)
        self.gridLayout_11.setObjectName("gridLayout_11")
        spacerItem6 = QtWidgets.QSpacerItem(194, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_11.addItem(spacerItem6, 2, 2, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(195, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_11.addItem(spacerItem7, 2, 0, 1, 1)
        self.btn_sentinelhub_check_credentials = QtWidgets.QPushButton(self.frame_sentinelhub_check_credentials)
        self.btn_sentinelhub_check_credentials.setMinimumSize(QtCore.QSize(200, 30))
        self.btn_sentinelhub_check_credentials.setMaximumSize(QtCore.QSize(200, 30))
        self.btn_sentinelhub_check_credentials.setObjectName("btn_sentinelhub_check_credentials")
        self.gridLayout_11.addWidget(self.btn_sentinelhub_check_credentials, 2, 1, 1, 1)
        self.lbl_sentinelhub_check_credentials = QtWidgets.QLabel(self.frame_sentinelhub_check_credentials)
        self.lbl_sentinelhub_check_credentials.setText("TextLabel")
        self.lbl_sentinelhub_check_credentials.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_sentinelhub_check_credentials.setObjectName("lbl_sentinelhub_check_credentials")
        self.gridLayout_11.addWidget(self.lbl_sentinelhub_check_credentials, 1, 0, 1, 3)
        self.gridLayout_5.addWidget(self.frame_sentinelhub_check_credentials, 1, 0, 1, 1)
        self.frame_sentinelhub_credentials = QtWidgets.QFrame(self.tab_sentinel)
        self.frame_sentinelhub_credentials.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_sentinelhub_credentials.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_sentinelhub_credentials.setObjectName("frame_sentinelhub_credentials")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.frame_sentinelhub_credentials)
        self.gridLayout_10.setVerticalSpacing(10)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.lbl_sentinelhub_client_id = QtWidgets.QLabel(self.frame_sentinelhub_credentials)
        self.lbl_sentinelhub_client_id.setObjectName("lbl_sentinelhub_client_id")
        self.gridLayout_10.addWidget(self.lbl_sentinelhub_client_id, 0, 0, 1, 1)
        self.txt_sentinelhub_client_id = QtWidgets.QLineEdit(self.frame_sentinelhub_credentials)
        self.txt_sentinelhub_client_id.setMinimumSize(QtCore.QSize(0, 30))
        self.txt_sentinelhub_client_id.setMaximumSize(QtCore.QSize(16777215, 30))
        self.txt_sentinelhub_client_id.setMaxLength(512)
        self.txt_sentinelhub_client_id.setObjectName("txt_sentinelhub_client_id")
        self.gridLayout_10.addWidget(self.txt_sentinelhub_client_id, 0, 1, 1, 1)
        self.lbl_sentinelhub_client_secret = QtWidgets.QLabel(self.frame_sentinelhub_credentials)
        self.lbl_sentinelhub_client_secret.setObjectName("lbl_sentinelhub_client_secret")
        self.gridLayout_10.addWidget(self.lbl_sentinelhub_client_secret, 1, 0, 1, 1)
        self.txt_sentinelhub_client_secret = QtWidgets.QLineEdit(self.frame_sentinelhub_credentials)
        self.txt_sentinelhub_client_secret.setMinimumSize(QtCore.QSize(0, 30))
        self.txt_sentinelhub_client_secret.setMaximumSize(QtCore.QSize(16777215, 30))
        self.txt_sentinelhub_client_secret.setMaxLength(512)
        self.txt_sentinelhub_client_secret.setObjectName("txt_sentinelhub_client_secret")
        self.gridLayout_10.addWidget(self.txt_sentinelhub_client_secret, 1, 1, 1, 1)
        self.gridLayout_5.addWidget(self.frame_sentinelhub_credentials, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_sentinel, "SentinelHub")
        self.tab_planet = QtWidgets.QWidget()
        self.tab_planet.setObjectName("tab_planet")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_planet)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_3 = QtWidgets.QFrame(self.tab_planet)
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QtWidgets.QLabel(self.frame_3)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_3, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_planet, "Planet")
        self.verticalLayout.addWidget(self.tabWidget)
        self.verticalLayout_2.addWidget(self.frame_content)

        self.retranslateUi(frm_settings)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(frm_settings)
        frm_settings.setTabOrder(self.cbo_language, self.txt_default_back_days)
        frm_settings.setTabOrder(self.txt_default_back_days, self.tabWidget)
        frm_settings.setTabOrder(self.tabWidget, self.txt_up42_project_id)
        frm_settings.setTabOrder(self.txt_up42_project_id, self.txt_up42_api_key)

    def retranslateUi(self, frm_settings):
        _translate = QtCore.QCoreApplication.translate
        frm_settings.setWindowTitle(_translate("frm_settings", "Settings"))
        self.label.setText(_translate("frm_settings", "Download path"))
        self.lbl_cloud_coverage.setText(_translate("frm_settings", "Default max cloud coverage"))
        self.label_2.setText(_translate("frm_settings", "Max catalogs"))
        self.lbl_language.setText(_translate("frm_settings", "Language"))
        self.lbl_days_after.setText(_translate("frm_settings", "Number of days in search range"))
        self.label_3.setText(_translate("frm_settings", "Max catalog features"))
        self.lbl_up42_project_id.setText(_translate("frm_settings", "Project ID"))
        self.lbl_up42_api_key.setText(_translate("frm_settings", "Api ID"))
        self.btn_up42_check_credentials.setText(_translate("frm_settings", "Check credentials"))
        self.btn_sentinelhub_check_credentials.setText(_translate("frm_settings", "Check credentials"))
        self.lbl_sentinelhub_client_id.setText(_translate("frm_settings", "Client ID"))
        self.lbl_sentinelhub_client_secret.setText(_translate("frm_settings", "Client secret"))
        self.label_5.setText(_translate("frm_settings", "Coming soon..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    frm_settings = QtWidgets.QWidget()
    ui = Ui_frm_settings()
    ui.setupUi(frm_settings)
    frm_settings.show()
    sys.exit(app.exec_())
