import json
import os
from re import S
import sys
import traceback

from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from pydantic import ValidationError


from models.user import User
from schemas.user import ProfilePD, UserPD
from ui.ui_login_popup import Ui_LoginPopup
from ui.ui_reg_popup import Ui_RegisterPopup
from ui.ui_main import Ui_MainWindow

from settings.config import settings


class ExpenseTracker(QMainWindow):
    def __init__(self):
        super(ExpenseTracker, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.data = {}
        self.get_or_save_user_data()
        self.refresh_data()
        self._auth()

    def _auth(self):
        if not self.data:
            self.ui.reg_button.show()
            self.ui.login_button.show()
            self.ui.reg_button.clicked.connect(self.open_reg_popup)
            self.ui.login_button.clicked.connect(self.open_login_popup)
        else:
            self.ui.reg_button.hide()
            self.ui.login_button.hide()

            self.ui.logout_button = QPushButton(self.ui.AuthFrame)
            self.ui.logout_button.setObjectName("logout_button")
            self.ui.logout_button.setStyleSheet(
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
            self.ui.auth_buttons.addWidget(self.ui.logout_button)
            self.ui.logout_button.setText("Выйти")
            self.ui.logout_button.clicked.connect(self.logout)

    def get_or_save_user_data(self, user_id: int = None) -> None:
        if user_id:
            user_obj = User.get(id=user_id)
            self.data = {
                "user_id": user_obj.id,
                "user_data": {
                    k: v
                    for k, v in dict(UserPD.model_validate(user_obj)).items()
                    if k not in ["password", "email"]
                },
            }

        user_data_file = settings.ROOT_PATH / "data" / "udata.json"

        if user_data_file.exists():
            with open(user_data_file, "r", encoding="utf-8") as fl:
                self.data = json.load(fl)
        else:
            if user_id and user_obj:
                with open(user_data_file, "w", encoding="utf-8") as fl:
                    json.dump(self.data, fl, ensure_ascii=False, indent=4)

    def refresh_data(self):
        """
        Обновление данных по конкртеному пользователю
        """
        if self.data != {}:
            user = User.get(id=self.data["user_id"])
            self.ui.UserDataArea.show()
            user_pd = UserPD.model_validate(user)
            self.ui.role_data.setText(user_pd.role)
            self.ui.phone_data.setText(user_pd.profile["phone"])
            self.ui.name_data.setText(user_pd.profile["name"])
            self.ui.suname_data.setText(user_pd.profile["suname"])
            self.ui.about_data.setText(user_pd.profile["about"])
            self.ui.datebd_data.setText(user_pd.profile["date_birthday"])
        else:
            self.ui.UserDataArea.hide()

    def open_reg_popup(self):
        """
        Открытие окна регистрации
        """
        self.new_window = QtWidgets.QDialog()
        self.reg_ui_window = Ui_RegisterPopup()
        self.reg_ui_window.setupUi(self.new_window)
        self.new_window.show()
        self.reg_ui_window.confim_button.clicked.connect(self.confim_reg)

    def confim_reg(self):
        """
        Подтверждение регистрации
        """
        username = self.reg_ui_window.username_input_2.text()
        email = self.reg_ui_window.email_input.text()
        password = self.reg_ui_window.pass_input.text()
        confim_password = self.reg_ui_window.confim_pass_input.text()

        if password != confim_password:
            self.reg_ui_window.error_msg.setText("Пароли не совпадают")
            return

        try:
            user_pd = UserPD(
                username=username, email=email, password=password, profile=None
            )
        except ValidationError as e:
            error_msgs = [error["msg"] for error in e.errors()]
            self.reg_ui_window.error_msg.show()
            self.reg_ui_window.error_msg.setText(
                "• " + "\n• ".join(error_msgs).replace("Value error,", "")
            )
            return

        user = User.create(**dict(user_pd))

        self.get_or_save_user_data(user.id)
        self._auth()
        self.refresh_data()

        self.new_window.close()

    def open_login_popup(self):
        """
        Открытие окна входа в аккаунт
        """
        self.new_window = QtWidgets.QDialog()
        self.login_ui_window = Ui_LoginPopup()
        self.login_ui_window.setupUi(self.new_window)
        self.new_window.show()
        self.login_ui_window.confim_button.clicked.connect(self.confim_login)

    def confim_login(self):
        """
        Подтверждение регистрации
        """
        username = self.login_ui_window.username_input.text()
        password = self.login_ui_window.pass_input.text()

        user = User.get(username=username)

        if user:
            if user.password == password:
                self.new_window.close()
                self.get_or_save_user_data(user.id)
                self._auth()
                self.refresh_data()
                return
        self.login_ui_window.error_msg.show()
        self.login_ui_window.error_msg.setText(
            "• " + "\n• ".join(["Invalid login credentials. Please try again."])
        )

    def logout(self):
        self.ui.logout_button.hide()
        self.data = {}
        data_file = settings.ROOT_PATH / "data" / "udata.json"
        os.remove(data_file)
        self._auth()
        self.refresh_data()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ExpenseTracker()
    window.show()

    sys.exit(app.exec())
