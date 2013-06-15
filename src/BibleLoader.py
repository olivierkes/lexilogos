# -*- coding: utf-8 -*-

import os
from PyQt4.QtCore import QRegExp

#TODO: traduction

class BibleLoader():

    def __init__(self, bible, trad=False):

        self._bible = bible
        self._books = [0]*27
        self._trad = trad
        self.loadBible()


    def loadBible(self):
        if self._trad:
            prefix = "../trad/"
        else:
            prefix = "../mss/"

        try:
            files = os.listdir(prefix + self._bible)
        except FileNotFoundError:
            print("Please do not enter an imaginary bible.")
            return

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
                v += l
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

    def getBook(self, bookNumber):
        return self._books[bookNumber]

    def getChapter(self, bookNumber, chapterNumber):
        return self._books[bookNumber][chapterNumber]

    def getVerse(self, bookNumber, chapterNumber, verseNumber):
        return self._books[bookNumber][chapterNumber][verseNumber]

    def chapterNumber(self, bookNumber):
        return len(self._books[bookNumber])

    def verseNumber(self, bookNumber, chapterNumber):
        return len(self._books[bookNumber][chapterNumber])

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
            if i in bookcode: return bookorder.index(i)

        print("ERROR: the bookcode is invalid.")

    def setBible(self, bible):
        self._bible = bible

    def Bible(self):
        return self._bible