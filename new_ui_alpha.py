from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QDialog
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.uic import loadUi
import sys
from  controller.newspaper import Newspapers

news = Newspapers()

class MainWindow(QMainWindow):

       def openLoginWindow(self):
              self.loginWindow = LoginWindow()
              self.loginWindow.show()

       def openRegisterWindow(self):
              self.registerWindow = RegisterWindow()
              self.registerWindow.show()

       def __init__(self):
              super(MainWindow, self).__init__()
              loadUi("./views/main/interface.ui", self)
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
              hot_news = news.get_hot_articles()[0]
              self.hot_news_title.setText(hot_news.get_title())
              self.hot_news_description.setText(hot_news.get_overview())
              print(hot_news.get_images())
              print(hot_news.get_id())
              self.hot_news_image.setScaledContents(True)           
              
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
              else:
                     self.status_label.setStyleSheet("color: #00ff00;")
                     self.status_label.setText("Login successful")

class RegisterWindow(QDialog):
       def __init__(self):
              super(RegisterWindow, self).__init__()
              loadUi("./views/login/register.ui", self)
              self.show()

class Older_news_element():
       def __init__(self):
                 
        self.old_1 = QtWidgets.QFrame(parent=self.older_news)
        self.old_1.setMaximumSize(QtCore.QSize(1204, 181))
        self.old_1.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.old_1.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.old_1.setObjectName("old_1")
        self.old_1.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        # TODO: Set lambda to function
        self.old_1.mousePressEvent = lambda event: print("Clicked old news 1")

        self.formLayout_5 = QtWidgets.QFormLayout(self.old_1)
        self.formLayout_5.setObjectName("formLayout_5")
        self.old_1_image = QtWidgets.QLabel(parent=self.old_1)
        self.old_1_image.setMaximumSize(QtCore.QSize(391, 181))
        self.old_1_image.setText("")
        self.old_1_image.setPixmap(QtGui.QPixmap())
        self.old_1_image.setScaledContents(True)
        self.old_1_image.setObjectName("old_1_image")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.old_1_image)
        self.old_1_set = QtWidgets.QFrame(parent=self.old_1)
        self.old_1_set.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.old_1_set.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.old_1_set.setObjectName("old_1_set")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.old_1_set)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.old_1_title = QtWidgets.QLabel(parent=self.old_1_set)
        self.old_1_title.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.old_1_title.setFont(font)
        self.old_1_title.setObjectName("old_1_title")
        self.verticalLayout_8.addWidget(self.old_1_title)
        self.old_1_description = QtWidgets.QLabel(parent=self.old_1_set)
        self.old_1_description.setMinimumSize(QtCore.QSize(0, 0))
        self.old_1_description.setMaximumSize(QtCore.QSize(16777215, 100))
        self.old_1_description.setStyleSheet("background-color: transparent; font-size: 15px;")
        self.old_1_description.setWordWrap(True)
        self.old_1_description.setObjectName("old_1_description")
        self.verticalLayout_8.addWidget(self.old_1_description)
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.old_1_set)
        self.verticalLayout_12.addWidget(self.old_1)


if __name__ == "__main__":
       app = QApplication(sys.argv)
       window = MainWindow()
       sys.exit(app.exec())
