# This Python file uses the following encoding: utf-8

import sys, os



from PySide6.QtWidgets import QMainWindow
from PyQt6 import QtWidgets




# Important:

# You need to run the following command to generate the ui_form.py file

#     pyside6-uic form.ui -o ui_form.py, or

#     pyside2-uic form.ui -o ui_form.py

from interface import Interface



class MainWindow(QMainWindow):

    def __init__(self, parent=None):

        super().__init__(parent)

        self.ui = Interface()

        self.ui.setupUi(self)





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Interface()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())

