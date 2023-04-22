import datetime
import os
import sys

from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QDialog, QApplication, QMessageBox
from PyQt6.uic import loadUi

from controller.newspaper import Newspapers

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
news = Newspapers()
add_article_callback = news.add_article


class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi(os.path.abspath("./views/add_articles.ui"), self)
        if not os.path.exists("./cache/state.json"):
            QMessageBox.warning(self, "Error", "Please login first!")
            return self.close()

        self.setWindowTitle("Pirate News - Add Article")
        # If not focus on the text edit, the paste action will not work
        if self.content_edit.hasFocus():
            # Paste image from clipboard
            self.clipboard = QApplication.clipboard()
            self.clipboard.dataChanged.connect(self.handle_clipboard_change)

        paste_action = QAction("Paste", self)
        paste_action.triggered.connect(self.paste_image)
        self.addAction(paste_action)

        # Buttons
        self.confirm_button.accepted.connect(self.accept_event)
        self.confirm_button.rejected.connect(self.reject_event)

    def handle_clipboard_change(self):
        if self.clipboard.mimeData().hasImage():
            self.paste_image()

    def paste_image(self):
        if self.clipboard.mimeData().hasImage():
            image = self.clipboard.image()
            cursor = self.text_edit.textCursor()
            cursor.insertImage(image)

    def accept_event(self) -> None:
        if not os.path.exists("./cache/state.json"):
            QMessageBox.warning(self, "Error", "Please login first!")
            return
        if self.title_edit.toPlainText() == "":
            QMessageBox.warning(self, "Error", "Please enter a title!")
            return
        if self.description_edit.toPlainText() == "":
            QMessageBox.warning(self, "Error", "Please enter a description!")
            return
        if self.content_edit.toPlainText() == "":
            QMessageBox.warning(self, "Error", "Please enter content!")
            return

        add_article_callback(date=str(datetime.datetime.today().strftime('%m-%d-%Y')),
                             title=self.title_edit.toPlainText(), overview=self.description_edit.toPlainText(),
                             content=self.content_edit.toHtml(), category=self.category_edit.currentText(),
                             preview_img=self.image_link.toPlainText())
        QMessageBox.information(self, "Success", "Article added successfully!")
        self.title_edit.setPlainText("")
        self.description_edit.setPlainText("")
        self.content_edit.setText("")
        self.category_edit.setCurrentIndex(0)
        self.image_link.setPlainText("")

    def reject_event(self) -> None:
        self.close()
