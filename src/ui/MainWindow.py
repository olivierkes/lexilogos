# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created: Wed Jun 19 13:40:56 2013
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget_settings = QtGui.QDockWidget(MainWindow)
        self.dockWidget_settings.setObjectName(_fromUtf8("dockWidget_settings"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.verticalLayout = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox_3 = QtGui.QGroupBox(self.dockWidgetContents)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.groupBox_3)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label)
        self.comboBox_book = QtGui.QComboBox(self.groupBox_3)
        self.comboBox_book.setObjectName(_fromUtf8("comboBox_book"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.comboBox_book)
        self.comboBox_chapter = QtGui.QComboBox(self.groupBox_3)
        self.comboBox_chapter.setObjectName(_fromUtf8("comboBox_chapter"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.comboBox_chapter)
        self.label_2 = QtGui.QLabel(self.groupBox_3)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtGui.QLabel(self.groupBox_3)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.comboBox_verseFrom = QtGui.QComboBox(self.groupBox_3)
        self.comboBox_verseFrom.setObjectName(_fromUtf8("comboBox_verseFrom"))
        self.horizontalLayout_2.addWidget(self.comboBox_verseFrom)
        self.label_4 = QtGui.QLabel(self.groupBox_3)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_2.addWidget(self.label_4)
        self.comboBox_verseTo = QtGui.QComboBox(self.groupBox_3)
        self.comboBox_verseTo.setObjectName(_fromUtf8("comboBox_verseTo"))
        self.horizontalLayout_2.addWidget(self.comboBox_verseTo)
        self.formLayout.setLayout(3, QtGui.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.line = QtGui.QFrame(self.groupBox_3)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.line)
        self.verticalLayout_6.addLayout(self.formLayout)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.pushButton_Start = QtGui.QPushButton(self.dockWidgetContents)
        self.pushButton_Start.setObjectName(_fromUtf8("pushButton_Start"))
        self.verticalLayout.addWidget(self.pushButton_Start)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.pushButton_moreOptions = QtGui.QPushButton(self.dockWidgetContents)
        self.pushButton_moreOptions.setCheckable(True)
        self.pushButton_moreOptions.setChecked(True)
        self.pushButton_moreOptions.setObjectName(_fromUtf8("pushButton_moreOptions"))
        self.horizontalLayout_5.addWidget(self.pushButton_moreOptions)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.widget = QtGui.QWidget(self.dockWidgetContents)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_7.setMargin(0)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.groupBox = QtGui.QGroupBox(self.widget)
        self.groupBox.setEnabled(False)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.radioButton_voc = QtGui.QRadioButton(self.groupBox)
        self.radioButton_voc.setChecked(True)
        self.radioButton_voc.setObjectName(_fromUtf8("radioButton_voc"))
        self.verticalLayout_3.addWidget(self.radioButton_voc)
        self.radioButton_grammar = QtGui.QRadioButton(self.groupBox)
        self.radioButton_grammar.setObjectName(_fromUtf8("radioButton_grammar"))
        self.verticalLayout_3.addWidget(self.radioButton_grammar)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout_7.addWidget(self.groupBox)
        self.groupBox_4 = QtGui.QGroupBox(self.widget)
        self.groupBox_4.setTitle(_fromUtf8(""))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.formLayout_2 = QtGui.QFormLayout(self.groupBox_4)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label_6 = QtGui.QLabel(self.groupBox_4)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_6)
        self.comboBox_sort = QtGui.QComboBox(self.groupBox_4)
        self.comboBox_sort.setObjectName(_fromUtf8("comboBox_sort"))
        self.comboBox_sort.addItem(_fromUtf8(""))
        self.comboBox_sort.addItem(_fromUtf8(""))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.comboBox_sort)
        self.label_7 = QtGui.QLabel(self.groupBox_4)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_7)
        self.comboBox_testLexicalForm = QtGui.QComboBox(self.groupBox_4)
        self.comboBox_testLexicalForm.setObjectName(_fromUtf8("comboBox_testLexicalForm"))
        self.comboBox_testLexicalForm.addItem(_fromUtf8(""))
        self.comboBox_testLexicalForm.addItem(_fromUtf8(""))
        self.comboBox_testLexicalForm.addItem(_fromUtf8(""))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.FieldRole, self.comboBox_testLexicalForm)
        self.label_8 = QtGui.QLabel(self.groupBox_4)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_8)
        self.comboBox_textLanguage = QtGui.QComboBox(self.groupBox_4)
        self.comboBox_textLanguage.setObjectName(_fromUtf8("comboBox_textLanguage"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.comboBox_textLanguage)
        self.label_9 = QtGui.QLabel(self.groupBox_4)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_9)
        self.comboBox_lexiconVersion = QtGui.QComboBox(self.groupBox_4)
        self.comboBox_lexiconVersion.setObjectName(_fromUtf8("comboBox_lexiconVersion"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.comboBox_lexiconVersion)
        self.verticalLayout_7.addWidget(self.groupBox_4)
        self.groupBox_2 = QtGui.QGroupBox(self.widget)
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.checkBox_moreThanOccurences = QtGui.QCheckBox(self.groupBox_2)
        self.checkBox_moreThanOccurences.setObjectName(_fromUtf8("checkBox_moreThanOccurences"))
        self.gridLayout.addWidget(self.checkBox_moreThanOccurences, 1, 0, 1, 1)
        self.checkBox_lessThanOccurences = QtGui.QCheckBox(self.groupBox_2)
        self.checkBox_lessThanOccurences.setObjectName(_fromUtf8("checkBox_lessThanOccurences"))
        self.gridLayout.addWidget(self.checkBox_lessThanOccurences, 0, 0, 1, 1)
        self.comboBox_lessThanOccurences = QtGui.QComboBox(self.groupBox_2)
        self.comboBox_lessThanOccurences.setEditable(True)
        self.comboBox_lessThanOccurences.setObjectName(_fromUtf8("comboBox_lessThanOccurences"))
        self.comboBox_lessThanOccurences.addItem(_fromUtf8(""))
        self.comboBox_lessThanOccurences.addItem(_fromUtf8(""))
        self.comboBox_lessThanOccurences.addItem(_fromUtf8(""))
        self.comboBox_lessThanOccurences.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox_lessThanOccurences, 0, 1, 1, 1)
        self.comboBox_moreThanOccurences = QtGui.QComboBox(self.groupBox_2)
        self.comboBox_moreThanOccurences.setEditable(True)
        self.comboBox_moreThanOccurences.setObjectName(_fromUtf8("comboBox_moreThanOccurences"))
        self.comboBox_moreThanOccurences.addItem(_fromUtf8(""))
        self.comboBox_moreThanOccurences.addItem(_fromUtf8(""))
        self.comboBox_moreThanOccurences.addItem(_fromUtf8(""))
        self.comboBox_moreThanOccurences.addItem(_fromUtf8(""))
        self.comboBox_moreThanOccurences.addItem(_fromUtf8(""))
        self.comboBox_moreThanOccurences.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox_moreThanOccurences, 1, 1, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout)
        self.label_5 = QtGui.QLabel(self.groupBox_2)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_5.addWidget(self.label_5)
        self.verticalLayout_7.addWidget(self.groupBox_2)
        self.verticalLayout.addWidget(self.widget)
        self.dockWidget_settings.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget_settings)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.pushButton_moreOptions, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.widget.setVisible)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "Pericope:", None))
        self.label.setText(_translate("MainWindow", "Book:", None))
        self.label_2.setText(_translate("MainWindow", "Chapter", None))
        self.label_3.setText(_translate("MainWindow", "Verse", None))
        self.label_4.setText(_translate("MainWindow", ":", None))
        self.pushButton_Start.setText(_translate("MainWindow", "Start", None))
        self.pushButton_moreOptions.setText(_translate("MainWindow", "+", None))
        self.groupBox.setTitle(_translate("MainWindow", "Type of game", None))
        self.radioButton_voc.setText(_translate("MainWindow", "Vocabulary", None))
        self.radioButton_grammar.setText(_translate("MainWindow", "Grammar", None))
        self.label_6.setText(_translate("MainWindow", "Sort words", None))
        self.comboBox_sort.setItemText(0, _translate("MainWindow", "Randomely", None))
        self.comboBox_sort.setItemText(1, _translate("MainWindow", "Alphabetically", None))
        self.label_7.setText(_translate("MainWindow", "Test", None))
        self.comboBox_testLexicalForm.setItemText(0, _translate("MainWindow", "Textual form", None))
        self.comboBox_testLexicalForm.setItemText(1, _translate("MainWindow", "Lexical form", None))
        self.comboBox_testLexicalForm.setItemText(2, _translate("MainWindow", "Both", None))
        self.label_8.setText(_translate("MainWindow", "Text", None))
        self.label_9.setText(_translate("MainWindow", "Lexicon", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Only words with:", None))
        self.checkBox_moreThanOccurences.setText(_translate("MainWindow", "more than", None))
        self.checkBox_lessThanOccurences.setText(_translate("MainWindow", "less than", None))
        self.comboBox_lessThanOccurences.setItemText(0, _translate("MainWindow", "500", None))
        self.comboBox_lessThanOccurences.setItemText(1, _translate("MainWindow", "1000", None))
        self.comboBox_lessThanOccurences.setItemText(2, _translate("MainWindow", "1500", None))
        self.comboBox_lessThanOccurences.setItemText(3, _translate("MainWindow", "2000", None))
        self.comboBox_moreThanOccurences.setItemText(0, _translate("MainWindow", "10", None))
        self.comboBox_moreThanOccurences.setItemText(1, _translate("MainWindow", "20", None))
        self.comboBox_moreThanOccurences.setItemText(2, _translate("MainWindow", "30", None))
        self.comboBox_moreThanOccurences.setItemText(3, _translate("MainWindow", "50", None))
        self.comboBox_moreThanOccurences.setItemText(4, _translate("MainWindow", "70", None))
        self.comboBox_moreThanOccurences.setItemText(5, _translate("MainWindow", "100", None))
        self.label_5.setText(_translate("MainWindow", "occurences in the NT.", None))

