# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Game.ui'
#
# Created: Sat Jun 15 11:33:55 2013
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
        Game.resize(748, 628)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Game.sizePolicy().hasHeightForWidth())
        Game.setSizePolicy(sizePolicy)
        self.verticalLayout = QtGui.QVBoxLayout(Game)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.plainTextEdit_original = QtGui.QPlainTextEdit(Game)
        self.plainTextEdit_original.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEdit_original.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_original.setSizePolicy(sizePolicy)
        self.plainTextEdit_original.setReadOnly(True)
        self.plainTextEdit_original.setBackgroundVisible(False)
        self.plainTextEdit_original.setCenterOnScroll(False)
        self.plainTextEdit_original.setObjectName(_fromUtf8("plainTextEdit_original"))
        self.horizontalLayout_8.addWidget(self.plainTextEdit_original)
        self.plainTextEdit_version = QtGui.QPlainTextEdit(Game)
        self.plainTextEdit_version.setReadOnly(True)
        self.plainTextEdit_version.setObjectName(_fromUtf8("plainTextEdit_version"))
        self.horizontalLayout_8.addWidget(self.plainTextEdit_version)
        self.verticalLayout_9 = QtGui.QVBoxLayout()
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.pushButton_cheatText = QtGui.QPushButton(Game)
        self.pushButton_cheatText.setCheckable(True)
        self.pushButton_cheatText.setChecked(True)
        self.pushButton_cheatText.setObjectName(_fromUtf8("pushButton_cheatText"))
        self.verticalLayout_9.addWidget(self.pushButton_cheatText)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem)
        self.horizontalLayout_8.addLayout(self.verticalLayout_9)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.groupBox_5 = QtGui.QGroupBox(Game)
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.listView_3 = QtGui.QListView(self.groupBox_5)
        self.listView_3.setObjectName(_fromUtf8("listView_3"))
        self.horizontalLayout_6.addWidget(self.listView_3)
        self.listView = QtGui.QListView(self.groupBox_5)
        self.listView.setObjectName(_fromUtf8("listView"))
        self.horizontalLayout_6.addWidget(self.listView)
        self.verticalLayout_10 = QtGui.QVBoxLayout()
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem1)
        self.pushButton_4 = QtGui.QPushButton(self.groupBox_5)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.verticalLayout_10.addWidget(self.pushButton_4)
        self.pushButton_3 = QtGui.QPushButton(self.groupBox_5)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.verticalLayout_10.addWidget(self.pushButton_3)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem2)
        self.horizontalLayout_6.addLayout(self.verticalLayout_10)
        self.listView_2 = QtGui.QListView(self.groupBox_5)
        self.listView_2.setObjectName(_fromUtf8("listView_2"))
        self.horizontalLayout_6.addWidget(self.listView_2)
        self.verticalLayout_8.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.pushButton_Validate = QtGui.QPushButton(self.groupBox_5)
        self.pushButton_Validate.setObjectName(_fromUtf8("pushButton_Validate"))
        self.horizontalLayout_3.addWidget(self.pushButton_Validate)
        self.verticalLayout_8.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addWidget(self.groupBox_5)

        self.retranslateUi(Game)
        QtCore.QObject.connect(self.pushButton_cheatText, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.plainTextEdit_version.setVisible)
        QtCore.QMetaObject.connectSlotsByName(Game)

    def retranslateUi(self, Game):
        Game.setWindowTitle(_translate("Game", "Form", None))
        self.plainTextEdit_original.setPlainText(_translate("Game", "1   Ἐν  ἀρχῇ  ἦν  ὁ  λόγος,  καὶ  ὁ  λόγος  ἦν  πρὸς  τὸν  θεόν,  καὶ  θεὸς  ἦν  ὁ  λόγος.  2   οὗτος  ἦν  ἐν  ἀρχῇ  πρὸς  τὸν  θεόν.  3   πάντα  δι’  αὐτοῦ  ἐγένετο,  καὶ  χωρὶς  αὐτοῦ  ἐγένετο  οὐδὲ  ἓν  ὃ  γέγονεν  4   ἐν  αὐτῷ  ζωὴ  ἦν,  καὶ  ἡ  ζωὴ  ἦν  τὸ  φῶς  τῶν  ἀνθρώπων·  5   καὶ  τὸ  φῶς  ἐν  τῇ  σκοτίᾳ  φαίνει  καὶ  ἡ  σκοτία  αὐτὸ  οὐ  κατέλαβεν.  ", None))
        self.pushButton_cheatText.setText(_translate("Game", "?", None))
        self.groupBox_5.setTitle(_translate("Game", "Answers", None))
        self.pushButton_4.setText(_translate("Game", "→", None))
        self.pushButton_3.setText(_translate("Game", "←", None))
        self.pushButton_Validate.setText(_translate("Game", "Validate", None))
