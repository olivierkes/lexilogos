#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
Converts a whole bible (i.e. every files in the given folder in arg1) changing
all characters from 'symbol' to 'unicode' (cf. 'transliteraite' function) and
writes the result in the folder given in arg2.
"""


import sys, os, re


def transliterate(text):

    symbol = "abcdefghijklmnopqrstuvwxyz"
    unicod = "αβχδεφγηιϕκλμνοπψρστυςωξθζ"

    translit = ""

    for i in range(len(text)):
        if text[i] in symbol:
            translit += unicod[symbol.index(text[i])]
        else:
            translit += text[i]

    return translit

if __name__ == "__main__":
    try:
        folderIn = sys.argv[1]
        folderOut = sys.argv[2]
    except IndexError:
        exit("Please enter 2 arguments: the folder you wish to convert, and \
the destination folder.")

    path = os.path.abspath(os.path.curdir)

    print(path)

    try:
        files = os.listdir(path + "/" + folderIn)
    except FileNotFoundError:
        exit("Please do not enter an imaginary folder.")

    folderIn = path + "/" + folderIn
    folderOut = path + "/" + folderOut
    if not os.path.exists(folderOut):
        os.makedirs(folderOut)

    for book in files:
        f = open(folderIn + "/" + book, 'r')
        text = f.read()
        f.close()

        translit = transliterate(text)

        f = open(folderOut + "/" + book, 'w')
        f.write(translit)
        f.close()
