from PyQt6.QtWidgets import QDialog, QFrame, QVBoxLayout
from PyQt6 import QtGui
from PyQt6.uic import loadUi
from views.add_articles import MainWindow as AddArticleWindow
from views.delete_articles import DeleteArticle as DeleteArticleWindow
from utils.get_preview_image import getimage_and_setname
from controller.newspaper import Newspapers
from model.dbquery import Database
import json

news = Newspapers()
db = Database()
class ArticleCardManager(QFrame):
    def __init__(self, article):
        super(ArticleCardManager, self).__init__()
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
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(ArticleManager, cls).__new__(cls)
        else:
            cls.instance.update_articles()
        return cls.instance
    
    def open_AddArticle(self):
        self.add_article_window.show()
        self.add_article_window.confirm_button.accepted.connect(self.update_articles)
        self.add_article_window.confirm_button.rejected.connect(self.add_article_window.hide)

    def open_DeleteArticle(self):
        self.delete_article_window.show()
        self.delete_article_window.confirm_button.accepted.connect(self.update_articles)
        self.delete_article_window.confirm_button.rejected.connect(self.delete_article_window.hide)

    def __init__(self):
        super(ArticleManager, self).__init__()
        loadUi("./views/article_management.ui", self)
        self.db = db
        self.add_article_window = AddArticleWindow()
        self.delete_article_window = DeleteArticleWindow()
        self.add_articles_button.clicked.connect(self.open_AddArticle)
        self.delete_articles_button.clicked.connect(self.open_DeleteArticle)
        self.state = json.loads(open("./cache/state.json", 'r').read())
        self.articles_author = db.get_articles_by_author_id(self.state.get("id"))
        if self.articles_list.layout() is not None:
            layout = self.articles_list.layout()
        else:
            layout = QVBoxLayout(self.articles_list)
        for article in self.articles_author:
            layout.addWidget(ArticleCardManager(article))
        self.articles_display.show()

    def update_articles(self):
        self.articles_author = self.db.get_articles_by_author_id(self.state.get("id"))
        if self.articles_list.layout() is not None:
            layout = self.articles_list.layout()
        else:
            layout = QVBoxLayout(self.articles_list)
        for i in reversed(range(layout.count())):
            layout.itemAt(i).widget().deleteLater()
        for article in self.articles_author:
            layout.addWidget(ArticleCardManager(article))
        self.articles_display.show()
        self.delete_article_window.update_views()
