# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Game.ui'
#
# Created: Sat Jun 22 13:03:30 2013
#      by: PyQt4 UI code generator 4.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Game(object):
    def setupUi(self, Game):
        Game.setObjectName(_fromUtf8("Game"))
        Game.resize(851, 860)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Game.sizePolicy().hasHeightForWidth())
        Game.setSizePolicy(sizePolicy)
        self.verticalLayout = QtGui.QVBoxLayout(Game)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.splitter_2 = QtGui.QSplitter(Game)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.widget = QtGui.QWidget(self.splitter_2)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_8.setMargin(0)
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.plainTextEdit_original = QtGui.QPlainTextEdit(self.widget)
        self.plainTextEdit_original.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEdit_original.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_original.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.plainTextEdit_original.setFont(font)
        self.plainTextEdit_original.setReadOnly(True)
        self.plainTextEdit_original.setPlainText(_fromUtf8(""))
        self.plainTextEdit_original.setBackgroundVisible(False)
        self.plainTextEdit_original.setCenterOnScroll(False)
        self.plainTextEdit_original.setObjectName(_fromUtf8("plainTextEdit_original"))
        self.horizontalLayout_8.addWidget(self.plainTextEdit_original)
        self.plainTextEdit_version = QtGui.QPlainTextEdit(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEdit_version.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_version.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.plainTextEdit_version.setFont(font)
        self.plainTextEdit_version.setReadOnly(True)
        self.plainTextEdit_version.setObjectName(_fromUtf8("plainTextEdit_version"))
        self.horizontalLayout_8.addWidget(self.plainTextEdit_version)
        self.verticalLayout_9 = QtGui.QVBoxLayout()
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.pushButton_cheatText = QtGui.QPushButton(self.widget)
        self.pushButton_cheatText.setCheckable(True)
        self.pushButton_cheatText.setChecked(True)
        self.pushButton_cheatText.setObjectName(_fromUtf8("pushButton_cheatText"))
        self.verticalLayout_9.addWidget(self.pushButton_cheatText)
        self.horizontalLayout_8.addLayout(self.verticalLayout_9)
        self.groupBox_5 = QtGui.QGroupBox(self.splitter_2)
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.splitter = QtGui.QSplitter(self.groupBox_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.listWidget_original = QtGui.QListWidget(self.splitter)
        self.listWidget_original.setObjectName(_fromUtf8("listWidget_original"))
        self.listWidget_translation = QtGui.QListWidget(self.splitter)
        self.listWidget_translation.setObjectName(_fromUtf8("listWidget_translation"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.splitter)
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_10 = QtGui.QVBoxLayout()
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem)
        self.pushButton_guess = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_guess.setObjectName(_fromUtf8("pushButton_guess"))
        self.verticalLayout_10.addWidget(self.pushButton_guess)
        self.pushButton_undoGuess = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_undoGuess.setObjectName(_fromUtf8("pushButton_undoGuess"))
        self.verticalLayout_10.addWidget(self.pushButton_undoGuess)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.verticalLayout_10)
        self.listWidget_guesses = QtGui.QListWidget(self.horizontalLayoutWidget)
        self.listWidget_guesses.setObjectName(_fromUtf8("listWidget_guesses"))
        self.horizontalLayout.addWidget(self.listWidget_guesses)
        self.verticalLayout_2.addWidget(self.splitter)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.pushButton_Validate = QtGui.QPushButton(self.groupBox_5)
        self.pushButton_Validate.setObjectName(_fromUtf8("pushButton_Validate"))
        self.horizontalLayout_3.addWidget(self.pushButton_Validate)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addWidget(self.splitter_2)

        self.retranslateUi(Game)
        QtCore.QObject.connect(self.pushButton_cheatText, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.plainTextEdit_version.setVisible)
        QtCore.QMetaObject.connectSlotsByName(Game)

    def retranslateUi(self, Game):
        Game.setWindowTitle(_translate("Game", "Form", None))
        self.pushButton_cheatText.setText(_translate("Game", "?", None))
        self.groupBox_5.setTitle(_translate("Game", "Answers", None))
        self.listWidget_original.setSortingEnabled(True)
        self.listWidget_translation.setSortingEnabled(True)
        self.pushButton_guess.setText(_translate("Game", "→", None))
        self.pushButton_undoGuess.setText(_translate("Game", "←", None))
        self.pushButton_Validate.setText(_translate("Game", "Solution", None))

