# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowajiWuy.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from pyqtgraph import GraphicsLayoutWidget
from pyqtgraph import PlotWidget


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
"font: 75 13pt \"Times New Roman\";\n"
"background-color:rgb(67, 67, 67);\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(1200, 920))
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"QLabel {\n"
"    color: rgb(255, 255, 255); /* Couleur du texte (blanc) */\n"
"    font-family: Arial, sans-serif; /* Police de caract\u00e8res */\n"
"    font-size: 16px; /* Taille de la police */\n"
"    font-weight: bold; /* Gras */\n"
"    padding: 5px; /* Marge int\u00e9rieure */\n"
"}\n"
"\n"
"#customLabel {\n"
"    background-color: rgb(40, 40, 40); /* Couleur de fond */\n"
"    border-radius: 5px; /* Coins arrondis */\n"
"    padding: 10px; /* Marge int\u00e9rieure */\n"
"}\n"
"")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.pushButton_start_acq = QPushButton(self.centralwidget)
        self.pushButton_start_acq.setObjectName(u"pushButton_start_acq")
        self.pushButton_start_acq.setStyleSheet(u"QPushButton {\n"
"	\n"
"	font: 75 14pt \"Arial\";\n"
"    background-color: rgb(40, 40, 40);  /* Nouvelle couleur de fond (gris fonc\u00e9) */\n"
"    color: white;  /* Couleur du texte */\n"
"    border: 1px solid rgb(100, 100, 100);  /* Bordure */\n"
"    border-radius: 9px;  /* Coins arrondis */\n"
"    padding: 5px 20px;  /* Marge int\u00e9rieure */\n"
"    min-height: 20px;  /* Hauteur minimale */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(50, 50, 50);  /* Nouvelle couleur de fond au survol (gris l\u00e9g\u00e8rement plus clair) */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(30, 30, 30);  /* Nouvelle couleur de fond lors du clic (gris plus fonc\u00e9) */\n"
"    border: 1px solid rgb(80, 80, 80);  /* Bordure au clic */\n"
"}\n"
"\n"
"")

        self.horizontalLayout_4.addWidget(self.pushButton_start_acq)

        self.pushButton_stop_acq = QPushButton(self.centralwidget)
        self.pushButton_stop_acq.setObjectName(u"pushButton_stop_acq")
        self.pushButton_stop_acq.setStyleSheet(u"QPushButton {\n"
"	font: 14pt \"Arial\";\n"
"    background-color: rgb(40, 40, 40);  /* Nouvelle couleur de fond (gris fonc\u00e9) */\n"
"    color: white;  /* Couleur du texte */\n"
"    border: 1px solid rgb(100, 100, 100);  /* Bordure */\n"
"    border-radius: 9px;  /* Coins arrondis */\n"
"    padding: 5px 20px;  /* Marge int\u00e9rieure */\n"
"    min-height: 20px;  /* Hauteur minimale */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(50, 50, 50);  /* Nouvelle couleur de fond au survol (gris l\u00e9g\u00e8rement plus clair) */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(30, 30, 30);  /* Nouvelle couleur de fond lors du clic (gris plus fonc\u00e9) */\n"
"    border: 1px solid rgb(80, 80, 80);  /* Bordure au clic */\n"
"}\n"
"\n"
"")

        self.horizontalLayout_4.addWidget(self.pushButton_stop_acq)


        self.gridLayout.addLayout(self.horizontalLayout_4, 3, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMaximumSize(QSize(92, 16777215))
        self.label.setStyleSheet(u"QLabel {\n"
"    color: rgb(255, 255, 255); /* Couleur du texte (blanc) */\n"
"    font-family: Arial, sans-serif; /* Police de caract\u00e8res */\n"
"    font-size: 16px; /* Taille de la police */\n"
"    font-weight: bold; /* Gras */\n"
"    padding: 5px; /* Marge int\u00e9rieure */\n"
"}\n"
"\n"
"#customLabel {\n"
"    background-color: rgb(40, 40, 40); /* Couleur de fond */\n"
"    border-radius: 5px; /* Coins arrondis */\n"
"    padding: 10px; /* Marge int\u00e9rieure */\n"
"}\n"
"")

        self.horizontalLayout_3.addWidget(self.label)

        self.doubleSpinBox_exposure = QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_exposure.setObjectName(u"doubleSpinBox_exposure")
        self.doubleSpinBox_exposure.setMaximumSize(QSize(125, 16777215))
        self.doubleSpinBox_exposure.setStyleSheet(u"QDoubleSpinBox {\n"
"	font: 14pt \"Arial\";\n"
"    background-color: rgb(30, 50, 70);  /* Couleur de fond (bleu fonc\u00e9) */\n"
"    color: white;  /* Couleur du texte */\n"
"    border: 1px solid rgb(70, 100, 120);  /* Bordure */\n"
"    border-radius: 5px;  /* Coins arrondis */\n"
"    padding: 3px 5px;  /* Marge int\u00e9rieure */\n"
"    min-height: 20px;  /* Hauteur minimale */\n"
"}\n"
"\n"
"QDoubleSpinBox::up-button, QDoubleSpinBox::down-button {\n"
"    background-color: rgb(40, 60, 80);  /* Couleur de fond des boutons */\n"
"    color: white;  /* Couleur du texte */\n"
"    border: 1px solid rgb(70, 100, 120);  /* Bordure */\n"
"    border-radius: 5px;  /* Coins arrondis */\n"
"    width: 10px;  /* Largeur des boutons */\n"
"    height: 10px;  /* Hauteur des boutons */\n"
"}\n"
"\n"
"QDoubleSpinBox::up-button:hover, QDoubleSpinBox::down-button:hover {\n"
"    background-color: rgb(50, 70, 90);  /* Couleur de fond des boutons au survol */\n"
"}\n"
"")
        self.doubleSpinBox_exposure.setDecimals(5)
        self.doubleSpinBox_exposure.setMaximum(200.000000000000000)
        self.doubleSpinBox_exposure.setSingleStep(0.100000000000000)
        self.doubleSpinBox_exposure.setValue(20.000000000000000)

        self.horizontalLayout_3.addWidget(self.doubleSpinBox_exposure)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.pushButtonArm = QPushButton(self.centralwidget)
        self.pushButtonArm.setObjectName(u"pushButtonArm")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButtonArm.sizePolicy().hasHeightForWidth())
        self.pushButtonArm.setSizePolicy(sizePolicy2)
        self.pushButtonArm.setMaximumSize(QSize(16777215, 25))
        self.pushButtonArm.setStyleSheet(u"QPushButton {\n"
"	font: 14pt \"Arial\";\n"
"    background-color: rgb(40, 40, 40);  /* Nouvelle couleur de fond (gris fonc\u00e9) */\n"
"    color: white;  /* Couleur du texte */\n"
"    border: 1px solid rgb(100, 100, 100);  /* Bordure */\n"
"    border-radius: 9px;  /* Coins arrondis */\n"
"    padding: 5px 20px;  /* Marge int\u00e9rieure */\n"
"    min-height: 20px;  /* Hauteur minimale */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(50, 50, 50);  /* Nouvelle couleur de fond au survol (gris l\u00e9g\u00e8rement plus clair) */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(30, 30, 30);  /* Nouvelle couleur de fond lors du clic (gris plus fonc\u00e9) */\n"
"    border: 1px solid rgb(80, 80, 80);  /* Bordure au clic */\n"
"}\n"
"\n"
"")

        self.horizontalLayout_3.addWidget(self.pushButtonArm)

        self.pushButton_disarm = QPushButton(self.centralwidget)
        self.pushButton_disarm.setObjectName(u"pushButton_disarm")
        self.pushButton_disarm.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pushButton_disarm.sizePolicy().hasHeightForWidth())
        self.pushButton_disarm.setSizePolicy(sizePolicy3)
        self.pushButton_disarm.setMinimumSize(QSize(0, 32))
        self.pushButton_disarm.setMaximumSize(QSize(16777215, 25))
        self.pushButton_disarm.setStyleSheet(u"QPushButton {\n"
"	font: 14pt \"Arial\";\n"
"    background-color: rgb(40, 40, 40);  /* Nouvelle couleur de fond (gris fonc\u00e9) */\n"
"    color: white;  /* Couleur du texte */\n"
"    border: 1px solid rgb(100, 100, 100);  /* Bordure */\n"
"    border-radius: 9px;  /* Coins arrondis */\n"
"    padding: 5px 20px;  /* Marge int\u00e9rieure */\n"
"    min-height: 20px;  /* Hauteur minimale */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(50, 50, 50);  /* Nouvelle couleur de fond au survol (gris l\u00e9g\u00e8rement plus clair) */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(30, 30, 30);  /* Nouvelle couleur de fond lors du clic (gris plus fonc\u00e9) */\n"
"    border: 1px solid rgb(80, 80, 80);  /* Bordure au clic */\n"
"}\n"
"\n"
"")

        self.horizontalLayout_3.addWidget(self.pushButton_disarm)


        self.gridLayout.addLayout(self.horizontalLayout_3, 4, 0, 1, 1)

        self.pushButton_clear_crosshair = QPushButton(self.centralwidget)
        self.pushButton_clear_crosshair.setObjectName(u"pushButton_clear_crosshair")
        self.pushButton_clear_crosshair.setStyleSheet(u"QPushButton {\n"
"	font: 14pt \"Arial\";\n"
"    background-color: rgb(40, 40, 40);  /* Nouvelle couleur de fond (gris fonc\u00e9) */\n"
"    color: white;  /* Couleur du texte */\n"
"    border: 1px solid rgb(100, 100, 100);  /* Bordure */\n"
"    border-radius: 9px;  /* Coins arrondis */\n"
"    padding: 5px 20px;  /* Marge int\u00e9rieure */\n"
"    min-height: 20px;  /* Hauteur minimale */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(50, 50, 50);  /* Nouvelle couleur de fond au survol (gris l\u00e9g\u00e8rement plus clair) */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(30, 30, 30);  /* Nouvelle couleur de fond lors du clic (gris plus fonc\u00e9) */\n"
"    border: 1px solid rgb(80, 80, 80);  /* Bordure au clic */\n"
"}\n"
"\n"
"")

        self.gridLayout.addWidget(self.pushButton_clear_crosshair, 3, 1, 1, 1)

        self.widget_Hcut = PlotWidget(self.centralwidget)
        self.widget_Hcut.setObjectName(u"widget_Hcut")
        self.widget_Hcut.setMinimumSize(QSize(0, 60))
        self.widget_Hcut.setMaximumSize(QSize(16777215, 60))

        self.gridLayout.addWidget(self.widget_Hcut, 2, 0, 1, 2)

        self.pushButton_normalisation = QPushButton(self.centralwidget)
        self.pushButton_normalisation.setObjectName(u"pushButton_normalisation")
        self.pushButton_normalisation.setStyleSheet(u"QPushButton {\n"
"	font: 14pt \"Arial\";\n"
"    background-color: rgb(40, 40, 40);  /* Nouvelle couleur de fond (gris fonc\u00e9) */\n"
"    color: white;  /* Couleur du texte */\n"
"    border: 1px solid rgb(100, 100, 100);  /* Bordure */\n"
"    border-radius: 9px;  /* Coins arrondis */\n"
"    padding: 5px 20px;  /* Marge int\u00e9rieure */\n"
"    min-height: 20px;  /* Hauteur minimale */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(50, 50, 50);  /* Nouvelle couleur de fond au survol (gris l\u00e9g\u00e8rement plus clair) */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(30, 30, 30);  /* Nouvelle couleur de fond lors du clic (gris plus fonc\u00e9) */\n"
"    border: 1px solid rgb(80, 80, 80);  /* Bordure au clic */\n"
"}\n"
"\n"
"")

        self.gridLayout.addWidget(self.pushButton_normalisation, 5, 1, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_ROI = QLabel(self.centralwidget)
        self.label_ROI.setObjectName(u"label_ROI")
        self.label_ROI.setStyleSheet(u"QLabel {\n"
"    color: rgb(255, 255, 255); /* Couleur du texte (blanc) */\n"
"    font-family: Arial, sans-serif; /* Police de caract\u00e8res */\n"
"    font-size: 16px; /* Taille de la police */\n"
"    font-weight: bold; /* Gras */\n"
"    padding: 5px; /* Marge int\u00e9rieure */\n"
"}\n"
"\n"
"#customLabel {\n"
"    background-color: rgb(40, 40, 40); /* Couleur de fond */\n"
"    border-radius: 5px; /* Coins arrondis */\n"
"    padding: 10px; /* Marge int\u00e9rieure */\n"
"}\n"
"")

        self.horizontalLayout_5.addWidget(self.label_ROI)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.pushButton_setROI = QPushButton(self.centralwidget)
        self.pushButton_setROI.setObjectName(u"pushButton_setROI")
        self.pushButton_setROI.setStyleSheet(u"QPushButton {\n"
"	font: 14pt \"Arial\";\n"
"    background-color: rgb(40, 40, 40);  /* Nouvelle couleur de fond (gris fonc\u00e9) */\n"
"    color: white;  /* Couleur du texte */\n"
"    border: 1px solid rgb(100, 100, 100);  /* Bordure */\n"
"    border-radius: 9px;  /* Coins arrondis */\n"
"    padding: 5px 20px;  /* Marge int\u00e9rieure */\n"
"    min-height: 20px;  /* Hauteur minimale */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(50, 50, 50);  /* Nouvelle couleur de fond au survol (gris l\u00e9g\u00e8rement plus clair) */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(30, 30, 30);  /* Nouvelle couleur de fond lors du clic (gris plus fonc\u00e9) */\n"
"    border: 1px solid rgb(80, 80, 80);  /* Bordure au clic */\n"
"}\n"
"\n"
"")

        self.horizontalLayout_5.addWidget(self.pushButton_setROI)

        self.pushButton_apply_ROI = QPushButton(self.centralwidget)
        self.pushButton_apply_ROI.setObjectName(u"pushButton_apply_ROI")
        self.pushButton_apply_ROI.setStyleSheet(u"QPushButton {\n"
"	font: 14pt \"Arial\";\n"
"    background-color: rgb(40, 40, 40);  /* Nouvelle couleur de fond (gris fonc\u00e9) */\n"
"    color: white;  /* Couleur du texte */\n"
"    border: 1px solid rgb(100, 100, 100);  /* Bordure */\n"
"    border-radius: 9px;  /* Coins arrondis */\n"
"    padding: 5px 20px;  /* Marge int\u00e9rieure */\n"
"    min-height: 20px;  /* Hauteur minimale */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(50, 50, 50);  /* Nouvelle couleur de fond au survol (gris l\u00e9g\u00e8rement plus clair) */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(30, 30, 30);  /* Nouvelle couleur de fond lors du clic (gris plus fonc\u00e9) */\n"
"    border: 1px solid rgb(80, 80, 80);  /* Bordure au clic */\n"
"}\n"
"\n"
"")

        self.horizontalLayout_5.addWidget(self.pushButton_apply_ROI)

        self.pushButton_clear_ROI = QPushButton(self.centralwidget)
        self.pushButton_clear_ROI.setObjectName(u"pushButton_clear_ROI")
        self.pushButton_clear_ROI.setStyleSheet(u"QPushButton {\n"
"	font: 14pt \"Arial\";\n"
"    background-color: rgb(40, 40, 40);  /* Nouvelle couleur de fond (gris fonc\u00e9) */\n"
"    color: white;  /* Couleur du texte */\n"
"    border: 1px solid rgb(100, 100, 100);  /* Bordure */\n"
"    border-radius: 9px;  /* Coins arrondis */\n"
"    padding: 5px 20px;  /* Marge int\u00e9rieure */\n"
"    min-height: 20px;  /* Hauteur minimale */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(50, 50, 50);  /* Nouvelle couleur de fond au survol (gris l\u00e9g\u00e8rement plus clair) */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(30, 30, 30);  /* Nouvelle couleur de fond lors du clic (gris plus fonc\u00e9) */\n"
"    border: 1px solid rgb(80, 80, 80);  /* Bordure au clic */\n"
"}\n"
"\n"
"")

        self.horizontalLayout_5.addWidget(self.pushButton_clear_ROI)


        self.gridLayout.addLayout(self.horizontalLayout_5, 6, 0, 1, 1)

        self.widgetFrame = GraphicsLayoutWidget(self.centralwidget)
        self.widgetFrame.setObjectName(u"widgetFrame")
        sizePolicy2.setHeightForWidth(self.widgetFrame.sizePolicy().hasHeightForWidth())
        self.widgetFrame.setSizePolicy(sizePolicy2)
        self.widgetFrame.setMinimumSize(QSize(540, 540))
        self.widgetFrame.setMaximumSize(QSize(19000, 19000))
        self.widgetFrame.setStyleSheet(u"")

        self.gridLayout.addWidget(self.widgetFrame, 0, 0, 2, 2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_external_trig = QLabel(self.centralwidget)
        self.label_external_trig.setObjectName(u"label_external_trig")
        self.label_external_trig.setStyleSheet(u"QLabel {\n"
"    color: rgb(255, 255, 255); /* Couleur du texte (blanc) */\n"
"    font-family: Arial, sans-serif; /* Police de caract\u00e8res */\n"
"    font-size: 16px; /* Taille de la police */\n"
"    font-weight: bold; /* Gras */\n"
"    padding: 5px; /* Marge int\u00e9rieure */\n"
"}\n"
"\n"
"#customLabel {\n"
"    background-color: rgb(40, 40, 40); /* Couleur de fond */\n"
"    border-radius: 5px; /* Coins arrondis */\n"
"    padding: 10px; /* Marge int\u00e9rieure */\n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.label_external_trig)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.pushButton_start_ext = QPushButton(self.centralwidget)
        self.pushButton_start_ext.setObjectName(u"pushButton_start_ext")
        self.pushButton_start_ext.setStyleSheet(u"QPushButton {\n"
"	font: 14pt \"Arial\";\n"
"    background-color: rgb(40, 40, 40);  /* Nouvelle couleur de fond (gris fonc\u00e9) */\n"
"    color: white;  /* Couleur du texte */\n"
"    border: 1px solid rgb(100, 100, 100);  /* Bordure */\n"
"    border-radius: 9px;  /* Coins arrondis */\n"
"    padding: 5px 20px;  /* Marge int\u00e9rieure */\n"
"    min-height: 20px;  /* Hauteur minimale */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(50, 50, 50);  /* Nouvelle couleur de fond au survol (gris l\u00e9g\u00e8rement plus clair) */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(30, 30, 30);  /* Nouvelle couleur de fond lors du clic (gris plus fonc\u00e9) */\n"
"    border: 1px solid rgb(80, 80, 80);  /* Bordure au clic */\n"
"}\n"
"\n"
"")

        self.horizontalLayout_2.addWidget(self.pushButton_start_ext)

        self.pushButton_stop_ext = QPushButton(self.centralwidget)
        self.pushButton_stop_ext.setObjectName(u"pushButton_stop_ext")
        self.pushButton_stop_ext.setStyleSheet(u"QPushButton {\n"
"	font: 14pt \"Arial\";\n"
"    background-color: rgb(40, 40, 40);  /* Nouvelle couleur de fond (gris fonc\u00e9) */\n"
"    color: white;  /* Couleur du texte */\n"
"    border: 1px solid rgb(100, 100, 100);  /* Bordure */\n"
"    border-radius: 9px;  /* Coins arrondis */\n"
"    padding: 5px 20px;  /* Marge int\u00e9rieure */\n"
"    min-height: 20px;  /* Hauteur minimale */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(50, 50, 50);  /* Nouvelle couleur de fond au survol (gris l\u00e9g\u00e8rement plus clair) */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(30, 30, 30);  /* Nouvelle couleur de fond lors du clic (gris plus fonc\u00e9) */\n"
"    border: 1px solid rgb(80, 80, 80);  /* Bordure au clic */\n"
"}\n"
"\n"
"")

        self.horizontalLayout_2.addWidget(self.pushButton_stop_ext)


        self.gridLayout.addLayout(self.horizontalLayout_2, 5, 0, 1, 1)

        self.widget_Vcut = PlotWidget(self.centralwidget)
        self.widget_Vcut.setObjectName(u"widget_Vcut")
        sizePolicy.setHeightForWidth(self.widget_Vcut.sizePolicy().hasHeightForWidth())
        self.widget_Vcut.setSizePolicy(sizePolicy)
        self.widget_Vcut.setMinimumSize(QSize(60, 0))
        self.widget_Vcut.setMaximumSize(QSize(60, 16777215))

        self.gridLayout.addWidget(self.widget_Vcut, 0, 2, 1, 1)

        self.pushButton_shot = QPushButton(self.centralwidget)
        self.pushButton_shot.setObjectName(u"pushButton_shot")
        self.pushButton_shot.setStyleSheet(u"QPushButton {\n"
"	font: 14pt \"Arial\";\n"
"    background-color: rgb(70, 30, 40);  /* Nouvelle couleur de fond (gris fonc\u00e9) */\n"
"    color: white;  /* Couleur du texte */\n"
"    border: 1px solid rgb(100, 100, 100);  /* Bordure */\n"
"    border-radius: 9px;  /* Coins arrondis */\n"
"    padding: 5px 20px;  /* Marge int\u00e9rieure */\n"
"    min-height: 20px;  /* Hauteur minimale */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(50, 50, 50);  /* Nouvelle couleur de fond au survol (gris l\u00e9g\u00e8rement plus clair) */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(30, 30, 30);  /* Nouvelle couleur de fond lors du clic (gris plus fonc\u00e9) */\n"
"    border: 1px solid rgb(80, 80, 80);  /* Bordure au clic */\n"
"}\n"
"\n"
"")

        self.gridLayout.addWidget(self.pushButton_shot, 4, 1, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widgetBinningFrame = GraphicsLayoutWidget(self.centralwidget)
        self.widgetBinningFrame.setObjectName(u"widgetBinningFrame")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.widgetBinningFrame.sizePolicy().hasHeightForWidth())
        self.widgetBinningFrame.setSizePolicy(sizePolicy4)
        self.widgetBinningFrame.setMinimumSize(QSize(540, 540))
        self.widgetBinningFrame.setMaximumSize(QSize(19000, 19000))

        self.verticalLayout_2.addWidget(self.widgetBinningFrame)

        self.textBrowserLogs = QTextBrowser(self.centralwidget)
        self.textBrowserLogs.setObjectName(u"textBrowserLogs")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.textBrowserLogs.sizePolicy().hasHeightForWidth())
        self.textBrowserLogs.setSizePolicy(sizePolicy5)
        self.textBrowserLogs.setMaximumSize(QSize(16777215, 240))
        self.textBrowserLogs.setStyleSheet(u"QTextBrowser {\n"
"    background-color: rgb(220, 225, 220);  /* Couleur de fond */\n"
"    color: rgb(50, 50, 50);  /* Couleur du texte */\n"
"    border: 1px solid rgb(200, 200, 200);  /* Bordure */\n"
"    border-radius: 5px;  /* Coins arrondis */\n"
"    padding: 10px;  /* Marge int\u00e9rieure */\n"
"    font-family: Arial, sans-serif;  /* Police de caract\u00e8res */\n"
"    font-size: 14px;  /* Taille de police */\n"
"}\n"
"\n"
"QTextBrowser:focus {\n"
"    border-color: rgb(0, 122, 204);  /* Couleur de la bordure lorsqu'il est en focus */\n"
"}\n"
"\n"
"QTextBrowser::placeholder {\n"
"    color: rgb(150, 150, 150);  /* Couleur du texte de l'espace r\u00e9serv\u00e9 */\n"
"}\n"
"\n"
"QTextBrowser:hover {\n"
"    background-color: rgb(245, 245, 245);  /* Couleur de fond au survol */\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.textBrowserLogs)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Andor GUI", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Acquisition", None))
        self.pushButton_start_acq.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.pushButton_stop_acq.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Exposure: ", None))
        self.pushButtonArm.setText(QCoreApplication.translate("MainWindow", u"Arm", None))
        self.pushButton_disarm.setText(QCoreApplication.translate("MainWindow", u"Disarm", None))
        self.pushButton_clear_crosshair.setText(QCoreApplication.translate("MainWindow", u"Clear crosshair", None))
        self.pushButton_normalisation.setText(QCoreApplication.translate("MainWindow", u"Normalisation", None))
        self.label_ROI.setText(QCoreApplication.translate("MainWindow", u"Camera ROI : ", None))
        self.pushButton_setROI.setText(QCoreApplication.translate("MainWindow", u"Set ROI", None))
        self.pushButton_apply_ROI.setText(QCoreApplication.translate("MainWindow", u"Apply ROI", None))
        self.pushButton_clear_ROI.setText(QCoreApplication.translate("MainWindow", u"Clear ROI", None))
        self.label_external_trig.setText(QCoreApplication.translate("MainWindow", u"External trigger mode :", None))
        self.pushButton_start_ext.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.pushButton_stop_ext.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.pushButton_shot.setText(QCoreApplication.translate("MainWindow", u"Shot", None))
    # retranslateUi

