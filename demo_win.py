# Loadui in Python
#
# Path to the ui file : ./views/interface.ui

import configparser
from PyQt6.QtWidgets import QApplication, QMainWindow, QSplashScreen
from PyQt6.uic import loadUi
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication, QDialog, QWidget
from utils.logger import Info_Log, Warning_Log, Error_Log
from controller.newspaper import Newspapers
import os

# Load some global variables from base.conf
config = configparser.ConfigParser()
config.read('base.conf')    
os.environ['mongo_host'] = config['App']['mongo_host']


class Interface(QMainWindow):

    def __init__(self, parent=None):
        super(Interface, self).__init__(parent)
        loadUi('./views/interface.ui', self)
        self.login.clicked.connect(self.login_screen)
        self.register_2.clicked.connect(self.register_screen)

    def login_screen(self):
        self.login_screen = LoginScreen()
        self.login_screen.show()

    def register_screen(self):
        self.register_screen = RegisterScreen()
        self.register_screen.show()

class LoginScreen(QDialog):
    def __init__(self, parent=None):
        super(LoginScreen, self).__init__(parent)
        loadUi('./views/login/login.ui', self)
        self.submit_button.clicked.connect(self.login_function)

    # Login logic
    def login_function(self):
        username = self.username_input.text()
        password = self.password_input.text()
        if username == 'admin' and password == 'admin':
            Info_Log('Login successful')
        else:
            Warning_Log('Login failed')
            


class RegisterScreen(QDialog):
    def __init__(self, parent=None):
        super(RegisterScreen, self).__init__(parent)
        loadUi('./views/login/register.ui', self)
        self.submit_button.clicked.connect(self.register_function)
    def register_function(self):
        if self.password_input.text() == '' or self.username_input.text() == '' or self.email_input.text() == '':
            Error_Log('Please fill all the fields')
        else:
            full_name = self.name_input.text()
            username = self.username_input.text()
            password = self.password_input.text()
            Info_Log(f'User {username} want to register. Full name: {full_name}. Do you want to add author to the database? [Y/N]')
            answer = input()
            answer = answer.lower()
            if answer == 'y':
                Newspapers().add_author(full_name, username, password)
                Info_Log(f'Added {username} to the database')
            elif answer == 'n':
                Info_Log(f'Canceled adding {username} to the database')
            else:
                Error_Log('Please answer with Y or N')
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Interface()
    window.show()
    sys.exit(app.exec())
