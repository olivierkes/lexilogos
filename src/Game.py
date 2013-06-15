# -*- coding: utf-8 -*-

from PyQt4.QtGui import QWidget, QSyntaxHighlighter, QTextCharFormat, QFont, \
                        QColor
from PyQt4.QtCore import QTime, Qt
from ui.Game import Ui_Game
import Game

class myHighlighter(QSyntaxHighlighter):

    def __init__(self, editor, game):
        QSyntaxHighlighter.__init__(self, editor.document())
        self._game = game

    def highlightBlock(self, text):
        s = self._game.listWidget_original.selectedItems()

        if len(s) > 0:
            word = s[0].text()

            pos = text.find(word)
            f = QTextCharFormat()
            f.setFontWeight(QFont.Bold)
            f.setForeground(QColor(Qt.darkRed))

            while pos >= 0:
                self.setFormat(pos, len(word), f)
                pos = text.find(word, pos + 1)


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
        self._wordsGuessed = []

        self._highlighter = myHighlighter(self.plainTextEdit_original, self)

        # Signal / Slots
        self.listWidget_original.itemSelectionChanged.connect(self._highlighter.rehighlight)
        self.plainTextEdit_original.cursorPositionChanged.connect(self.textSelectionChanged)

        self.loadText()

    def textSelectionChanged(self):
        c = self.plainTextEdit_original.textCursor()
        if len(c.selectedText()) == 0:
            c.movePosition(c.StartOfWord, c.MoveAnchor)
            c.movePosition(c.EndOfWord, c.KeepAnchor)

        r = self.listWidget_original.findItems(c.selectedText(), Qt.MatchExactly)
        if len(r) > 0:
            self.listWidget_original.setCurrentItem(r[0])


        #self.plainTextEdit_original.setTextCursor(c)

    def loadText(self):
        text = []
        t = ""
        for i in range(self._verseFrom, self._verseTo + 1):
            v = self.BibleLoader.parseVerse(self._book, self._chapter, i)
            t += self.BibleLoader.getVerseTextOnly(self._book, self._chapter, i)
            text += v

        print(text)

        #TODO: enlever les doublons

        self._words = [w for (w, s, g) in text]
        self._strongs = [s for (w, s, g) in text]
        self._grammars = [g for (w, s, g) in text]

        self.plainTextEdit_original.setPlainText(t)
        self.populateListOriginal()
        self.populateListTranslation()

    def populateListOriginal(self):
        self.listWidget_original.clear()
        for i in self._words:
            if i not in self._wordsGuessed:
                self.listWidget_original.addItem(str(i))

    def populateListTranslation(self):
        self.listWidget_translation.clear()
        for i in self._strongs:
            if i not in self._wordsGuessed:
                self.listWidget_translation.addItem(str(i))
