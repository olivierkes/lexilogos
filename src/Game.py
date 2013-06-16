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

        # Marks the words already guessed
        f = QTextCharFormat()
        f.setForeground(QColor(Qt.lightGray))
        for (i, j) in self._game._alreadyGuessed:
            word = self._game._words[i]
            pos = text.find(word)
            while pos >= 0:
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
        self._words = []            # Words as in the text
        self._lexicals = []         # Lexical form of the word
        self._strongs = []          # Strong number
        self._definitions = []      # Definition
        self._grammars = []         # Grammatical informations
        self._alreadyGuessed = []   # list of words ID already guessed

        # Signal / Slots
        self.listWidget_original.itemSelectionChanged\
                                .connect(self._highlighter.rehighlight)
        self.listWidget_original.itemDoubleClicked.connect(self.guessOnList)
        self.listWidget_translation.itemDoubleClicked.connect(self.guessOnList)
        self.listWidget_guesses.itemDoubleClicked.connect(self.undoGuess)
        self.pushButton_guess.clicked.connect(self.testGuess)
        self.pushButton_undoGuess.clicked.connect(self.undoGuess)
        self.plainTextEdit_original.cursorPositionChanged\
                                   .connect(self.textSelectionChanged)
        self.pushButton_Validate.clicked.connect(self.validate)

        # While debugging
        self.listWidget_original.setSortingEnabled(False)
        self.listWidget_translation.setSortingEnabled(False)

        # Get the party going
        self.loadText()

    def validate(self):
        "The user is happy with his or her guess and wants the solution."
        #TODO

    def testGuess(self):
        "We test if the guess is valid, i.e. if both rows are selected."
        i = self.listWidget_original.currentRow()
        j = self.listWidget_translation.currentRow()

        if i != -1 and j != -1:
            self.guess(i, j)

    def undoGuess(self, item=None):
        "The user wants to undo a guess."
        i = self.listWidget_guesses.currentRow()
        if i != -1:
            self._alreadyGuessed.pop(i)
            self.populateLists()

    def guessOnList(self, item):
        "The user made a guess by double-clicking on a list."
        self.testGuess()

    def guess(self, i, j):
        """The user guessed that item number 'i' in the first list is item 'j'
        in the second one."""
        itemI = self.listWidget_original.item(i).text()
        itemJ = self.listWidget_translation.item(j).text()

        IDi = self.toID(itemI)
        IDj = self.toID(itemJ)

        self._alreadyGuessed.append((IDi, IDj))

        # Makes it visible to the user
        self.populateLists()

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

        # Generate _lexicals (lexical forms of words)
        for i in self._strongs:
            u = self.StrongParser.getGreekUnicode(int(i))
            self._lexicals.append(u)

        # Generate _definitions (definitions of words)
        for i in self._strongs:
            d = self.StrongParser.getKJVDefinition(int(i))
            self._definitions.append(d)

        # Makes it all visible to the user
        self.plainTextEdit_original.setPlainText(t)
        self.populateLists()

    def populateLists(self):
        "Populates all lists."
        self.populateListOriginal()
        self.populateListTranslation()
        self.populateListGuesses()
        self._highlighter.rehighlight()

    def populateListOriginal(self):
        """
        Populates the list of words to be translated, on the basis of internal
        informations, i.e. self._words.
        """
        self.listWidget_original.clear()

        if self._testLexicalForm:
            theList = self._lexicals
        else:
            theList = self._words

        for i in theList:
            if not self.alreadyGuessedWord(self.toID(i)):
                self.listWidget_original.addItem(str(i))

    def populateListTranslation(self):
        """
        Populates the definitions, on the basis of internal informations,
        i.e. self._strongs.
        """
        self.listWidget_translation.clear()
        for i in self._definitions:
            if not self.alreadyGuessedDefinition(self.toID(i)):
                self.listWidget_translation.addItem(i)

    def populateListGuesses(self):
        "Populates the list of guesses already made."
        self.listWidget_guesses.clear()
        for (i, j) in self._alreadyGuessed:
            if self._testLexicalForm:
                t1 = self._lexicals[i]
            else:
                t1 = self._words[i]
            t2 = self._definitions[j]
            self.listWidget_guesses.addItem(t1 + " → " + t2)

    def toID(self, text):
        "Returns the ID (i.e. the position) of the given word."
        if text in self._words:
            return self._words.index(text)
        elif text in self._lexicals:
            return self._lexicals.index(text)
        elif text in self._strongs:
            return self._strongs.index(text)
        elif text in self._definitions:
            return self._definitions.index(text)
        else:
            return -1

    def alreadyGuessedWord(self, ID):
        """Returns TRUE if the word whose ID has been given has already been
        used."""
        for (i, j) in self._alreadyGuessed:
            if i == ID:
                return True
        return False

    def alreadyGuessedDefinition(self, ID):
        """Returns TRUE if the definition whose ID has been given has already
        been used."""
        for (i, j) in self._alreadyGuessed:
            if j == ID:
                return True
        return False
