# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'register.ui'
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

class Ui_RegisterWindow(object):
    def setupUi(self, RegisterWindow):
        if not RegisterWindow.objectName():
            RegisterWindow.setObjectName(u"RegisterWindow")
        RegisterWindow.resize(403, 470)
        RegisterWindow.setMinimumSize(QSize(392, 369))
        RegisterWindow.setMaximumSize(QSize(510, 500))
        RegisterWindow.setStyleSheet(u".QLineEdit{\n"
"	width: 250%;\n"
"	height: auto;\n"
"	border:none;\n"
"	border-bottom: 1px solid black\n"
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
"*{\n"
"	background-color: rgb(255,255,255);\n"
"	margin: 0\n"
"}")
        self.centralwidget = QWidget(RegisterWindow)
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

        self.name_frame = QFrame(self.centralwidget)
        self.name_frame.setObjectName(u"name_frame")
        self.name_frame.setFrameShape(QFrame.StyledPanel)
        self.name_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.name_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.name_txt = QLabel(self.name_frame)
        self.name_txt.setObjectName(u"name_txt")
        self.name_txt.setMaximumSize(QSize(16777215, 20))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(False)
        self.name_txt.setFont(font1)

        self.verticalLayout_2.addWidget(self.name_txt)

        self.name_input = QLineEdit(self.name_frame)
        self.name_input.setObjectName(u"name_input")
        font2 = QFont()
        font2.setPointSize(11)
        self.name_input.setFont(font2)

        self.verticalLayout_2.addWidget(self.name_input)


        self.verticalLayout.addWidget(self.name_frame, 0, Qt.AlignHCenter)

        self.username_frame = QFrame(self.centralwidget)
        self.username_frame.setObjectName(u"username_frame")
        self.username_frame.setFrameShape(QFrame.StyledPanel)
        self.username_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.username_frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.username_txt = QLabel(self.username_frame)
        self.username_txt.setObjectName(u"username_txt")
        self.username_txt.setMaximumSize(QSize(16777215, 20))
        self.username_txt.setFont(font1)

        self.verticalLayout_4.addWidget(self.username_txt)

        self.username_input = QLineEdit(self.username_frame)
        self.username_input.setObjectName(u"username_input")
        self.username_input.setFont(font2)

        self.verticalLayout_4.addWidget(self.username_input)


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

        self.registerButton = QPushButton(self.centralwidget)
        self.registerButton.setObjectName(u"registerButton")
        self.registerButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.registerButton, 0, Qt.AlignHCenter)

        RegisterWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(RegisterWindow)

        QMetaObject.connectSlotsByName(RegisterWindow)
    # setupUi

    def retranslateUi(self, RegisterWindow):
        RegisterWindow.setWindowTitle(QCoreApplication.translate("RegisterWindow", u"MainWindow", None))
        self.title_txt.setText(QCoreApplication.translate("RegisterWindow", u"Register to become an Author", None))
        self.name_txt.setText(QCoreApplication.translate("RegisterWindow", u"Full Name", None))
        self.username_txt.setText(QCoreApplication.translate("RegisterWindow", u"Username", None))
        self.pwrd_txt.setText(QCoreApplication.translate("RegisterWindow", u"Password", None))
        self.registerButton.setText(QCoreApplication.translate("RegisterWindow", u"Register", None))
    # retranslateUi

