from PyQt6.uic import loadUi 
from PyQt6.QtWidgets import QDialog, QApplication, QTextEdit, QDialogButtonBox, QMessageBox
from PyQt6 import QtGui
from PyQt6.QtGui import QClipboard, QAction
import os,sys
import datetime
import json
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from controller.newspaper import Newspapers

news = Newspapers()
class MainWindow(QDialog):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        loadUi(os.path.abspath("./views/add_articles.ui"), self)
        self.show()
        if not os.path.exists("./cache/state.json"):
            QMessageBox.warning(self, "Error", "Please login first!")
            return self.close()
        
        self.setWindowTitle("Pirate News - Add Article")
        #Paste image from clipboard
        self.clipboard = QApplication.clipboard()
        self.clipboard.dataChanged.connect(self.handle_clipboard_change)

        paste_action = QAction("Paste", self)
        paste_action.triggered.connect(self.paste_image)
        self.addAction(paste_action)

        #Buttons
        self.confirm_button.accepted.connect(self.accept)
        self.confirm_button.rejected.connect(self.reject)

    def handle_clipboard_change(self):
        if self.clipboard.mimeData().hasImage():
            self.paste_image()

    def paste_image(self):
        if self.clipboard.mimeData().hasImage():
            image = self.clipboard.image()
            cursor = self.text_edit.textCursor()
            cursor.insertImage(image)

    def accept(self) -> None:
        if not os.path.exists("./cache/state.json"):
            QMessageBox.warning(self, "Error", "Please login first!")
            return
        state = json.load(open("./cache/state.json", "r"))
        news.login(state["username"], state["password"])
        news.add_article(date=str(datetime.datetime.today().strftime('%m-%d-%Y')), title=self.title_edit.toPlainText(), overview=self.description_edit.toPlainText(), content=self.content_edit.toHtml(), category=self.category_edit.currentText(), preview_img=self.image_link.toPlainText())
        QMessageBox.information(self, "Success", "Article added successfully!")
    
    def reject(self) -> None:
        sys.exit()
    
if __name__ == '__main__':

    app = QApplication(sys.argv)
    app.setApplicationName("Pirate News")
    window = MainWindow()
    sys.exit(app.exec())