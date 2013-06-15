# -*- coding: utf-8 -*-

from PyQt4.QtGui import QMainWindow, QPushButton
from ui.MainWindow import Ui_MainWindow
from Game import Game
from BibleLoader import BibleLoader

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)

        # user interface configuration.
        self.setupUi(self)


        # Hide some stuff
        self.pushButton_moreOptions.setChecked(False)

        # Loads Bible
        self.BibleLoader = BibleLoader("BP05FNL")

        # Signal / Slots connections
        self.comboBox_book.currentIndexChanged.connect(self.populatesChapter)
        self.comboBox_chapter.currentIndexChanged.connect(self.populatesVerseFrom)
        self.comboBox_verseFrom.currentIndexChanged.connect(self.populatesVerseTo)
        self.pushButton_Start.clicked.connect(self.startGame)

        # Initalisation
        self.populatesBook()

        # Display
        self.show()
        self.dockWidget_settings.setMaximumWidth(self.dockWidget_settings.width())

    def startGame(self):
        #Creates and sets the central widget

        self.game = Game(self.comboBox_book.currentIndex(),
                         self.comboBox_chapter.currentIndex(),
                         self.comboBox_verseFrom.currentIndex(),
                         self.comboBox_verseFrom.currentIndex() +
                                         self.comboBox_verseTo.currentIndex(),
                         self)
        self.setCentralWidget(self.game)




    def populatesBook(self):
        "Populates the combobox with the NT books names."
        bookList = ["Matthew", "Mark", "Luke", "John", "Acts", "Romans",
                "1 Corinthians", "2 Corinthians", "Galatians", "Ephesians",
                "Philippians", "Colossians", "1 Thessalonians",
                "2 Thessalonians", "1 Timothy", "2 Timothy", "Titus",
                "Philemon", "Hebrews", "James", "1 Peter", "2 Peter", "1 John",
                "2 John", "3 John", "Jude", "Revelation"]

        for i in bookList:
            self.comboBox_book.addItem(i)

    def populatesChapter(self, bookNumber):
        self.comboBox_chapter.clear()
        for i in range(self.BibleLoader.chapterNumber(bookNumber)):
            self.comboBox_chapter.addItem(str(i + 1))

    def populatesVerseFrom(self, chapterNumber):
        self.comboBox_verseFrom.clear()
        for i in range(self.BibleLoader.verseNumber(self.comboBox_book.currentIndex(), chapterNumber)):
            self.comboBox_verseFrom.addItem(str(i + 1))


    def populatesVerseTo(self, verseNumber):
        self.comboBox_verseTo.clear()
        for i in range(verseNumber, self.BibleLoader.verseNumber(self.comboBox_book.currentIndex(), self.comboBox_chapter.currentIndex())):
            self.comboBox_verseTo.addItem(str(i + 1))

