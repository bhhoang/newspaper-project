import json

from PyQt6 import QtGui
from PyQt6.QtWidgets import QDialog, QMessageBox, QVBoxLayout, QFrame
from PyQt6.uic import loadUi

from model.dbquery import Database
from utils.get_preview_image import getimage_and_setname

db = Database()


class DeleteConfirm(QMessageBox):
    def __init__(self):
        super(DeleteConfirm, self).__init__()
        self.setWindowTitle("Confirmation")
        self.setText("Are you sure you want to delete the selected articles?")
        self.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        self.setDefaultButton(QMessageBox.StandardButton.No)


class DeleteArticleCard(QFrame):
    def __init__(self, article):
        super(DeleteArticleCard, self).__init__()
        loadUi("./views/articledel_card.ui", self)
        self.article = article
        self.title.setText(self.article['title'])
        self.description.setText(self.article['description'])
        self.image.setPixmap(QtGui.QPixmap(getimage_and_setname(self.article['preview_img'], self.article['_id'])))


class DeleteArticle(QDialog):
    def __init__(self):
        super(DeleteArticle, self).__init__()
        loadUi('./views/delete_articles.ui', self)

        # Connect signals and slots
        self.confirm_button.accepted.connect(self.submit)
        self.confirm_button.rejected.connect(self.reject)
        self.state = json.loads(open("./cache/state.json", 'r').read())
        self.articles_author = db.get_articles_by_author_id(self.state.get("id"))
        if self.articles_list.layout() != None:
            layout = self.articles_list.layout()
        else:
            layout = QVBoxLayout(self.articles_list)
        for article in self.articles_author:
            article_card = DeleteArticleCard(article)
            layout.addWidget(article_card)
        self.articles_list.setLayout(layout)

    def submit(self):
        chosen = False
        for i in reversed(range(self.articles_list.layout().count())):
            if self.articles_list.layout().itemAt(i).widget().choosing_checkbox.isChecked():
                chosen = True
                state = json.loads(open("./cache/state.json", 'r').read())
                db._delete_article(self.articles_list.layout().itemAt(i).widget().article)
                db.remove_article_from_author(state.get("id"),
                                              self.articles_list.layout().itemAt(i).widget().article["_id"])
                self.articles_list.layout().itemAt(i).widget().deleteLater()
        if chosen:
            QMessageBox.information(self, "Success", "Article deleted successfully!")
            return
        else:
            QMessageBox.warning(self, "Error", "Please select atleast an article to delete!")
            return

    def update_views(self):
        self.articles_author = db.get_articles_by_author_id(self.state.get("id"))
        if self.articles_list.layout() != None:
            layout = self.articles_list.layout()
        else:
            layout = QVBoxLayout(self.articles_list)
        for i in reversed(range(self.articles_list.layout().count())):
            self.articles_list.layout().itemAt(i).widget().deleteLater()
        for article in self.articles_author:
            article_card = DeleteArticleCard(article)
            layout.addWidget(article_card)
        self.articles_list.show()

    def reject(self):
        self.close()
