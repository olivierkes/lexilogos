# -*- coding: utf-8 -*-

from PyQt4.QtGui import QWidget
from ui.Game import Ui_Game
import Game

class Game(QWidget, Ui_Game):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        Ui_Game.__init__(self)

        # user interface configuration.
        self.setupUi(self)

        #Hide some stuff
        self.pushButton_cheatText.setChecked(False)