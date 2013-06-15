#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Lexilogos main file.
"""

import sys
from PyQt4 import QtGui

from MainWindow import MainWindow


def main():

    app = QtGui.QApplication(sys.argv)
    app.setOrganizationName("Theologeek")
    app.setOrganizationDomain("www.theologeek.ch")
    app.setApplicationName("Lexilogos")

    w = MainWindow()
    w.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
