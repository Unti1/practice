
import sys

from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow

from models.user import User
from schemas.user import ProfilePD, UserPD
from ui.ui_reg_popup import Ui_RegisterPopup
from ui.ui_main import Ui_MainWindow

def func():
    print('Hello')
    
class ExpenseTracker(QMainWindow):
    def __init__(self):
        super(ExpenseTracker, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.reg_button.clicked.connect(self.open_reg_popup)
        
    def open_reg_popup(self):
        self.new_window = QtWidgets.QDialog()
        self.reg_ui_window = Ui_RegisterPopup()
        self.reg_ui_window.setupUi(self.new_window)
        self.new_window.show()
        sender = self.sender()
        self.reg_ui_window.confim_button.clicked.connect(self.confim_reg)
        
    def confim_reg(self):
        username = self.reg_ui_window.username_input_2.text()
        email = self.reg_ui_window.email_input.text()
        password = self.reg_ui_window.pass_input.text()
        confim_password = self.reg_ui_window.confim_pass_input.text()
        
        print(f'User input:\n{username}\n{email}\n{password}\n{confim_password}')
        
        if password != confim_password:
            self.reg_ui_window.error_msg.setText('Пароли не совпадают')
            return
        
        try:
            ...
            user_pd = UserPD(username = username, email=email, password=password, profile=None)
        except Exception as e:
            self.reg_ui_window.error_msg.setText(str(e))
            print(e)
            return
        
        User.create(**dict(user_pd))
        self.new_window.close()
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ExpenseTracker()
    window.show()
    
    sys.exit(app.exec())
