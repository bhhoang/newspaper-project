import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QFileDialog
from PyQt6.QtGui import QClipboard, QAction

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.clipboard = QApplication.clipboard()
        self.clipboard.dataChanged.connect(self.handle_clipboard_change)

        self.text_edit = QTextEdit()
        self.setCentralWidget(self.text_edit)
        save_action = QAction("Save", self)
        save_action.setShortcut("Ctrl+S")
        save_action.triggered.connect(self.save_text)
        self.addAction(save_action)

    def save_text(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt)")
        if file_name:
            with open(file_name, "w", encoding="utf-8") as f:
                f.write(self.text_edit.toHtml())

    def handle_clipboard_change(self):
        if self.clipboard.mimeData().hasImage():
            self.paste_image()

    def paste_image(self):
        if self.clipboard.mimeData().hasImage():
            image = self.clipboard.image()
            cursor = self.text_edit.textCursor()
            cursor.insertImage(image)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())