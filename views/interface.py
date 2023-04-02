# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLayout, QMainWindow,
    QPushButton, QScrollArea, QSizePolicy, QVBoxLayout,
    QWidget)
from login import Ui_LoginWindow
from register import Ui_RegisterWindow

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(1263, 826)
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        icon = QIcon()
        icon.addFile(u"__siesta_tantei_wa_mou_shindeiru_drawn_by_lua22__sample-6b25b3a8cf6b7de416ce0100826da1b4.jpg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.000000000000000)
#if QT_CONFIG(statustip)
        MainWindow.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
        MainWindow.setStyleSheet(u"*{\n"
"	border: none;\n"
"	margin: 0;\n"
"	padding: 0;\n"
"	scrollbar-width: thin\n"
"}\n"
"\n"
"QSrollBar{\n"
"	border:none;\n"
"	background-color: rgb(161, 161, 161);\n"
"	margin: 0\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical, QScrollBar::add-line:horizontal, QScrollBar::sub-line:vertical, QScrollBar::sub-line:horizontal{\n"
"	border: none;\n"
"	background: none\n"
"}\n"
"\n"
"QScrollBar:handle{\n"
"	border:none;\n"
"	background-color: rgb(64, 65, 66);\n"
"	border-radius: 8%;\n"
"	width: 12px\n"
"}\n"
"\n"
"QScrollBar::handle:vertical{\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal, QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"	border: none;\n"
"}\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical, QScrollBar:left-arrow:horizontal, QScrollBar::right-arrow:horizontal {\n"
"    border: none;\n"
"	background:none;\n"
" }\n"
"QScrollBar::handle:vertical:hove"
                        "r, QScrollBar::handle:horizontal:hover{	\n"
"	background-color: rgb(36, 36, 36);\n"
"}\n"
"QScrollBar::handle:vertical:pressed, QScrollBar::handle:horizontal:pressed {	\n"
"	background-color: rgb(24,24,24);\n"
"}\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
"	margin: 0;\n"
"	padding: 0;\n"
"	border: none\n"
"}")
        self.verticalLayout_7 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.categories = QFrame(self.centralwidget)
        self.categories.setObjectName(u"categories")
        self.categories.setMaximumSize(QSize(16777215, 100))
        self.categories.setStyleSheet(u"*{\n"
"	border:none;\n"
"	background: 	#3e3e42;\n"
"	color: white;\n"
"	margin: 0;\n"
"	padding: 0;\n"
"}\n"
"\n"
"QPushButton{\n"
"	text-decoration: underline;\n"
"	font-size: 14px;\n"
"	font: 10pt url('https://fonts.googleapis.com/css2?family=Oswald:wght@500&family=Roboto:wght@300&display=swap');\n"
"}\n"
"\n"
".QFrame#categories{\n"
"	width:100%;\n"
"	padding: 0;\n"
"	border:100px\n"
"}")
        self.gridLayout_2 = QGridLayout(self.categories)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, -1, 0)
        self.app_icon = QLabel(self.categories)
        self.app_icon.setObjectName(u"app_icon")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.app_icon.sizePolicy().hasHeightForWidth())
        self.app_icon.setSizePolicy(sizePolicy)
        self.app_icon.setMinimumSize(QSize(94, 90))
        self.app_icon.setMaximumSize(QSize(94, 94))
        self.app_icon.setPixmap(QPixmap(u"assets/c2809fdd51f6ea93032bfed10dcf824b.png"))
        self.app_icon.setScaledContents(True)
        self.app_icon.setWordWrap(True)
        self.app_icon.setMargin(0)
        self.app_icon.setIndent(-1)

        self.gridLayout_2.addWidget(self.app_icon, 0, 0, 4, 2, Qt.AlignLeft|Qt.AlignVCenter)

        self.user_action = QWidget(self.categories)
        self.user_action.setObjectName(u"user_action")
        self.horizontalLayout_2 = QHBoxLayout(self.user_action)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.login = QPushButton(self.user_action)
        self.login.setObjectName(u"login")
        self.login.setMaximumSize(QSize(100, 16777215))
        self.login.setCursor(QCursor(Qt.PointingHandCursor))
        self.login.setStyleSheet(u"*{\n"
"	color: white\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"user (3).png", QSize(), QIcon.Normal, QIcon.Off)
        self.login.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.login)

        self.register_2 = QPushButton(self.user_action)
        self.register_2.setObjectName(u"register_2")
        self.register_2.setMaximumSize(QSize(100, 16777215))
        self.register_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.register_2.setStyleSheet(u"*{\n"
"	color: white\n"
"}")
        self.register_2.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.register_2)


        self.gridLayout_2.addWidget(self.user_action, 0, 4, 1, 1)

        self.app_name = QLabel(self.categories)
        self.app_name.setObjectName(u"app_name")
        self.app_name.setMinimumSize(QSize(0, 25))
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.app_name.setFont(font)

        self.gridLayout_2.addWidget(self.app_name, 0, 3, 2, 1, Qt.AlignHCenter)

        self.category_container = QHBoxLayout()
        self.category_container.setSpacing(70)
        self.category_container.setObjectName(u"category_container")
        self.category_container.setSizeConstraint(QLayout.SetNoConstraint)
        self.category_container.setContentsMargins(0, 10, 0, 0)
        self.Economy = QPushButton(self.categories)
        self.Economy.setObjectName(u"Economy")
        self.Economy.setCursor(QCursor(Qt.PointingHandCursor))

        self.category_container.addWidget(self.Economy)

        self.Politics = QPushButton(self.categories)
        self.Politics.setObjectName(u"Politics")
        self.Politics.setCursor(QCursor(Qt.PointingHandCursor))

        self.category_container.addWidget(self.Politics)

        self.Traffic = QPushButton(self.categories)
        self.Traffic.setObjectName(u"Traffic")
        self.Traffic.setCursor(QCursor(Qt.PointingHandCursor))

        self.category_container.addWidget(self.Traffic)

        self.Medical = QPushButton(self.categories)
        self.Medical.setObjectName(u"Medical")
        self.Medical.setCursor(QCursor(Qt.PointingHandCursor))

        self.category_container.addWidget(self.Medical)

        self.Sport = QPushButton(self.categories)
        self.Sport.setObjectName(u"Sport")
        self.Sport.setCursor(QCursor(Qt.PointingHandCursor))

        self.category_container.addWidget(self.Sport)

        self.Travel = QPushButton(self.categories)
        self.Travel.setObjectName(u"Travel")
        self.Travel.setCursor(QCursor(Qt.PointingHandCursor))

        self.category_container.addWidget(self.Travel)

        self.Entertain = QPushButton(self.categories)
        self.Entertain.setObjectName(u"Entertain")
        self.Entertain.setCursor(QCursor(Qt.PointingHandCursor))

        self.category_container.addWidget(self.Entertain)

        self.SciTech = QPushButton(self.categories)
        self.SciTech.setObjectName(u"SciTech")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.SciTech.sizePolicy().hasHeightForWidth())
        self.SciTech.setSizePolicy(sizePolicy1)
        self.SciTech.setBaseSize(QSize(0, 0))
        self.SciTech.setCursor(QCursor(Qt.PointingHandCursor))

        self.category_container.addWidget(self.SciTech)

        self.category_container.setStretch(0, 1)
        self.category_container.setStretch(1, 1)
        self.category_container.setStretch(2, 1)
        self.category_container.setStretch(3, 1)
        self.category_container.setStretch(4, 1)
        self.category_container.setStretch(5, 1)
        self.category_container.setStretch(6, 1)
        self.category_container.setStretch(7, 2)

        self.gridLayout_2.addLayout(self.category_container, 2, 3, 2, 1)


        self.verticalLayout_7.addWidget(self.categories)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1259, 1419))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stonk = QFrame(self.scrollAreaWidgetContents)
        self.stonk.setObjectName(u"stonk")
        self.stonk.setFrameShape(QFrame.StyledPanel)
        self.stonk.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.stonk)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.hot_news = QFrame(self.stonk)
        self.hot_news.setObjectName(u"hot_news")
        self.hot_news.setMaximumSize(QSize(16777215, 16777215))
        self.hot_news.setStyleSheet(u"*{\n"
"	background: transparent;\n"
"	border-radius: 10px;\n"
"	word-wrap: break-word;\n"
"	width: auto;\n"
"	height: auto\n"
"}\n"
"")
        self.gridLayout_4 = QGridLayout(self.hot_news)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.hot_news_container = QFrame(self.hot_news)
        self.hot_news_container.setObjectName(u"hot_news_container")
        self.hot_news_container.setFrameShape(QFrame.StyledPanel)
        self.hot_news_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.hot_news_container)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.hot_news_label = QLabel(self.hot_news_container)
        self.hot_news_label.setObjectName(u"hot_news_label")
        self.hot_news_label.setMinimumSize(QSize(711, 32))
        self.hot_news_label.setMaximumSize(QSize(711, 32))
        self.hot_news_label.setAutoFillBackground(False)

        self.verticalLayout_2.addWidget(self.hot_news_label)

        self.hot_news_image_2 = QLabel(self.hot_news_container)
        self.hot_news_image_2.setObjectName(u"hot_news_image_2")
        self.hot_news_image_2.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.hot_news_image_2.sizePolicy().hasHeightForWidth())
        self.hot_news_image_2.setSizePolicy(sizePolicy2)
        self.hot_news_image_2.setMinimumSize(QSize(0, 0))
        self.hot_news_image_2.setMaximumSize(QSize(711, 400))
        self.hot_news_image_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.hot_news_image_2.setLayoutDirection(Qt.LeftToRight)
        self.hot_news_image_2.setAutoFillBackground(False)
        self.hot_news_image_2.setStyleSheet(u"")
        self.hot_news_image_2.setFrameShape(QFrame.Panel)
        self.hot_news_image_2.setFrameShadow(QFrame.Raised)
        self.hot_news_image_2.setTextFormat(Qt.RichText)
        self.hot_news_image_2.setPixmap(QPixmap(u"assets/Screenshot (14).png"))
        self.hot_news_image_2.setScaledContents(True)
        self.hot_news_image_2.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.hot_news_image_2, 0, Qt.AlignLeft|Qt.AlignTop)

        self.hot_news_description_6 = QLabel(self.hot_news_container)
        self.hot_news_description_6.setObjectName(u"hot_news_description_6")
        self.hot_news_description_6.setMaximumSize(QSize(16777215, 60))
        self.hot_news_description_6.setStyleSheet(u"*{\n"
"	background-color: white\n"
"}")
        self.hot_news_description_6.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.hot_news_description_6, 0, Qt.AlignTop)


        self.gridLayout_4.addWidget(self.hot_news_container, 2, 0, 1, 1)


        self.horizontalLayout.addWidget(self.hot_news)

        self.recent_news = QWidget(self.stonk)
        self.recent_news.setObjectName(u"recent_news")
        self.recent_news.setMaximumSize(QSize(1421, 16777215))
        self.recent_news.setAutoFillBackground(False)
        self.recent_news.setStyleSheet(u"*{\n"
"	background: transparent;\n"
"	border-radius: 10px;\n"
"	word-wrap: break-word;\n"
"	width: auto;\n"
"	height: auto\n"
"}\n"
"")
        self.verticalLayout_4 = QVBoxLayout(self.recent_news)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.hot_news_label_2 = QLabel(self.recent_news)
        self.hot_news_label_2.setObjectName(u"hot_news_label_2")
        self.hot_news_label_2.setMaximumSize(QSize(1000, 50))
        self.hot_news_label_2.setAutoFillBackground(False)

        self.verticalLayout_4.addWidget(self.hot_news_label_2)

        self.recent_news_ = QWidget(self.recent_news)
        self.recent_news_.setObjectName(u"recent_news_")
        self.recent_news_.setMaximumSize(QSize(488, 269))
        self.recent_news_.setStyleSheet(u"*{\n"
"	background: transparent;\n"
"	border-radius: 10px;\n"
"	word-wrap: break-word;\n"
"	width: auto;\n"
"	height: auto\n"
"}\n"
"")
        self.verticalLayout_5 = QVBoxLayout(self.recent_news_)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.recent_2_image = QLabel(self.recent_news_)
        self.recent_2_image.setObjectName(u"recent_2_image")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.recent_2_image.sizePolicy().hasHeightForWidth())
        self.recent_2_image.setSizePolicy(sizePolicy3)
        self.recent_2_image.setMinimumSize(QSize(0, 0))
        self.recent_2_image.setMaximumSize(QSize(16777215, 16777215))
        self.recent_2_image.setCursor(QCursor(Qt.PointingHandCursor))
        self.recent_2_image.setPixmap(QPixmap(u"assets/Screenshot (14).png"))
        self.recent_2_image.setScaledContents(True)

        self.verticalLayout_5.addWidget(self.recent_2_image)

        self.recent_2_description = QLabel(self.recent_news_)
        self.recent_2_description.setObjectName(u"recent_2_description")
        sizePolicy2.setHeightForWidth(self.recent_2_description.sizePolicy().hasHeightForWidth())
        self.recent_2_description.setSizePolicy(sizePolicy2)
        self.recent_2_description.setMaximumSize(QSize(16777215, 60))
        self.recent_2_description.setStyleSheet(u"*{\n"
"	background-color: white\n"
"}")
        self.recent_2_description.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.recent_2_description)


        self.verticalLayout_4.addWidget(self.recent_news_)

        self.recent_news_1 = QFrame(self.recent_news)
        self.recent_news_1.setObjectName(u"recent_news_1")
        self.recent_news_1.setMaximumSize(QSize(488, 269))
        self.verticalLayout_6 = QVBoxLayout(self.recent_news_1)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.recent_2_image_2 = QLabel(self.recent_news_1)
        self.recent_2_image_2.setObjectName(u"recent_2_image_2")
        self.recent_2_image_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.recent_2_image_2.setPixmap(QPixmap(u"assets/Screenshot (14).png"))
        self.recent_2_image_2.setScaledContents(True)

        self.verticalLayout_6.addWidget(self.recent_2_image_2)

        self.recent_1_description = QLabel(self.recent_news_1)
        self.recent_1_description.setObjectName(u"recent_1_description")
        self.recent_1_description.setMinimumSize(QSize(0, 0))
        self.recent_1_description.setMaximumSize(QSize(16777215, 60))
        self.recent_1_description.setStyleSheet(u"*{\n"
"	background-color: white\n"
"}")
        self.recent_1_description.setWordWrap(True)

        self.verticalLayout_6.addWidget(self.recent_1_description)


        self.verticalLayout_4.addWidget(self.recent_news_1)


        self.horizontalLayout.addWidget(self.recent_news)


        self.verticalLayout.addWidget(self.stonk)

        self.older_news = QFrame(self.scrollAreaWidgetContents)
        self.older_news.setObjectName(u"older_news")
        self.older_news.setFrameShape(QFrame.StyledPanel)
        self.older_news.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.older_news)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.hot_news_label_3 = QLabel(self.older_news)
        self.hot_news_label_3.setObjectName(u"hot_news_label_3")
        self.hot_news_label_3.setMinimumSize(QSize(711, 32))
        self.hot_news_label_3.setMaximumSize(QSize(711, 32))
        self.hot_news_label_3.setAutoFillBackground(False)

        self.verticalLayout_12.addWidget(self.hot_news_label_3)

        self.old_1 = QFrame(self.older_news)
        self.old_1.setObjectName(u"old_1")
        self.old_1.setMaximumSize(QSize(1204, 181))
        self.old_1.setFrameShape(QFrame.StyledPanel)
        self.old_1.setFrameShadow(QFrame.Raised)
        self.formLayout_5 = QFormLayout(self.old_1)
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.old_1_image = QLabel(self.old_1)
        self.old_1_image.setObjectName(u"old_1_image")
        self.old_1_image.setMaximumSize(QSize(391, 181))
        self.old_1_image.setPixmap(QPixmap(u"assets/Screenshot (14).png"))
        self.old_1_image.setScaledContents(True)

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.old_1_image)

        self.old_1_set = QFrame(self.old_1)
        self.old_1_set.setObjectName(u"old_1_set")
        self.old_1_set.setFrameShape(QFrame.StyledPanel)
        self.old_1_set.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.old_1_set)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.old_1_title = QLabel(self.old_1_set)
        self.old_1_title.setObjectName(u"old_1_title")
        self.old_1_title.setMaximumSize(QSize(16777215, 20))
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        self.old_1_title.setFont(font1)

        self.verticalLayout_8.addWidget(self.old_1_title)

        self.old_1_description = QLabel(self.old_1_set)
        self.old_1_description.setObjectName(u"old_1_description")
        self.old_1_description.setMinimumSize(QSize(0, 0))
        self.old_1_description.setMaximumSize(QSize(16777215, 100))
        self.old_1_description.setStyleSheet(u"*{\n"
"	background-color: white\n"
"}")
        self.old_1_description.setWordWrap(True)

        self.verticalLayout_8.addWidget(self.old_1_description)


        self.formLayout_5.setWidget(0, QFormLayout.FieldRole, self.old_1_set)


        self.verticalLayout_12.addWidget(self.old_1)

        self.old_2 = QFrame(self.older_news)
        self.old_2.setObjectName(u"old_2")
        self.old_2.setMaximumSize(QSize(1204, 181))
        self.old_2.setFrameShape(QFrame.StyledPanel)
        self.old_2.setFrameShadow(QFrame.Raised)
        self.formLayout_8 = QFormLayout(self.old_2)
        self.formLayout_8.setObjectName(u"formLayout_8")
        self.old_2_image = QLabel(self.old_2)
        self.old_2_image.setObjectName(u"old_2_image")
        self.old_2_image.setMaximumSize(QSize(391, 181))
        self.old_2_image.setPixmap(QPixmap(u"assets/Screenshot (14).png"))
        self.old_2_image.setScaledContents(True)

        self.formLayout_8.setWidget(0, QFormLayout.LabelRole, self.old_2_image)

        self.old_2_set = QFrame(self.old_2)
        self.old_2_set.setObjectName(u"old_2_set")
        self.old_2_set.setFrameShape(QFrame.StyledPanel)
        self.old_2_set.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.old_2_set)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.old_2_title = QLabel(self.old_2_set)
        self.old_2_title.setObjectName(u"old_2_title")
        self.old_2_title.setMaximumSize(QSize(16777215, 20))
        self.old_2_title.setFont(font1)

        self.verticalLayout_11.addWidget(self.old_2_title)

        self.old_2_description = QLabel(self.old_2_set)
        self.old_2_description.setObjectName(u"old_2_description")
        self.old_2_description.setMinimumSize(QSize(0, 0))
        self.old_2_description.setMaximumSize(QSize(16777215, 100))
        self.old_2_description.setStyleSheet(u"*{\n"
"	background-color: white\n"
"}")
        self.old_2_description.setWordWrap(True)

        self.verticalLayout_11.addWidget(self.old_2_description)


        self.formLayout_8.setWidget(0, QFormLayout.FieldRole, self.old_2_set)


        self.verticalLayout_12.addWidget(self.old_2)

        self.old_3 = QFrame(self.older_news)
        self.old_3.setObjectName(u"old_3")
        self.old_3.setMaximumSize(QSize(1204, 181))
        self.old_3.setFrameShape(QFrame.StyledPanel)
        self.old_3.setFrameShadow(QFrame.Raised)
        self.formLayout_7 = QFormLayout(self.old_3)
        self.formLayout_7.setObjectName(u"formLayout_7")
        self.old_3_image = QLabel(self.old_3)
        self.old_3_image.setObjectName(u"old_3_image")
        self.old_3_image.setMaximumSize(QSize(391, 181))
        self.old_3_image.setPixmap(QPixmap(u"assets/Screenshot (14).png"))
        self.old_3_image.setScaledContents(True)

        self.formLayout_7.setWidget(0, QFormLayout.LabelRole, self.old_3_image)

        self.old_3_set = QFrame(self.old_3)
        self.old_3_set.setObjectName(u"old_3_set")
        self.old_3_set.setFrameShape(QFrame.StyledPanel)
        self.old_3_set.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.old_3_set)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.old_3_title = QLabel(self.old_3_set)
        self.old_3_title.setObjectName(u"old_3_title")
        self.old_3_title.setMaximumSize(QSize(16777215, 20))
        self.old_3_title.setFont(font1)

        self.verticalLayout_10.addWidget(self.old_3_title)

        self.old_3_description = QLabel(self.old_3_set)
        self.old_3_description.setObjectName(u"old_3_description")
        self.old_3_description.setMinimumSize(QSize(0, 0))
        self.old_3_description.setMaximumSize(QSize(16777215, 100))
        self.old_3_description.setStyleSheet(u"*{\n"
"	background-color: white\n"
"}")
        self.old_3_description.setWordWrap(True)

        self.verticalLayout_10.addWidget(self.old_3_description)


        self.formLayout_7.setWidget(0, QFormLayout.FieldRole, self.old_3_set)


        self.verticalLayout_12.addWidget(self.old_3)

        self.old_4 = QFrame(self.older_news)
        self.old_4.setObjectName(u"old_4")
        self.old_4.setMaximumSize(QSize(1204, 181))
        self.old_4.setFrameShape(QFrame.StyledPanel)
        self.old_4.setFrameShadow(QFrame.Raised)
        self.formLayout_6 = QFormLayout(self.old_4)
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.old_4_image = QLabel(self.old_4)
        self.old_4_image.setObjectName(u"old_4_image")
        self.old_4_image.setMaximumSize(QSize(391, 181))
        self.old_4_image.setPixmap(QPixmap(u"assets/Screenshot (14).png"))
        self.old_4_image.setScaledContents(True)

        self.formLayout_6.setWidget(0, QFormLayout.LabelRole, self.old_4_image)

        self.old_4_set = QFrame(self.old_4)
        self.old_4_set.setObjectName(u"old_4_set")
        self.old_4_set.setFrameShape(QFrame.StyledPanel)
        self.old_4_set.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.old_4_set)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.old_4_title = QLabel(self.old_4_set)
        self.old_4_title.setObjectName(u"old_4_title")
        self.old_4_title.setMaximumSize(QSize(16777215, 20))
        self.old_4_title.setFont(font1)

        self.verticalLayout_9.addWidget(self.old_4_title)

        self.old_4_description = QLabel(self.old_4_set)
        self.old_4_description.setObjectName(u"old_4_description")
        self.old_4_description.setMinimumSize(QSize(0, 0))
        self.old_4_description.setMaximumSize(QSize(16777215, 100))
        self.old_4_description.setStyleSheet(u"*{\n"
"	background-color: white\n"
"}")
        self.old_4_description.setWordWrap(True)

        self.verticalLayout_9.addWidget(self.old_4_description)


        self.formLayout_6.setWidget(0, QFormLayout.FieldRole, self.old_4_set)


        self.verticalLayout_12.addWidget(self.old_4)


        self.verticalLayout.addWidget(self.older_news)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_7.addWidget(self.scrollArea)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Newspaper App", None))
        self.app_icon.setText("")
        self.login.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.login.clicked.connect(self.login_win)
        self.register_2.setText(QCoreApplication.translate("MainWindow", u"Register", None))
        self.register_2.clicked.connect(self.register_win)
        self.app_name.setText(QCoreApplication.translate("MainWindow", u"TOMATO NEWS", None))
        self.Economy.setText(QCoreApplication.translate("MainWindow", u"Economy", None))
        self.Politics.setText(QCoreApplication.translate("MainWindow", u"Politics", None))
        self.Traffic.setText(QCoreApplication.translate("MainWindow", u"Traffic", None))
        self.Medical.setText(QCoreApplication.translate("MainWindow", u"Medical", None))
        self.Sport.setText(QCoreApplication.translate("MainWindow", u"Sport", None))
        self.Travel.setText(QCoreApplication.translate("MainWindow", u"Travel", None))
        self.Entertain.setText(QCoreApplication.translate("MainWindow", u"Entertain", None))
        self.SciTech.setText(QCoreApplication.translate("MainWindow", u"Science and Technology", None))
        self.hot_news_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">HOT NEWS</span></p></body></html>", None))
        self.hot_news_image_2.setText("")
        self.hot_news_description_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Lorem Ipsum</span><span style=\" font-size:10pt;\"> is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic</span></p></body></html>", None))
        self.hot_news_label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">	RECENT NEWS</span></p></body></html>", None))
        self.recent_2_image.setText("")
        self.recent_2_description.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Lorem Ipsum</span><span style=\" font-size:10pt;\"> is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic</span></p></body></html>", None))
        self.recent_2_image_2.setText("")
        self.recent_1_description.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Lorem Ipsum</span><span style=\" font-size:10pt;\"> is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic</span></p></body></html>", None))
        self.hot_news_label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">OLDER NEWS</span></p></body></html>", None))
        self.old_1_image.setText("")
        self.old_1_title.setText(QCoreApplication.translate("MainWindow", u"SAMPLE TITLE", None))
        self.old_1_description.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Lorem Ipsum</span><span style=\" font-size:10pt;\"> is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic</span></p></body></html>", None))
        self.old_2_image.setText("")
        self.old_2_title.setText(QCoreApplication.translate("MainWindow", u"SAMPLE TITLE", None))
        self.old_2_description.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Lorem Ipsum</span><span style=\" font-size:10pt;\"> is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic</span></p></body></html>", None))
        self.old_3_image.setText("")
        self.old_3_title.setText(QCoreApplication.translate("MainWindow", u"SAMPLE TITLE", None))
        self.old_3_description.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Lorem Ipsum</span><span style=\" font-size:10pt;\"> is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic</span></p></body></html>", None))
        self.old_4_image.setText("")
        self.old_4_title.setText(QCoreApplication.translate("MainWindow", u"SAMPLE TITLE", None))
        self.old_4_description.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Lorem Ipsum</span><span style=\" font-size:10pt;\"> is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic</span></p></body></html>", None))
    # retranslateUi
    
    def login_win(self):
        self.login = QMainWindow()
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self.login)
        self.login.show()

    def register_win(self):
        self.register = QMainWindow()
        self.ui = Ui_RegisterWindow()
        self.ui.setupUi(self.register)
        self.register.show()
