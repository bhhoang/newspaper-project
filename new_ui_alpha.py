from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QDialog, QFrame, QVBoxLayout
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.uic import loadUi
import sys,os
from  controller.newspaper import Newspapers
from model.dbquery import Database
from selectolax.parser import HTMLParser
import requests, shutil
import configparser
import ctypes

myappid = u'group3.piratenews.maingui.1.0.0'
# u is for unicode
# From win7 onwards, you need to explicitly set the app user model id. Reference keyword: AppUserModelID
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

db = Database()
news = Newspapers()
not_available_image = "./views/assets/Resource/No_Image_Available.jpg"


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
              self.setWindowIcon(QtGui.QIcon("./views/assets/icons/logo.png"))
              self.setWindowTitle("Pirate News")
              self.stackedWidget.setCurrentWidget(self.main_page)
              self.app_mascot.setCursor(QtCore.Qt.CursorShape.PointingHandCursor)
              self.app_mascot.mousePressEvent = lambda event: self.stackedWidget.setCurrentWidget(self.main_page)
              self.app_mascot.setToolTip("Go to home page")
              self.Economy.setIcon(QtGui.QIcon("./views/assets/icons/statistics.png"))
              self.Politics.setIcon(QtGui.QIcon("./views/assets/icons/politics.png"))
              self.Sport.setIcon(QtGui.QIcon("./views/assets/icons/sport.png"))
              self.SciTech.setIcon(QtGui.QIcon("./views/assets/icons/science.png"))
              self.Entertain.setIcon(QtGui.QIcon("./views/assets/icons/music.png"))
              self.Traffic.setIcon(QtGui.QIcon("./views/assets/icons/car.png"))
              self.Medical.setIcon(QtGui.QIcon("./views/assets/icons/medical.png"))
              self.Travel.setIcon(QtGui.QIcon("./views/assets/icons/mountain.png"))
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
              recents = news.get_recent_articles()
              self.hot_news_title.setText(hot_news.get_title())
              self.hot_news_description.setText(hot_news.get_overview())
              if (hot_news.get_images() == None or hot_news.get_images() == []):
                     self.hot_news_image.setPixmap(QtGui.QPixmap(not_available_image))
              self.hot_news_image.setScaledContents(True)           
              self.hot_news_image.mousePressEvent = lambda event: self.open_article(hot_news)
              self.hot_news_container.setCursor(QtCore.Qt.CursorShape.PointingHandCursor)
              self.hot_news_image.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
              self.hot_news_image.setStyleSheet("border: 1px solid #000000; border-radius: 5px;")
              self.hot_news_image.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
              self.hot_news_image.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
              self.hot_news_image.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
              self.hot_news_image.setContentsMargins(0, 0, 0, 0)
              self.hot_news_image.setWordWrap(True)

              self.hot_news_title.mousePressEvent = lambda event: self.open_article(hot_news)

              self.recent_news_1.setCursor(QtCore.Qt.CursorShape.PointingHandCursor)
              self.recent_news_1.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
              self.recent_news_1.mousePressEvent = lambda event: self.open_article(recents[0])
              self.recent_1_title.setText(recents[0].get_title())
              self.recent_news_1.setToolTip(recents[0].get_title())
              self.recent_1_description.setText(recents[0].get_overview())
              if (recents[0].get_images() == None or recents[0].get_images() == []):
                     self.recent_1_image.setPixmap(QtGui.QPixmap(not_available_image))
              self.recent_1_image.setScaledContents(True)
              self.recent_1_image.setStyleSheet("border: 1px solid #000000; border-radius: 5px;")
              self.recent_1_image.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
              self.recent_1_image.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
              self.recent_1_image.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
              self.recent_1_image.setContentsMargins(0, 0, 0, 0)
              self.recent_1_image.setWordWrap(True)


              self.recent_news_2.setCursor(QtCore.Qt.CursorShape.PointingHandCursor)
              self.recent_news_2.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
              self.recent_news_2.mousePressEvent = lambda event: self.open_article(recents[1])
              self.recent_2_title.setText(recents[1].get_title())
              self.recent_news_2.setToolTip(recents[1].get_title())
              self.recent_2_description.setText(recents[1].get_overview())
              if (recents[1].get_images() == None or recents[1].get_images() == []):
                     self.recent_2_image.setPixmap(QtGui.QPixmap(not_available_image))
              self.recent_2_image.setScaledContents(True)
              self.recent_2_image.setStyleSheet("border: 1px solid #000000; border-radius: 5px;")
              self.recent_2_image.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
              self.recent_2_image.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
              self.recent_2_image.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
              self.recent_2_image.setContentsMargins(0, 0, 0, 0)
              self.recent_2_image.setWordWrap(True)

              ## Older news part
              self.old_1.setCursor(QtCore.Qt.CursorShape.PointingHandCursor)
              self.old_1.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
              self.old_1.mousePressEvent = lambda event: self.open_article(recents[2])
              self.old_1_title.setText(recents[2].get_title())
              self.old_1.setToolTip(recents[2].get_title())
              self.old_1_description.setText(recents[2].get_overview())
              if (recents[2].get_images() == None or recents[2].get_images() == []):
                     self.old_1_image.setPixmap(QtGui.QPixmap(not_available_image))
              self.old_1_image.setScaledContents(True)

              self.old_2.setCursor(QtCore.Qt.CursorShape.PointingHandCursor)
              self.old_2.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
              self.old_2.mousePressEvent = lambda event: self.open_article(recents[3])
              self.old_2_title.setText(recents[3].get_title())
              self.old_2.setToolTip(recents[3].get_title())
              self.old_2_description.setText(recents[3].get_overview())
              if (recents[3].get_images() == None or recents[3].get_images() == []):
                     self.old_2_image.setPixmap(QtGui.QPixmap(not_available_image))

              self.old_3.setCursor(QtCore.Qt.CursorShape.PointingHandCursor)
              self.old_3.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
              self.old_3.mousePressEvent = lambda event: self.open_article(recents[4])
              self.old_3_title.setText(recents[4].get_title())
              self.old_3.setToolTip(recents[4].get_title())
              self.old_3_description.setText(recents[4].get_overview())
              if (recents[4].get_images() == None or recents[4].get_images() == []):
                     self.old_3_image.setPixmap(QtGui.QPixmap(not_available_image))

              self.old_4.setCursor(QtCore.Qt.CursorShape.PointingHandCursor)
              self.old_4.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
              self.old_4.mousePressEvent = lambda event: self.open_article(recents[5])
              self.old_4_title.setText(recents[5].get_title())
              self.old_4.setToolTip(recents[5].get_title())
              self.old_4_description.setText(recents[5].get_overview())
              if (recents[5].get_images() == None or recents[5].get_images() == []):
                     self.old_4_image.setPixmap(QtGui.QPixmap(not_available_image))

              ## Categories part
              self.Economy.clicked.connect(lambda: self.open_category("Economy"))
              self.Sport.clicked.connect(lambda: self.open_category("Sport"))
              self.Politics.clicked.connect(lambda: self.open_category("Politics"))
              self.Entertain.clicked.connect(lambda: self.open_category("Entertainment"))
              self.Traffic.clicked.connect(lambda: self.open_category("Traffic"))
              self.Medical.clicked.connect(lambda: self.open_category("Medical"))
              self.SciTech.clicked.connect(lambda: self.open_category("Science & Technology"))    
              self.Travel.clicked.connect(lambda: self.open_category("Travel"))

              self.Economy.setToolTip("Economy")
              self.Sport.setToolTip("Sport")
              self.Politics.setToolTip("Politics")
              self.Entertain.setToolTip("Entertainment")
              self.Traffic.setToolTip("Traffic")
              self.Medical.setToolTip("Medical")
              self.SciTech.setToolTip("Science & Technology")
              self.Travel.setToolTip("Travel")

              self.show()
       def button_menu_action(self, action) -> None:
              if action.text() == "Login":
                     self.openLoginWindow()
              elif action.text() == "Register":
                     self.openRegisterWindow()
              elif action.text() == "Exit":
                     sys.exit()

       def open_category(self, category: str)->None:
              self.stackedWidget.setCurrentWidget(self.category_page)
              self.setWindowTitle("Pirates News - " + category)
              self.list_articles_by_category = db.get_article_by_category(category)
              if self.category_contents.layout() != None:
                     self.delete_widgets(self.category_contents.layout())
                     layout = self.category_contents.layout()
              if self.category_contents.layout() != None:
                     self.delete_widgets(self.category_contents.layout())
                     layout = self.category_contents.layout()
              else:
                     layout = QVBoxLayout(self.category_contents)
              for article in self.list_articles_by_category:
                     card = ArticleCard(article)
                     layout.addWidget(card)
              self.category_scroll_area.setWidgetResizable(True)
              self.category_scroll_area.show()

       


       def delete_widgets(self, layout) -> None:
              for i in reversed(range(layout.count())):
                     layout.itemAt(i).widget().deleteLater()

       def open_article(self, article):
              """
              Open article page to read article
              """
              # change stacked widget to article page and stacked widget is in MainWindow class
              self.stackedWidget.setCurrentWidget(self.article_page)
              self.setWindowTitle("Pirates News - " + article.get_title())
              self.article_title.setText(article.get_title())
              html_content = article.get_content()
              html_content = HTMLParser(html_content)
              images = list()
              if html_content.css_first('img') != None:
                     for image in html_content.css('img'):
                            images.append(image.attributes.get('src'))
              local_images = list()
              article_id = str(article.get_id())
              ## Download to local cache
              iterate = 0
              for image in images:
                     if not os.path.exists("./cache/images/article_" + article_id + "/" + str(iterate) + ".jpg"):
                            if not os.path.exists("./cache/images/article_" + article_id + "/"):
                                   os.makedirs("./cache/images/article_" + article_id + "/")
                            res = requests.get(image)
                            with open("./cache/images/article_" + article_id + "/" + str(iterate) + ".jpg", 'wb') as f:
                                   f.write(res.content)
                            local_images.append("./cache/images/article_" + article_id + "/" + str(iterate) + ".jpg")
                            iterate += 1 
                     else:
                            local_images.append("./cache/images/article_" + article_id + "/" + str(iterate) + ".jpg")

              ## Replace img src with each of local images
              html_content = str(html_content.html)
              if not os.path.exists("./cache/article_" + article_id + ".html"):
                     if not os.path.exists("./cache/"):
                            os.makedirs("./cache/")
                     for i in range(len(images)):
                            img_source = images[i]
                            img_replace = local_images[i]
                            html_content = html_content.replace(img_source, img_replace)
                     with open("./cache/article_" + article_id + ".html", 'w') as f:
                            f.write(html_content)
              article.set_content(open("./cache/article_" + article_id + ".html", 'r').read())
              ## Align image to center
              article.set_content(article.get_content().replace("<img", "<p align='center'><img"))
              article.set_content(article.get_content().replace("</img>", "</img></p>"))
              self.content.setText(article.get_content())
              author = db.get_author_by_id(int(article.get_author()))
              self.author_name.setText("Author: " + author.get("name") + "\nDate: " + article.get_date())

class ArticleCard(QFrame):
       def __init__(self, article: list[dict], parent=None):
              super(ArticleCard, self).__init__()
              loadUi("./views/login/Article_card.ui", self)
              self.article = article
              self.article_title.setText(article['title'])
              self.article_description.setText(article['description'])
              self.article_image.setPixmap(QtGui.QPixmap(not_available_image))
              self.article_image.setScaledContents(True)
              self.article_image.setStyleSheet("border: 1px solid #000000; border-radius: 5px;")
              self.article_image.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
              self.article_image.setContentsMargins(0, 0, 0, 0)
              self.article_image.setWordWrap(False)
              self.setCursor(QtCore.Qt.CursorShape.PointingHandCursor)
              self.mousePressEvent = lambda event: self.open_article()
              self.setMinimumHeight(200)
       
       def open_article(self)->None:
              """
              Open article page to read article
              """
              # change stacked widget to article page and stacked widget is in MainWindow class
              window.stackedWidget.setCurrentWidget(window.article_page)
              window.setWindowTitle("Pirates News - " + self.article['title'])
              window.article_title.setText(self.article['title'])
              html_content = self.article['content']
              html_content = HTMLParser(html_content)
              images = list()
              if html_content.css_first('img') != None:
                     for image in html_content.css('img'):
                            images.append(image.attributes.get('src'))
              local_images = list()
              article_id = str(self.article['_id'])
              ## Download to local cache
              iterate = 0
              for image in images:
                     if not os.path.exists("./cache/images/article_" + article_id + "/" + str(iterate) + ".jpg"):
                            if not os.path.exists("./cache/images/article_" + article_id + "/"):
                                   os.makedirs("./cache/images/article_" + article_id + "/")
                            res = requests.get(image)
                            with open("./cache/images/article_" + article_id + "/" + str(iterate) + ".jpg", 'wb') as f:
                                   f.write(res.content)
                            local_images.append("./cache/images/article_" + article_id + "/" + str(iterate) + ".jpg")
                            iterate += 1 
                     else:
                            local_images.append("./cache/images/article_" + article_id + "/" + str(iterate) + ".jpg")

              ## Replace img src with each of local images
              html_content = str(html_content.html)
              if not os.path.exists("./cache/article_" + article_id + ".html"):
                     if not os.path.exists("./cache/"):
                            os.makedirs("./cache/")
                     for i in range(len(images)):
                            img_source = images[i]
                            img_replace = local_images[i]
                            html_content = html_content.replace(img_source, img_replace)
                     with open("./cache/article_" + article_id + ".html", 'w') as f:
                            f.write(html_content)
              self.article['content'] = open("./cache/article_" + article_id + ".html", 'r').read()
              ## Align image to center
              self.article['content'] = self.article['content'].replace("<img", "<p align='center'><img")
              self.article['content'] = self.article['content'].replace("</img>", "</img></p>")
              window.content.setText(self.article['content'])
              author = db.get_author_by_id(int(self.article['author']))
              window.author_name.setText("Author: " + author.get("name") + "\nDate: " + self.article.get('date'))

class LoginWindow(QDialog):
       def __init__(self):
              super(LoginWindow, self).__init__()
              loadUi("./views/login/login.ui", self)
              self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
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
                     QtCore.QTimer.singleShot(1000, self.close)
                     window.username_label.setText("Hello, " + self.username_input.text())
                     window.username_label.setStyleSheet("border-bottom: 1px solid #000000;")
                     window.menu = QtWidgets.QMenu()
                     window.menu.addAction("Profile")
                     window.menu.addAction("Logout")                
                     window.functional_button.setMenu(window.menu)
                     window.functional_button.setStyleSheet("QPushButton::menu-indicator {image:none;}"
                                                          "QPushButton:pressed::menu-inidcator{image:none;}"
                                                          "QPushButton:pressed{border: none}"
                                                          "QPushButton{background-color: #ffffff; border-image: url(./views/assets/icons/user.png); border-radius: 50%; padding: 5px, border: 1px solid #000000;}")

                     window.functional_button.menu().setStyleSheet("QMenu::item {background-color: transparent; padding: 5px; color: #000000;} "
                                                "QMenu::item:selected {background-color: #000000; color: #ffffff;}"
                                                "QMenu::item:pressed {background-color: #000000; color: #ffffff;} "
                                                "QMenu{background-color: #ffffff; border: 1px solid #000000; border-radius: 5px; padding: 5px; margin: 0px; font-size: 12px; font-family: 'Segoe UI';}")

                     window.functional_button.menu().setCursor(QtCore.Qt.CursorShape.PointingHandCursor)

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
                     if state == False:
                            self.status_label.setStyleSheet("color: #ff0000;")
                            self.status_label.setText("Username or email already exists")
                     else:
                            self.status_label.setText("Register successful")
                            QtCore.QTimer.singleShot(1000, self.close)
                     


if __name__ == "__main__":
       ## StackWidget
       app = QtWidgets.QApplication(sys.argv)
       window = MainWindow()
       try: 
           sys.exit(app.exec(), shutil.rmtree("./cache"))
       except TypeError:
           print("Exited")
       except FileNotFoundError:
           print("Exited")
