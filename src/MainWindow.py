# -*- coding: utf-8 -*-

from PyQt4.QtGui import QMainWindow, QPushButton
from ui.MainWindow import Ui_MainWindow
from Game import Game

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)

        # user interface configuration.
        self.setupUi(self)

        # Hide some stuff
        self.pushButton_moreOptions.setChecked(False)

        self.loadGame()

        # Display
        self.show()

    def loadGame(self):
        self.game = Game()
        self.setCentralWidget(self.game)


