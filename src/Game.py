# -*- coding: utf-8 -*-

from PyQt4.QtGui import QWidget, QSyntaxHighlighter, QTextCharFormat, QFont, \
                        QColor
from PyQt4.QtCore import QTime, Qt
from ui.Game import Ui_Game
#import Game
from StrongParser import StrongParser


class myHighlighter(QSyntaxHighlighter):
    "Simple highlighter for the QPlainTextEdit."

    def __init__(self, editor, game):
        "Initialises the highlighter. Needs the 'game' it is used in."
        QSyntaxHighlighter.__init__(self, editor.document())
        self._game = game

    def highlightBlock(self, text):
        "Highlights in the text the word selected in the list."

        # Do we have a word selected in the list?
        # TODO: maybe we should do that only if we are displaying the specifical
        #       form, and not the lexicon one, because it won't work and it
        #       helps too much.
        if not self._game._testLexicalForm:
            s = self._game.listWidget_original.selectedItems()
            if len(s) > 0:
                word = s[0].text()
                pos = text.find(word)
                f = QTextCharFormat()
                f.setFontWeight(QFont.Bold)
                f.setForeground(QColor(Qt.darkRed))

                while pos >= 0:
                    # We get sure we are not simply highlighting within a word
                    if text[pos - 1: pos] == " " and \
                       text[pos + len(word):pos + len(word) + 1] == " " or \
                       pos == 0 or pos + len(word) == len(text):
                        self.setFormat(pos, len(word), f)
                    pos = text.find(word, pos + 1)


class Game(QWidget, Ui_Game):
    """
    Contains everything concerning the game, i.e. gessing the definition of a
    word while reading the context in which it occurs.
    """
    def __init__(self, book=10, chapter=1, verseFrom=6, verseTo=6, parent=None):
        "Initialises a Game given a book, a chapter, and the verses."
        QWidget.__init__(self)
        Ui_Game.__init__(self)

        # User interface configuration.
        self.setupUi(self)

        # Hide some stuff
        self.pushButton_cheatText.setChecked(False)

        # Strong Parser
        self.StrongParser = StrongParser()
        self._highlighter = myHighlighter(self.plainTextEdit_original, self)

        # Settings
        self._book = book
        self._chapter = chapter
        self._verseFrom = verseFrom
        self._verseTo = verseTo
        self.BibleLoader = parent.BibleLoader
        self._startTime = QTime.currentTime()
        self._testLexicalForm = parent.comboBox_testLexicalForm.currentIndex()\
                                == 1

        # Internal lists
        self._words = []          # Words as in the text
        self._lexicals = []       # Lexical form of the word
        self._strongs = []        # Strong number
        self._definitions = []    # Definition
        self._grammars = []       # Grammatical informations
        self._wordsGuessed = []   # Words already guessed

        # Signal / Slots
        self.listWidget_original.itemSelectionChanged\
                                .connect(self._highlighter.rehighlight)
        self.plainTextEdit_original.cursorPositionChanged\
                                   .connect(self.textSelectionChanged)

        # While debugging
        self.listWidget_original.setSortingEnabled(False)
        self.listWidget_translation.setSortingEnabled(False)

        # Get the party going
        self.loadText()

    def textSelectionChanged(self):
        """
        This to do when the user clicks on the text.
        """
        # Finds the selected text
        c = self.plainTextEdit_original.textCursor()
        if len(c.selectedText()) == 0:
            c.movePosition(c.StartOfWord, c.MoveAnchor)
            c.movePosition(c.EndOfWord, c.KeepAnchor)
        # If it is a word in the list, selects it
        r = self.listWidget_original.findItems(c.selectedText(),
                                               Qt.MatchExactly)
        if len(r) > 0:
            self.listWidget_original.setCurrentItem(r[0])

        #self.plainTextEdit_original.setTextCursor(c)

    def loadText(self):
        """
        Loads the biblical verses on the basis of self settings (_verseFrom and
        _verseTo). Displays the text, populates the lists.
        """

        # Gets the biblical text in 'text'
        text = []
        t = ""
        for i in range(self._verseFrom, self._verseTo + 1):
            v = self.BibleLoader.getParsedVerse(self._book, self._chapter, i)
            t += self.BibleLoader.getVerseTextOnly(self._book, self._chapter,
                                                   i) + " "
            text += v

        # Removes doubles. Either in one list or the other, according to
        # the setting (displaying the specifical form, or the lexicon form)
        for (w, s, g) in text:
            if not self._testLexicalForm and not w in self._words:
                self._words.append(w)
                self._strongs.append(s)
                self._grammars.append(g)
            elif self._testLexicalForm and not s in self._strongs:
                self._words.append(w)
                self._strongs.append(s)
                self._grammars.append(g)

        for i in self._strongs:
            u = self.StrongParser.getGreekUnicode(int(i))
            self._lexicals.append(u)

        self.plainTextEdit_original.setPlainText(t)
        self.populateListOriginal()
        self.populateListTranslation()

    def populateListOriginal(self):
        """
        Populates the list of words to be translated, on the basis of internal
        informations, i.e. self._words.
        """
        self.listWidget_original.clear()

        if self._testLexicalForm:
            theList = self._lexical
        else:
            theList = self._words

        for i in theList:
            if i not in self._wordsGuessed:
                self.listWidget_original.addItem(str(i))

    def populateListTranslation(self):
        """
        Populates the definitions, on the basis of internal informations,
        i.e. self._strongs.
        """
        self.listWidget_translation.clear()
        for i in self._strongs:
            if i not in self._wordsGuessed:
                d = self.StrongParser.getKJVDefinition(int(i))
                self.listWidget_translation.addItem(d)
