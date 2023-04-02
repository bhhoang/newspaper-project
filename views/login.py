# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        if not LoginWindow.objectName():
            LoginWindow.setObjectName(u"LoginWindow")
        LoginWindow.resize(510, 293)
        LoginWindow.setMinimumSize(QSize(497, 0))
        LoginWindow.setMaximumSize(QSize(510, 300))
        LoginWindow.setStyleSheet(u".QLineEdit{\n"
"	border-radius: 5px;\n"
"	width: 250%;\n"
"	height: auto;\n"
"	border:none\n"
"}\n"
".QPushButton{\n"
"	background-color: rgb(1, 124, 255);\n"
"	border-radius: 5px;\n"
"	width: 80%;\n"
"	height: auto;\n"
"	color: white;\n"
"	border:none\n"
"}\n"
".QPushButton:focus{\n"
"	background-color: rgb(0, 50, 255);\n"
"	pointer-events:none;\n"
"	border: none\n"
"}\n"
"")
        self.centralwidget = QWidget(LoginWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 20)
        self.title_frame = QFrame(self.centralwidget)
        self.title_frame.setObjectName(u"title_frame")
        self.title_frame.setMaximumSize(QSize(16777215, 160))
        self.title_frame.setStyleSheet(u"background-color: rgb(42, 42, 42);\n"
"color: white")
        self.title_frame.setFrameShape(QFrame.StyledPanel)
        self.title_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.title_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.title_txt = QLabel(self.title_frame)
        self.title_txt.setObjectName(u"title_txt")
        font = QFont()
        font.setPointSize(20)
        self.title_txt.setFont(font)

        self.horizontalLayout.addWidget(self.title_txt, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout.addWidget(self.title_frame)

        self.username_frame = QFrame(self.centralwidget)
        self.username_frame.setObjectName(u"username_frame")
        self.username_frame.setFrameShape(QFrame.StyledPanel)
        self.username_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.username_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.username_txt = QLabel(self.username_frame)
        self.username_txt.setObjectName(u"username_txt")
        self.username_txt.setMaximumSize(QSize(16777215, 20))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(False)
        self.username_txt.setFont(font1)

        self.verticalLayout_2.addWidget(self.username_txt)

        self.username_input = QLineEdit(self.username_frame)
        self.username_input.setObjectName(u"username_input")
        font2 = QFont()
        font2.setPointSize(11)
        self.username_input.setFont(font2)

        self.verticalLayout_2.addWidget(self.username_input)


        self.verticalLayout.addWidget(self.username_frame, 0, Qt.AlignHCenter)

        self.pwrd_frame = QFrame(self.centralwidget)
        self.pwrd_frame.setObjectName(u"pwrd_frame")
        self.pwrd_frame.setFrameShape(QFrame.StyledPanel)
        self.pwrd_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.pwrd_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pwrd_txt = QLabel(self.pwrd_frame)
        self.pwrd_txt.setObjectName(u"pwrd_txt")
        self.pwrd_txt.setMaximumSize(QSize(16777215, 20))
        font3 = QFont()
        font3.setPointSize(12)
        self.pwrd_txt.setFont(font3)

        self.verticalLayout_3.addWidget(self.pwrd_txt)

        self.pwrd_input = QLineEdit(self.pwrd_frame)
        self.pwrd_input.setObjectName(u"pwrd_input")
        self.pwrd_input.setFont(font2)
        self.pwrd_input.setEchoMode(QLineEdit.Password)

        self.verticalLayout_3.addWidget(self.pwrd_input)


        self.verticalLayout.addWidget(self.pwrd_frame, 0, Qt.AlignHCenter)

        self.loginButton = QPushButton(self.centralwidget)
        self.loginButton.setObjectName(u"loginButton")
        self.loginButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.loginButton, 0, Qt.AlignHCenter)

        LoginWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoginWindow)

        QMetaObject.connectSlotsByName(LoginWindow)
    # setupUi

    def retranslateUi(self, LoginWindow):
        LoginWindow.setWindowTitle(QCoreApplication.translate("LoginWindow", u"MainWindow", None))
        self.title_txt.setText(QCoreApplication.translate("LoginWindow", u"Login as Author", None))
        self.username_txt.setText(QCoreApplication.translate("LoginWindow", u"Username", None))
        self.pwrd_txt.setText(QCoreApplication.translate("LoginWindow", u"Password", None))
        self.loginButton.setText(QCoreApplication.translate("LoginWindow", u"Login", None))
    # retranslateUi

