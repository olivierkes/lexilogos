# -*- coding: utf-8 -*-

from PyQt4.QtGui import QWidget
from PyQt4.QtCore import QTime
from ui.Game import Ui_Game
import Game

class Game(QWidget, Ui_Game):

    def __init__(self, book=10, chapter=1, verseFrom=6, verseTo=6, parent=None):
        QWidget.__init__(self)
        Ui_Game.__init__(self)

        # user interface configuration.
        self.setupUi(self)

        #Hide some stuff
        self.pushButton_cheatText.setChecked(False)

        # Initialise var
        self._book = book
        self._chapter = chapter
        self._verseFrom = verseFrom
        self._verseTo = verseTo
        self.BibleLoader = parent.BibleLoader
        self._startTime = QTime.currentTime()

        self.loadText()


    def loadText(self):
        t = ""
        for i in range(self._verseFrom, self._verseTo + 1):
            print(self._verseFrom, self._verseTo + 1)
            t += self.BibleLoader.getVerse(self._book, self._chapter, i) + "\n"

        self.plainTextEdit_original.setPlainText(t)
