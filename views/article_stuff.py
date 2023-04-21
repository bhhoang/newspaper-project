from PyQt6.QtWidgets import QDialog, QFrame, QVBoxLayout
from PyQt6 import QtGui
from PyQt6.uic import loadUi
from views.add_articles import MainWindow as AddArticleWindow
from views.delete_articles import DeleteArticle as DeleteArticleWindow
from utils.get_preview_image import getimage_and_setname

import json

class AricleCardManager(QFrame):
       def __init__(self, article):
              super(AricleCardManager, self).__init__()
              loadUi("./views/article_mgmt_card.ui", self)
              self.article = article
              self.title.setText(self.article['title'])
              self.description.setText(self.article['description'])
              self.image.setPixmap(QtGui.QPixmap(getimage_and_setname(self.article['preview_img'], self.article['_id'])))
              self.image.setScaledContents(True)

class DeleteArticleCard(QFrame):
       def __init__(self, article, db):
              super(DeleteArticleCard, self).__init__()
              loadUi("./views/articledel_card.ui", self)
              self.article = article
              self.title.setText(self.article['title'])
              self.description.setText(self.article['description'])
              self.image.setPixmap(QtGui.QPixmap(getimage_and_setname(self.article['preview_img'], self.article['_id'])))
              self.image.setScaledContents(True)
              self.confirm_button.accepted.connect(lambda: self.delete_article(db))
              self.confirm_button.rejected.connect(self.close)
       def delete_article(self, db):
              db.delete_article(self.article['_id'])
              self.close()


class ArticleManager(QDialog):
       def open_AddArticle(self, news):
              self.add_article_window = AddArticleWindow(news.add_article)
              self.add_article_window.show()
       
       def open_DeleteArticle(self):
              self.delete_article_window = DeleteArticleWindow()
              self.delete_article_window.show()

       def __init__(self, news, db):
              super(ArticleManager, self).__init__()
              loadUi("./views/article_management.ui", self)
              self.add_articles_button.clicked.connect(lambda: self.open_AddArticle(news))
              self.delete_articles_button.clicked.connect(self.open_DeleteArticle)
              state = json.loads(open("./cache/state.json", 'r').read())
              self.articles_author = db.get_articles_by_author_id(state.get("id"))
              if self.articles_list.layout() != None:
                     layout = self.articles_list.layout()
              else:
                     layout = QVBoxLayout(self.articles_list)
              for article in self.articles_author:
                     layout.addWidget(AricleCardManager(article))
              
              self.articles_display.show()