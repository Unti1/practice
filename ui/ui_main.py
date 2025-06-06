# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QFrame,
    QHBoxLayout,
    QHeaderView,
    QLabel,
    QMainWindow,
    QPushButton,
    QSizePolicy,
    QTableView,
    QVBoxLayout,
    QWidget,
)
import ui.res_rc as res_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(794, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));\n"
            "font-family: Roboto;"
        )
        self.OperationsData = QTableView(self.centralwidget)
        self.OperationsData.setObjectName("OperationsData")
        self.OperationsData.setGeometry(QRect(116, 0, 411, 601))
        self.OperationsData.setStyleSheet(
            "QTableView {\n"
            "background-color: rgba(0,0,0,60);\n"
            "border: 1px solid rgba(0,0,0,80);\n"
            "border-radius: 10px;\n"
            "}\n"
            "\n"
            "QTableView:section {\n"
            "background-color: rgb(53,53,53);\n"
            "border: none;\n"
            "height: 50px;\n"
            "font-size: 14pt;\n"
            "}\n"
            "\n"
            "QTableView:item {\n"
            "border-style: none;\n"
            "border-botton: rgba(255,255,255,50);\n"
            "}\n"
            "\n"
            "QTableView:item:select {\n"
            "border: none;\n"
            "color: rgb(255,255,255,);\n"
            "background-color: rgba(255,255,255, 50);\n"
            "}\n"
            "\n"
            "\n"
            ""
        )
        self.UserDataArea = QFrame(self.centralwidget)
        self.UserDataArea.setObjectName("UserDataArea")
        self.UserDataArea.setGeometry(QRect(540, 110, 231, 201))
        self.UserDataArea.setStyleSheet(
            "background-color: rgba(0,0,0, 40);\nborder: none;\n"
        )
        self.verticalLayout = QVBoxLayout(self.UserDataArea)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.role_data = QLabel(self.UserDataArea)
        self.role_data.setObjectName("role_data")
        self.role_data.setStyleSheet(
            "background-color: rgba(0,0,0, 40);\nborder: none;\n"
        )
        self.role_data.setAlignment(
            Qt.AlignmentFlag.AlignLeading
            | Qt.AlignmentFlag.AlignLeft
            | Qt.AlignmentFlag.AlignVCenter
        )

        self.verticalLayout.addWidget(self.role_data)

        self.phone_data = QLabel(self.UserDataArea)
        self.phone_data.setObjectName("phone_data")
        self.phone_data.setAlignment(
            Qt.AlignmentFlag.AlignLeading
            | Qt.AlignmentFlag.AlignLeft
            | Qt.AlignmentFlag.AlignVCenter
        )

        self.verticalLayout.addWidget(self.phone_data)

        self.name_data = QLabel(self.UserDataArea)
        self.name_data.setObjectName("name_data")
        self.name_data.setAlignment(
            Qt.AlignmentFlag.AlignLeading
            | Qt.AlignmentFlag.AlignLeft
            | Qt.AlignmentFlag.AlignVCenter
        )

        self.verticalLayout.addWidget(self.name_data)

        self.suname_data = QLabel(self.UserDataArea)
        self.suname_data.setObjectName("suname_data")
        self.suname_data.setAlignment(
            Qt.AlignmentFlag.AlignLeading
            | Qt.AlignmentFlag.AlignLeft
            | Qt.AlignmentFlag.AlignVCenter
        )

        self.verticalLayout.addWidget(self.suname_data)

        self.about_data = QLabel(self.UserDataArea)
        self.about_data.setObjectName("about_data")
        self.about_data.setAlignment(
            Qt.AlignmentFlag.AlignLeading
            | Qt.AlignmentFlag.AlignLeft
            | Qt.AlignmentFlag.AlignVCenter
        )

        self.verticalLayout.addWidget(self.about_data)

        self.datebd_data = QLabel(self.UserDataArea)
        self.datebd_data.setObjectName("datebd_data")
        self.datebd_data.setAlignment(
            Qt.AlignmentFlag.AlignLeading
            | Qt.AlignmentFlag.AlignLeft
            | Qt.AlignmentFlag.AlignVCenter
        )

        self.verticalLayout.addWidget(self.datebd_data)

        self.ControlFrame = QFrame(self.centralwidget)
        self.ControlFrame.setObjectName("ControlFrame")
        self.ControlFrame.setGeometry(QRect(2, 1, 111, 141))
        self.ControlFrame.setStyleSheet(
            "background-color: rgba(0,0,0, 40);\nborder: none;\n"
        )
        self.ControlButtonsArea = QVBoxLayout(self.ControlFrame)
        self.ControlButtonsArea.setSpacing(0)
        self.ControlButtonsArea.setObjectName("ControlButtonsArea")
        self.ControlButtonsArea.setContentsMargins(0, 0, 0, 0)
        self.add_row = QPushButton(self.ControlFrame)
        self.add_row.setObjectName("add_row")
        self.add_row.setStyleSheet(
            "QPushButton {\n"
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
            "}"
        )
        icon = QIcon()
        icon.addFile(
            ":/icons/icons/add.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off
        )
        self.add_row.setIcon(icon)

        self.ControlButtonsArea.addWidget(self.add_row)

        self.upd_row = QPushButton(self.ControlFrame)
        self.upd_row.setObjectName("upd_row")
        self.upd_row.setStyleSheet(
            "QPushButton {\n"
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
            "}"
        )
        icon1 = QIcon()
        icon1.addFile(
            ":/icons/icons/edit.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off
        )
        self.upd_row.setIcon(icon1)

        self.ControlButtonsArea.addWidget(self.upd_row)

        self.del_row = QPushButton(self.ControlFrame)
        self.del_row.setObjectName("del_row")
        self.del_row.setStyleSheet(
            "QPushButton {\n"
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
            "}"
        )
        icon2 = QIcon()
        icon2.addFile(
            ":/icons/icons/delete.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off
        )
        self.del_row.setIcon(icon2)

        self.ControlButtonsArea.addWidget(self.del_row)

        self.WalletFrame = QFrame(self.centralwidget)
        self.WalletFrame.setObjectName("WalletFrame")
        self.WalletFrame.setGeometry(QRect(540, 380, 241, 221))
        self.WalletFrame.setStyleSheet(
            "background-color: rgba(0,0,0, 40);\nborder: none;\n"
        )
        self.UserBalance = QVBoxLayout(self.WalletFrame)
        self.UserBalance.setSpacing(3)
        self.UserBalance.setObjectName("UserBalance")
        self.UserBalance.setContentsMargins(0, 0, 0, 0)
        self.CurrentWallet = QFrame(self.WalletFrame)
        self.CurrentWallet.setObjectName("CurrentWallet")
        self.horizontalLayout_3 = QHBoxLayout(self.CurrentWallet)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.WalletText = QLabel(self.CurrentWallet)
        self.WalletText.setObjectName("WalletText")

        self.horizontalLayout_3.addWidget(self.WalletText)

        self.UserBalance.addWidget(self.CurrentWallet)

        self.EarningText = QLabel(self.WalletFrame)
        self.EarningText.setObjectName("EarningText")

        self.UserBalance.addWidget(self.EarningText)

        self.EarningArea = QFrame(self.WalletFrame)
        self.EarningArea.setObjectName("EarningArea")
        self.horizontalLayout_2 = QHBoxLayout(self.EarningArea)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.icon_uptrand = QLabel(self.EarningArea)
        self.icon_uptrand.setObjectName("icon_uptrand")
        self.icon_uptrand.setMaximumSize(QSize(24, 16777215))
        self.icon_uptrand.setPixmap(QPixmap(":/icons/icons/trending_up.svg"))

        self.horizontalLayout_2.addWidget(self.icon_uptrand)

        self.value_uptrand = QLabel(self.EarningArea)
        self.value_uptrand.setObjectName("value_uptrand")

        self.horizontalLayout_2.addWidget(self.value_uptrand)

        self.UserBalance.addWidget(self.EarningArea)

        self.OutcomeText = QLabel(self.WalletFrame)
        self.OutcomeText.setObjectName("OutcomeText")

        self.UserBalance.addWidget(self.OutcomeText)

        self.OutcomeWalleArea = QFrame(self.WalletFrame)
        self.OutcomeWalleArea.setObjectName("OutcomeWalleArea")
        self.horizontalLayout = QHBoxLayout(self.OutcomeWalleArea)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.icon_downtrand = QLabel(self.OutcomeWalleArea)
        self.icon_downtrand.setObjectName("icon_downtrand")
        self.icon_downtrand.setMaximumSize(QSize(24, 16777215))
        self.icon_downtrand.setPixmap(QPixmap(":/icons/icons/trending_down.svg"))

        self.horizontalLayout.addWidget(self.icon_downtrand)

        self.value_downtrand = QLabel(self.OutcomeWalleArea)
        self.value_downtrand.setObjectName("value_downtrand")

        self.horizontalLayout.addWidget(self.value_downtrand)

        self.UserBalance.addWidget(self.OutcomeWalleArea)

        self.AuthFrame = QFrame(self.centralwidget)
        self.AuthFrame.setObjectName("AuthFrame")
        self.AuthFrame.setGeometry(QRect(530, 0, 261, 31))
        self.AuthFrame.setStyleSheet("background-color: none;\nborder: none;\n")
        self.auth_buttons = QHBoxLayout(self.AuthFrame)
        self.auth_buttons.setSpacing(1)
        self.auth_buttons.setObjectName("auth_buttons")
        self.auth_buttons.setContentsMargins(0, 0, 0, 0)
        self.reg_button = QPushButton(self.AuthFrame)
        self.reg_button.setObjectName("reg_button")
        self.reg_button.setStyleSheet(
            "QPushButton {\n"
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
            "}"
        )
        icon3 = QIcon()
        icon3.addFile(
            ":/icons/icons/person_add.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off
        )
        self.reg_button.setIcon(icon3)

        self.auth_buttons.addWidget(self.reg_button)

        self.login_button = QPushButton(self.AuthFrame)
        self.login_button.setObjectName("login_button")
        self.login_button.setStyleSheet(
            "QPushButton {\n"
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
            "}"
        )
        icon4 = QIcon()
        icon4.addFile(
            ":/icons/icons/login.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off
        )
        self.login_button.setIcon(icon4)

        self.auth_buttons.addWidget(self.login_button)
        
        self.UserDataLabel = QFrame(self.centralwidget)
        self.UserDataLabel.setObjectName("UserDataLabel")
        self.UserDataLabel.setGeometry(QRect(550, 70, 211, 31))
        self.UserDataLabel.setMaximumSize(QSize(16777215, 50))
        self.UserDataLabel.setStyleSheet(
            "background-color: rgba(0,0,0, 40);\nborder: none;\n"
        )
        self.horizontalLayout_4 = QHBoxLayout(self.UserDataLabel)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.UserDataLabel)
        self.label_15.setObjectName("label_15")
        self.label_15.setMaximumSize(QSize(24, 16777215))
        self.label_15.setStyleSheet("background-color: rgba(255,255,255,50);")
        self.label_15.setFrameShadow(QFrame.Shadow.Raised)
        self.label_15.setPixmap(QPixmap(":/icons/icons/person.svg"))
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_15)

        self.label_14 = QLabel(self.UserDataLabel)
        self.label_14.setObjectName("label_14")
        self.label_14.setStyleSheet(
            "background-color: rgba(0,0,0, 40);\nborder: none;\n"
        )
        self.label_14.setFrameShadow(QFrame.Shadow.Raised)
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_14)

        self.SupportButton = QPushButton(self.centralwidget)
        self.SupportButton.setObjectName("SupportButton")
        self.SupportButton.setGeometry(QRect(2, 554, 111, 41))
        self.SupportButton.setStyleSheet(
            "QPushButton {\n"
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
            "}"
        )
        icon5 = QIcon()
        icon5.addFile(
            ":/icons/icons/support_agent.svg",
            QSize(),
            QIcon.Mode.Normal,
            QIcon.State.Off,
        )
        self.SupportButton.setIcon(icon5)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate(
                "MainWindow",
                "\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u044b",
                None,
            )
        )
        self.role_data.setText(QCoreApplication.translate("MainWindow", ":Role:", None))
        self.phone_data.setText(
            QCoreApplication.translate("MainWindow", ":phone:", None)
        )
        self.name_data.setText(QCoreApplication.translate("MainWindow", ":name:", None))
        self.suname_data.setText(
            QCoreApplication.translate("MainWindow", ":suname:", None)
        )
        self.about_data.setText(
            QCoreApplication.translate("MainWindow", ":about:", None)
        )
        self.datebd_data.setText(
            QCoreApplication.translate("MainWindow", ":datebirthday:", None)
        )
        self.add_row.setText(
            QCoreApplication.translate(
                "MainWindow", "\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None
            )
        )
        self.upd_row.setText(
            QCoreApplication.translate(
                "MainWindow", "\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None
            )
        )
        self.del_row.setText(
            QCoreApplication.translate(
                "MainWindow", "\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None
            )
        )
        self.WalletText.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0422\u0435\u043a\u0443\u0449\u0438\u0439 \u0441\u0447\u0451\u0442",
                None,
            )
        )
        self.EarningText.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0417\u0430\u0440\u0430\u0431\u043e\u0442\u0430\u043d\u043e",
                None,
            )
        )
        self.icon_uptrand.setText("")
        self.value_uptrand.setText(
            QCoreApplication.translate("MainWindow", "income", None)
        )
        self.OutcomeText.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0417\u0430\u0440\u0430\u0431\u043e\u0442\u0430\u043d\u043e",
                None,
            )
        )
        self.icon_downtrand.setText("")
        self.value_downtrand.setText(
            QCoreApplication.translate("MainWindow", "outcome", None)
        )
        self.reg_button.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f",
                None,
            )
        )
        self.login_button.setText(
            QCoreApplication.translate(
                "MainWindow", "\u0412\u043e\u0439\u0442\u0438", None
            )
        )
        self.label_15.setText("")
        self.label_14.setText(
            QCoreApplication.translate(
                "MainWindow", "\u0414\u0430\u043d\u043d\u044b\u0435", None
            )
        )
        self.SupportButton.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041f\u043e\u0434\u0434\u0435\u0440\u0436\u043a\u0430",
                None,
            )
        )

    # retranslateUi
