# -*- coding: utf-8 -*-

import os
from PyQt4.QtCore import QRegExp

#TODO: traduction


class BibleLoader():
    """
    This class is used to load a Bible, and query some verse, or statistics.
    """

    def __init__(self, bible, trad=False):
        """Initialization.
        'Bible' must be the name of the folder in which the Bible is stored.
        If loading a traduction and not the original text, use 'trad=True',
        because the files are stored in a different folder."""

        self._bible = bible
        self._books = [0] * 27
        self._trad = trad
        self.loadBible()

    def loadBible(self):
        "Loads the Bible from files on disk."
        if self._trad:
            prefix = "../trad/"
        else:
            prefix = "../mss/"

        # Try listing the given directory
        try:
            files = os.listdir(prefix + self._bible)
        except FileNotFoundError:
            print("Please do not enter an imaginary bible.")
            return

        # Read each file, identify the book number, and parse the book.
        for i in files:
            f = open(prefix + self._bible + "/" + i, 'r')
            book = f.read()
            f.close()
            bookNumber = self.bookcodeToIndex(i)
            self._books[bookNumber] = self.parseBook(book)

    def parseBook(self, book):
        """
        Takes a raw book and returns an array of array of array such as:
        [0][0][0] = Mt 1, 1
        [1][8][4] = Mr 9, 5
        i.e. [bookNumber][chapter][verse]
        Note that chapter and verse start from 0.
        etc.
        """
        result = []
        line = book.split("\n")

        # Puts each verse on one line
        verse = []
        v = ""
        for l in line:
            if l[0:5] == "     ":
                if v: verse.append(v)
                v = l[5:]
            else:
                v += " " + l
        if v: verse.append(v)

        r = QRegExp(r'(\d+):(\d+)\s*(.*)')
        chapter = []
        for v in verse:
            pos = r.indexIn(v)
            chap = int(r.cap(1))
            ver = int(r.cap(2))
            text = r.cap(3).strip()
            if ver == 1:
                if len(chapter) > 0: result.append(chapter)
                chapter = [text]
            else:
                chapter.append(text)
        if len(chapter) > 0: result.append(chapter)

        return result

    def parse(self, text):
        """
        Parse some text, assuming it is in the form of:
            word 1414 {grammar} word 1414 {grammar} etc.
        and returns a list of tupples '(word, strong, grammar)'.
        """
        result = []
        r = QRegExp(r'([αβχδεφγηιϕκλμνοπθρστυςωξψζ]*)' +
                     '\s*' +
                     '([\d ]+)' +
                     '\s*' +
                     '\{(.*)\}\s*')
        r.setMinimal(True)
        pos = r.indexIn(text)
        while pos >= 0:
            # Some verbs have two strong numbers, we keep only the first,
            # the second one being grammar
            strong = r.cap(2).strip()
            if " " in strong:
                strong = strong.split(" ")[0]
            result.append((r.cap(1).strip(),
                           strong,
                           r.cap(3).strip()))
            pos = r.indexIn(text, pos + len(r.cap(0)))
        return result

    def bookcodeToIndex(self, bookcode):
        """
        Returns the index of the given bookcode.
        Exemple: "MT" or "MT.BP5" returns 0 (first book of the NT)
        """
        bookorder = ["MT", "MR", "LU", "JOH", "AC", "RO", "1CO", "2CO", "GA",
                     "EPH", "COL", "PHP", "1TH", "2TH", "1TI", "2TI", "TIT",
                     "PHM", "HEB", "JAS", "1PE", "2PE", "1JO", "2JO", "3JO",
                     "JUDE", "RE"]

        for i in bookorder:
            if i in bookcode:
                return bookorder.index(i)

        print("ERROR: the bookcode is invalid.")

    def setBible(self, bible):
        "Change the Bible. Not sure it works just like that."
        self._bible = bible
        self.loadBible()

###############################################################################
# Query Functions
###############################################################################

    def getVerseTextOnly(self, bookNumber, chapterNumber, verseNumber):
        "Returns the verse, but only the text as string."
        v = self.getVerse(bookNumber, chapterNumber, verseNumber)
        return " ".join([i[0] for i in self.parse(v)])

    def getBook(self, bookNumber):
        "Returns a book (as array of array, chapter and verse)"
        return self._books[bookNumber]

    def getChapter(self, bookNumber, chapterNumber):
        "Returns a chapter (as array of verse)."
        return self._books[bookNumber][chapterNumber]

    def getVerse(self, bookNumber, chapterNumber, verseNumber):
        "Returns a verse, as string. With codes and all."
        return self._books[bookNumber][chapterNumber][verseNumber]

    def getParsedVerse(self, book, chapter, verse):
        "Returns a verse, parsed."
        return self.parse(self.getVerse(book, chapter, verse))

    def numberOfChapter(self, bookNumber):
        "Retuns the number of thapter in the book of given number."
        return len(self._books[bookNumber])

    def numberOfVerse(self, bookNumber, chapterNumber):
        "Returns the number of verse in the chapter of given numbers."
        return len(self._books[bookNumber][chapterNumber])

###############################################################################
# Stats
###############################################################################

    def numberOfOccurence(self, strongNumber):
        n = 0
        for b in self._books:
            for c in b:
                for v in c:
                    if " " + strongNumber + " " in v:
                        n += 1
        return n
