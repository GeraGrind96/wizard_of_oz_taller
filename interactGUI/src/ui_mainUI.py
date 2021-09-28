# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainUI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_guiDlg(object):
    def setupUi(self, guiDlg):
        if not guiDlg.objectName():
            guiDlg.setObjectName(u"guiDlg")
        guiDlg.resize(1239, 857)
        self.drop_shadow_frame = QFrame(guiDlg)
        self.drop_shadow_frame.setObjectName(u"drop_shadow_frame")
        self.drop_shadow_frame.setGeometry(QRect(0, 0, 1238, 861))
        self.drop_shadow_frame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0.578947, y2:0.557, stop:0 rgba(215, 215, 215, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius:100px;\n"
"\n"
"")
        self.drop_shadow_frame.setFrameShape(QFrame.NoFrame)
        self.drop_shadow_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.drop_shadow_frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_3 = QFrame(self.drop_shadow_frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color:none;")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.stackedWidget = QStackedWidget(self.frame_3)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(20, 120, 1171, 591))
        self.stackedWidget.setStyleSheet(u"background-color:none;")
        self.stackedWidget.setFrameShadow(QFrame.Plain)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setStyleSheet(u"background-color:none;")
        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(470, 260, 201, 20))
        font = QFont()
        font.setFamily(u"Noto Color Emoji")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: qlineargradient(spread:pad, x1:0.0366492, y1:0.091, x2:0.283, y2:0.573864, stop:0 rgba(0, 116, 71, 255), stop:1 rgba(0, 166, 51, 255));")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.inicioconversacion = QPushButton(self.page)
        self.inicioconversacion.setObjectName(u"inicioconversacion")
        self.inicioconversacion.setGeometry(QRect(470, 510, 201, 41))
        self.inicioconversacion.setStyleSheet(u"QPushButton {\n"
"	background-color: qlineargradient(spread:pad, x1:0.163, y1:0.0911818, x2:0.762316, y2:0.676, stop:0 rgba(37, 185, 63, 255), stop:1 rgba(0, 166, 51, 255));\n"
"	color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(199, 199, 199, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	border: none;\n"
"	border-radius:20px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(199, 199, 199, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"")
        self.nombre_usuario = QLineEdit(self.page)
        self.nombre_usuario.setObjectName(u"nombre_usuario")
        self.nombre_usuario.setGeometry(QRect(450, 310, 241, 25))
        self.nombre_usuario.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(192, 192, 192, 255), stop:1 rgba(225, 225, 225, 255));\n"
"border: none;\n"
"border-radius:20px;")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setStyleSheet(u"")
        self.finconversacion = QPushButton(self.page_2)
        self.finconversacion.setObjectName(u"finconversacion")
        self.finconversacion.setGeometry(QRect(490, 490, 161, 81))
        self.finconversacion.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.07, y1:0.0454545, x2:1, y2:1, stop:0 rgba(108, 188, 154, 255), stop:1 rgba(235, 255, 185, 255));")
        self.textoaenviar = QLineEdit(self.page_2)
        self.textoaenviar.setObjectName(u"textoaenviar")
        self.textoaenviar.setGeometry(QRect(60, 90, 191, 91))
        self.textoaenviar.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(9, 41, 4, 255), stop:0.085 rgba(2, 79, 0, 255), stop:0.19 rgba(50, 147, 22, 255), stop:0.275 rgba(236, 191, 49, 255), stop:0.39 rgba(243, 61, 34, 255), stop:0.555 rgba(135, 81, 60, 255), stop:0.667 rgba(121, 75, 255, 255), stop:0.825 rgba(164, 255, 244, 255), stop:0.885 rgba(104, 222, 71, 255), stop:1 rgba(93, 128, 0, 255));")
        self.botonalegria = QPushButton(self.page_2)
        self.botonalegria.setObjectName(u"botonalegria")
        self.botonalegria.setGeometry(QRect(770, 160, 89, 25))
        self.botonalegria.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.botonenfadado = QPushButton(self.page_2)
        self.botonenfadado.setObjectName(u"botonenfadado")
        self.botonenfadado.setGeometry(QRect(770, 210, 89, 25))
        self.botonenfadado.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.nuevaconv = QPushButton(self.page_3)
        self.nuevaconv.setObjectName(u"nuevaconv")
        self.nuevaconv.setGeometry(QRect(480, 270, 201, 41))
        self.nuevaconv.setStyleSheet(u"QPushButton {\n"
"	background-color: qlineargradient(spread:pad, x1:0.163, y1:0.0911818, x2:0.762316, y2:0.676, stop:0 rgba(37, 185, 63, 255), stop:1 rgba(0, 166, 51, 255));\n"
"	color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(199, 199, 199, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	border: none;\n"
"	border-radius:20px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(199, 199, 199, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"")
        self.finprograma = QPushButton(self.page_3)
        self.finprograma.setObjectName(u"finprograma")
        self.finprograma.setGeometry(QRect(480, 370, 201, 41))
        self.finprograma.setStyleSheet(u"QPushButton {\n"
"	background-color: qlineargradient(spread:pad, x1:0.163, y1:0.0911818, x2:0.762316, y2:0.676, stop:0 rgba(37, 185, 63, 255), stop:1 rgba(0, 166, 51, 255));\n"
"	color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(199, 199, 199, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	border: none;\n"
"	border-radius:20px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(199, 199, 199, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"")
        self.stackedWidget.addWidget(self.page_3)

        self.verticalLayout.addWidget(self.frame_3)


        self.retranslateUi(guiDlg)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(guiDlg)
    # setupUi

    def retranslateUi(self, guiDlg):
        guiDlg.setWindowTitle(QCoreApplication.translate("guiDlg", u"interactGUI", None))
        self.label_2.setText(QCoreApplication.translate("guiDlg", u"Usuaria/o", None))
        self.inicioconversacion.setText(QCoreApplication.translate("guiDlg", u"Siguiente", None))
        self.finconversacion.setText(QCoreApplication.translate("guiDlg", u"Fin", None))
        self.botonalegria.setText(QCoreApplication.translate("guiDlg", u"Alegr\u00eda", None))
        self.botonenfadado.setText(QCoreApplication.translate("guiDlg", u"Enfado", None))
        self.nuevaconv.setText(QCoreApplication.translate("guiDlg", u"Nueva conversaci\u00f3n", None))
        self.finprograma.setText(QCoreApplication.translate("guiDlg", u"Finalizar programa", None))
    # retranslateUi

