# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_popup.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(350, 199)
        Dialog.setMaximumSize(QSize(350, 200))
        Dialog.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));\n"
"font-family: Roboto;")
        self.mainframe = QFrame(Dialog)
        self.mainframe.setObjectName(u"mainframe")
        self.mainframe.setGeometry(QRect(0, 0, 351, 201))
        self.mainframe.setStyleSheet(u"background-color: rgba(0,0,0, 40);\n"
"border: none;\n"
"")
        self.mainframe.setFrameShape(QFrame.Shape.StyledPanel)
        self.mainframe.setFrameShadow(QFrame.Shadow.Raised)
        self.main_label = QLabel(self.mainframe)
        self.main_label.setObjectName(u"main_label")
        self.main_label.setGeometry(QRect(160, 10, 31, 16))
        self.main_label.setStyleSheet(u"background-color: none;\n"
"border: none;\n"
"")
        self.username_label = QLabel(self.mainframe)
        self.username_label.setObjectName(u"username_label")
        self.username_label.setGeometry(QRect(10, 40, 111, 20))
        self.username_label.setStyleSheet(u"background-color: none;")
        self.pass_lab = QLabel(self.mainframe)
        self.pass_lab.setObjectName(u"pass_lab")
        self.pass_lab.setGeometry(QRect(10, 70, 111, 20))
        self.pass_lab.setStyleSheet(u"background-color: none;")
        self.error_msg = QLabel(self.mainframe)
        self.error_msg.setObjectName(u"error_msg")
        self.error_msg.setGeometry(QRect(10, 100, 331, 31))
        self.error_msg.setStyleSheet(u"background-color: none;")
        self.confim_button = QPushButton(self.mainframe)
        self.confim_button.setObjectName(u"confim_button")
        self.confim_button.setGeometry(QRect(40, 140, 271, 41))
        self.confim_button.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(0,0,0, 40);\n"
"border: 1px  solid rgba(0,0,0,70);\n"
"border-radius: 5px;\n"
"height: 50px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgba(255,255,255,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color:  rgba(255,255,255,80);\n"
"}")
        self.pass_input = QLineEdit(self.mainframe)
        self.pass_input.setObjectName(u"pass_input")
        self.pass_input.setGeometry(QRect(140, 70, 201, 21))
        self.pass_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.username_input = QLineEdit(self.mainframe)
        self.username_input.setObjectName(u"username_input")
        self.username_input.setGeometry(QRect(140, 40, 201, 21))
        self.username_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.main_label.setText(QCoreApplication.translate("Dialog", u"\u0412\u0445\u043e\u0434", None))
        self.username_label.setText(QCoreApplication.translate("Dialog", u"\u0418\u043c\u044f \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.pass_lab.setText(QCoreApplication.translate("Dialog", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.error_msg.setText(QCoreApplication.translate("Dialog", u":error_msg:", None))
        self.confim_button.setText(QCoreApplication.translate("Dialog", u"\u0412\u0445\u043e\u0434", None))
    # retranslateUi

