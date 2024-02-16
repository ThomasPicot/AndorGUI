# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowytkmMC.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from pyqtgraph import PlotWidget
from pyqtgraph import GraphicsLayoutWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 920)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(u"QMainWindow{\n"
"background-color:rgb(67, 67, 67);\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(1200, 920))
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget_Vcut = PlotWidget(self.centralwidget)
        self.widget_Vcut.setObjectName(u"widget_Vcut")
        self.widget_Vcut.setMinimumSize(QSize(45, 540))
        self.widget_Vcut.setMaximumSize(QSize(45, 16777215))

        self.gridLayout.addWidget(self.widget_Vcut, 0, 1, 1, 1)

        self.pushButton_normalisation = QPushButton(self.centralwidget)
        self.pushButton_normalisation.setObjectName(u"pushButton_normalisation")

        self.gridLayout.addWidget(self.pushButton_normalisation, 2, 1, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_external_trig = QLabel(self.centralwidget)
        self.label_external_trig.setObjectName(u"label_external_trig")
        self.label_external_trig.setStyleSheet(u"QLabel{color:#ffffff;}")

        self.horizontalLayout_2.addWidget(self.label_external_trig)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.pushButton_start_ext = QPushButton(self.centralwidget)
        self.pushButton_start_ext.setObjectName(u"pushButton_start_ext")

        self.horizontalLayout_2.addWidget(self.pushButton_start_ext)

        self.pushButton_stop_ext = QPushButton(self.centralwidget)
        self.pushButton_stop_ext.setObjectName(u"pushButton_stop_ext")

        self.horizontalLayout_2.addWidget(self.pushButton_stop_ext)


        self.gridLayout.addLayout(self.horizontalLayout_2, 4, 0, 1, 1)

        self.widgetFrame = GraphicsLayoutWidget(self.centralwidget)
        self.widgetFrame.setObjectName(u"widgetFrame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widgetFrame.sizePolicy().hasHeightForWidth())
        self.widgetFrame.setSizePolicy(sizePolicy1)
        self.widgetFrame.setMinimumSize(QSize(540, 540))
        self.widgetFrame.setMaximumSize(QSize(19000, 19000))

        self.gridLayout.addWidget(self.widgetFrame, 0, 0, 1, 1)

        self.widget_Hcut = PlotWidget(self.centralwidget)
        self.widget_Hcut.setObjectName(u"widget_Hcut")
        self.widget_Hcut.setMinimumSize(QSize(540, 45))
        self.widget_Hcut.setMaximumSize(QSize(16777215, 45))

        self.gridLayout.addWidget(self.widget_Hcut, 1, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"QLabel{color:#ffffff;}")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.pushButton_start_acq = QPushButton(self.centralwidget)
        self.pushButton_start_acq.setObjectName(u"pushButton_start_acq")
        self.pushButton_start_acq.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.pushButton_start_acq)

        self.pushButton_stop_acq = QPushButton(self.centralwidget)
        self.pushButton_stop_acq.setObjectName(u"pushButton_stop_acq")
        self.pushButton_stop_acq.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.pushButton_stop_acq)


        self.gridLayout.addLayout(self.horizontalLayout_4, 2, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(45, 16777215))
        self.label.setStyleSheet(u"QLabel{color:#ffffff;}")

        self.horizontalLayout_3.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.doubleSpinBox_exposure = QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_exposure.setObjectName(u"doubleSpinBox_exposure")
        self.doubleSpinBox_exposure.setMaximumSize(QSize(125, 16777215))
        self.doubleSpinBox_exposure.setDecimals(5)
        self.doubleSpinBox_exposure.setMaximum(200.000000000000000)
        self.doubleSpinBox_exposure.setSingleStep(0.100000000000000)
        self.doubleSpinBox_exposure.setValue(100.000000000000000)

        self.horizontalLayout_3.addWidget(self.doubleSpinBox_exposure)

        self.pushButtonArm = QPushButton(self.centralwidget)
        self.pushButtonArm.setObjectName(u"pushButtonArm")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButtonArm.sizePolicy().hasHeightForWidth())
        self.pushButtonArm.setSizePolicy(sizePolicy2)
        self.pushButtonArm.setMaximumSize(QSize(16777215, 25))
        self.pushButtonArm.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.pushButtonArm)

        self.pushButton_disarm = QPushButton(self.centralwidget)
        self.pushButton_disarm.setObjectName(u"pushButton_disarm")
        sizePolicy2.setHeightForWidth(self.pushButton_disarm.sizePolicy().hasHeightForWidth())
        self.pushButton_disarm.setSizePolicy(sizePolicy2)
        self.pushButton_disarm.setMaximumSize(QSize(16777215, 25))
        self.pushButton_disarm.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.pushButton_disarm)


        self.gridLayout.addLayout(self.horizontalLayout_3, 3, 0, 1, 1)

        self.pushButton_shot = QPushButton(self.centralwidget)
        self.pushButton_shot.setObjectName(u"pushButton_shot")
        self.pushButton_shot.setStyleSheet(u"")

        self.gridLayout.addWidget(self.pushButton_shot, 1, 1, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_ROI = QLabel(self.centralwidget)
        self.label_ROI.setObjectName(u"label_ROI")
        self.label_ROI.setStyleSheet(u"QLabel{color:white;}")

        self.horizontalLayout_5.addWidget(self.label_ROI)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.pushButton_setROI = QPushButton(self.centralwidget)
        self.pushButton_setROI.setObjectName(u"pushButton_setROI")

        self.horizontalLayout_5.addWidget(self.pushButton_setROI)

        self.pushButton_apply_ROI = QPushButton(self.centralwidget)
        self.pushButton_apply_ROI.setObjectName(u"pushButton_apply_ROI")

        self.horizontalLayout_5.addWidget(self.pushButton_apply_ROI)

        self.pushButton_clear_ROI = QPushButton(self.centralwidget)
        self.pushButton_clear_ROI.setObjectName(u"pushButton_clear_ROI")

        self.horizontalLayout_5.addWidget(self.pushButton_clear_ROI)


        self.gridLayout.addLayout(self.horizontalLayout_5, 5, 0, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widgetBinningFrame = GraphicsLayoutWidget(self.centralwidget)
        self.widgetBinningFrame.setObjectName(u"widgetBinningFrame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.widgetBinningFrame.sizePolicy().hasHeightForWidth())
        self.widgetBinningFrame.setSizePolicy(sizePolicy3)
        self.widgetBinningFrame.setMinimumSize(QSize(540, 540))
        self.widgetBinningFrame.setMaximumSize(QSize(19000, 19000))

        self.verticalLayout_2.addWidget(self.widgetBinningFrame)

        self.textBrowserLogs = QTextBrowser(self.centralwidget)
        self.textBrowserLogs.setObjectName(u"textBrowserLogs")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.textBrowserLogs.sizePolicy().hasHeightForWidth())
        self.textBrowserLogs.setSizePolicy(sizePolicy4)
        self.textBrowserLogs.setMaximumSize(QSize(16777215, 240))
        self.textBrowserLogs.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.textBrowserLogs)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_normalisation.setText(QCoreApplication.translate("MainWindow", u"Normalisation", None))
        self.label_external_trig.setText(QCoreApplication.translate("MainWindow", u"External trigger mode :", None))
        self.pushButton_start_ext.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.pushButton_stop_ext.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Acquisition", None))
        self.pushButton_start_acq.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.pushButton_stop_acq.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Exposure: ", None))
        self.pushButtonArm.setText(QCoreApplication.translate("MainWindow", u"Arm", None))
        self.pushButton_disarm.setText(QCoreApplication.translate("MainWindow", u"Disarm", None))
        self.pushButton_shot.setText(QCoreApplication.translate("MainWindow", u"Shot", None))
        self.label_ROI.setText(QCoreApplication.translate("MainWindow", u"Camera ROI : ", None))
        self.pushButton_setROI.setText(QCoreApplication.translate("MainWindow", u"Set ROI", None))
        self.pushButton_apply_ROI.setText(QCoreApplication.translate("MainWindow", u"Apply ROI", None))
        self.pushButton_clear_ROI.setText(QCoreApplication.translate("MainWindow", u"Clear ROI", None))
    # retranslateUi

