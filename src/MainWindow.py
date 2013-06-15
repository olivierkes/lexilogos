# -*- coding: utf-8 -*-

from PyQt4.QtGui import QMainWindow
from ui.Ui_MainWindow import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)

        # user interface configuration.
        self.setupUi(self)

        # Hide some stuff
        self.pushButton_moreOptions.setChecked(False)
        self.pushButton_cheatText.setChecked(False)


        # Display
        self.show()

