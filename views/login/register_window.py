from PyQt6.QtWidgets import QDialog
from PyQt6 import QtCore
from PyQt6.uic import loadUi
from controller.newspaper import Newspapers

news = Newspapers()


class RegisterWindow(QDialog):
    def __init__(self):
        super(RegisterWindow, self).__init__()
        loadUi("./views/login/register.ui", self)
        self.show()
        self.submit_button.clicked.connect(self.submit)

    def submit(self):
        if (self.name_input.text()).strip() == "" or self.password_input.text() == "" or self.username_input.text() == "" or self.email_input.text() == "":
            self.status_label.setStyleSheet("color: #ff0000;")
            self.status_label.setText("All fields are required")
        else:
            self.status_label.setStyleSheet("color: #00ff00;")
            username = self.username_input.text()
            password = self.password_input.text()
            name = self.name_input.text()
            email = self.email_input.text()

            state = news.create_author(str(username), password, str(name), str(email))
            if not state:
                self.status_label.setStyleSheet("color: #ff0000;")
                self.status_label.setText("Username or email already exists")
            else:
                self.status_label.setText("Register successful")
                QtCore.QTimer.singleShot(1000, self.close)
