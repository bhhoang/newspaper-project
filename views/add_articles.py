from PyQt6.uic import loadUi 
from PyQt6.QtWidgets import QDialog, QApplication, QTextEdit, QDialogButtonBox, QMessageBox
from PyQt6 import QtGui
from PyQt6.QtGui import QClipboard, QAction
import os,sys
import datetime
from ..controller.newspaper import Newspapers
news = Newspapers()

class MainWindow(QDialog):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        print(os.path.abspath("add_articles.ui"))
        loadUi(os.path.abspath("add_articles.ui"), self)
        self.show()
        
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
        #news.add_article(self.title_edit.toPlainText(), self.description_edit.toPlainText(), self.content_edit.toHtml(), self.category_edit.currentText())
        print(datetime.datetime.today().strftime('%m-%d-%Y'))
    
    def reject(self) -> None:
        sys.exit()
    
if __name__ == '__main__':

    app = QApplication(sys.argv)
    app.setApplicationName("Pirate News")
    window = MainWindow()
    sys.exit(app.exec())