from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QDialog
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.uic import loadUi
import sys

class MainWindow(QDialog):

       def openLoginWindow(self):
              self.loginWindow = LoginWindow()
              self.loginWindow.show()

       def openRegisterWindow(self):
              self.registerWindow = RegisterWindow()
              self.registerWindow.show()

       def __init__(self):
              super(MainWindow, self).__init__()
              loadUi("./views/new_ui.ui", self)
              menu = QtWidgets.QMenu(self)
              actions = ["Login", "Register", "Exit"]
              for action in actions:
                     menu.addAction(action)
              self.functional_button.setMenu(menu)
              self.functional_button.setFlat(True)
              self.functional_button.setIcon(QtGui.QIcon("./views/assets/icons/user.png"))
              self.functional_button.setText("")
              self.functional_button.setIconSize(QtCore.QSize(50, 50))
              self.functional_button.setCursor(QtCore.Qt.CursorShape.PointingHandCursor)
              self.functional_button.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
              self.functional_button.setDown(True)

              self.functional_button.setStyleSheet("QPushButton::menu-indicator {image:none;}"
                                                   "QPushButton:pressed::menu-inidcator{image:none;}"
                                                   "QPushButton:pressed{border: none}"
                                                   "QPushButton{background-color: #ffffff; border-image: url(./views/assets/icons/user.png); border-radius: 50%; padding: 5px, border: 1px solid #000000;}")
              
              self.functional_button.menu().setStyleSheet("QMenu::item {background-color: transparent; padding: 5px; color: #000000;} "
                                         "QMenu::item:selected {background-color: #000000; color: #ffffff;}"
                                         "QMenu::item:pressed {background-color: #000000; color: #ffffff;} "
                                         "QMenu{background-color: #ffffff; border: 1px solid #000000; border-radius: 5px; padding: 5px; margin: 0px; font-size: 12px; font-family: 'Segoe UI';}")
              
              self.functional_button.menu().setCursor(QtCore.Qt.CursorShape.PointingHandCursor)
              self.functional_button.menu().triggered.connect(self.button_menu_action)
              self.show()
       def button_menu_action(self, action):
              if action.text() == "Login":
                     self.openLoginWindow()
              elif action.text() == "Register":
                     self.openRegisterWindow()
              elif action.text() == "Exit":
                     sys.exit()

class LoginWindow(QDialog):
       def __init__(self):
              super(LoginWindow, self).__init__()
              loadUi("./views/login/login.ui", self)
              self.submit_button.clicked.connect(self.submit)
              self.show()
       def submit(self):
              if not self.username_input.text() == "admin" and not self.password_input.text() == "admin":
                     self.status_label.setStyleSheet("color: #ff0000;")
                     if self.username_input.text() == "":
                            self.status_label.setText("Username is required")
                     elif self.password_input.text() == "":
                            self.status_label.setText("Password is required")
                     else:
                            self.status_label.setText("Invalid username or password")

class RegisterWindow(QDialog):
       def __init__(self):
              super(RegisterWindow, self).__init__()
              loadUi("./views/login/register.ui", self)
              self.show()

if __name__ == "__main__":
       app = QApplication(sys.argv)
       window = MainWindow()
       sys.exit(app.exec())
