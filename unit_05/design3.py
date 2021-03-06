# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'notepad3.ui'
#
# Created: Wed Dec  9 12:34:29 2015
#      by: PyQt4 UI code generator 4.10.4
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
        MainWindow.resize(658, 480)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 0, 641, 461))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 658, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu_File = QtGui.QMenu(self.menubar)
        self.menu_File.setObjectName(_fromUtf8("menu_File"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName(_fromUtf8("menuView"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolbar = QtGui.QToolBar(MainWindow)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setPointSize(14)
        self.toolbar.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/new.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolbar.setProperty("new", icon)
        self.toolbar.setObjectName(_fromUtf8("toolbar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolbar)
        MainWindow.insertToolBarBreak(self.toolbar)
        self.closeAction = QtGui.QAction(MainWindow)
        self.closeAction.setObjectName(_fromUtf8("closeAction"))
        self.newAction = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/new.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.newAction.setIcon(icon1)
        self.newAction.setObjectName(_fromUtf8("newAction"))
        self.openAction = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/open.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.openAction.setIcon(icon2)
        self.openAction.setObjectName(_fromUtf8("openAction"))
        self.saveAction = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/save.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveAction.setIcon(icon3)
        self.saveAction.setObjectName(_fromUtf8("saveAction"))
        self.printAction = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/print.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.printAction.setIcon(icon4)
        self.printAction.setObjectName(_fromUtf8("printAction"))
        self.previewAction = QtGui.QAction(MainWindow)
        self.previewAction.setIcon(icon3)
        self.previewAction.setObjectName(_fromUtf8("previewAction"))
        self.cutAction = QtGui.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/cut.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cutAction.setIcon(icon5)
        self.cutAction.setObjectName(_fromUtf8("cutAction"))
        self.copyAction = QtGui.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/copy.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.copyAction.setIcon(icon6)
        self.copyAction.setObjectName(_fromUtf8("copyAction"))
        self.pasteAction = QtGui.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/paste.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pasteAction.setIcon(icon7)
        self.pasteAction.setObjectName(_fromUtf8("pasteAction"))
        self.undoAction = QtGui.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/undo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.undoAction.setIcon(icon8)
        self.undoAction.setObjectName(_fromUtf8("undoAction"))
        self.redoAction = QtGui.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/redo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.redoAction.setIcon(icon9)
        self.redoAction.setObjectName(_fromUtf8("redoAction"))
        self.menu_File.addAction(self.newAction)
        self.menu_File.addAction(self.openAction)
        self.menu_File.addAction(self.saveAction)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.printAction)
        self.menu_File.addAction(self.previewAction)
        self.menu_File.addAction(self.closeAction)
        self.menuEdit.addAction(self.cutAction)
        self.menuEdit.addAction(self.copyAction)
        self.menuEdit.addAction(self.pasteAction)
        self.menuEdit.addAction(self.undoAction)
        self.menuEdit.addAction(self.redoAction)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.newAction)
        self.toolbar.addAction(self.openAction)
        self.toolbar.addAction(self.saveAction)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.printAction)
        self.toolbar.addAction(self.previewAction)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.cutAction)
        self.toolbar.addAction(self.copyAction)
        self.toolbar.addAction(self.pasteAction)
        self.toolbar.addAction(self.undoAction)
        self.toolbar.addAction(self.redoAction)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Блокнот", None))
        self.menu_File.setTitle(_translate("MainWindow", "&File", None))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit", None))
        self.menuView.setTitle(_translate("MainWindow", "View", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.toolbar.setWindowTitle(_translate("MainWindow", "Options", None))
        self.closeAction.setText(_translate("MainWindow", "Close", None))
        self.closeAction.setToolTip(_translate("MainWindow", "Close Notepad", None))
        self.closeAction.setStatusTip(_translate("MainWindow", "Close app", None))
        self.closeAction.setShortcut(_translate("MainWindow", "Ctrl+Q", None))
        self.newAction.setText(_translate("MainWindow", "New", None))
        self.newAction.setToolTip(_translate("MainWindow", "Create New File", None))
        self.newAction.setStatusTip(_translate("MainWindow", "Create New File", None))
        self.newAction.setShortcut(_translate("MainWindow", "Ctrl+N", None))
        self.openAction.setText(_translate("MainWindow", "Open", None))
        self.openAction.setToolTip(_translate("MainWindow", "Open a File", None))
        self.openAction.setStatusTip(_translate("MainWindow", "Open a File", None))
        self.openAction.setShortcut(_translate("MainWindow", "Ctrl+O", None))
        self.saveAction.setText(_translate("MainWindow", "Save", None))
        self.saveAction.setToolTip(_translate("MainWindow", "Save a File", None))
        self.saveAction.setStatusTip(_translate("MainWindow", "Save a File", None))
        self.saveAction.setShortcut(_translate("MainWindow", "Ctrl+S", None))
        self.printAction.setText(_translate("MainWindow", "Print document", None))
        self.printAction.setStatusTip(_translate("MainWindow", "Print document", None))
        self.printAction.setShortcut(_translate("MainWindow", "Ctrl+P", None))
        self.previewAction.setText(_translate("MainWindow", "Page View", None))
        self.previewAction.setStatusTip(_translate("MainWindow", "Preview page before printing", None))
        self.previewAction.setShortcut(_translate("MainWindow", "Ctrl+Shift+P", None))
        self.cutAction.setText(_translate("MainWindow", "Cut to clipboard", None))
        self.cutAction.setStatusTip(_translate("MainWindow", "Delete and copy text to clipboard", None))
        self.cutAction.setShortcut(_translate("MainWindow", "Ctrl+X", None))
        self.copyAction.setText(_translate("MainWindow", "Copy text to clipboard", None))
        self.copyAction.setStatusTip(_translate("MainWindow", "Copy text to clipboard", None))
        self.copyAction.setShortcut(_translate("MainWindow", "Ctrl+C", None))
        self.pasteAction.setText(_translate("MainWindow", "Paste from clipboard", None))
        self.pasteAction.setStatusTip(_translate("MainWindow", "Paste text from clipboard", None))
        self.pasteAction.setShortcut(_translate("MainWindow", "Ctrl+V", None))
        self.undoAction.setText(_translate("MainWindow", "Undo last action", None))
        self.undoAction.setStatusTip(_translate("MainWindow", "Undo last action", None))
        self.undoAction.setShortcut(_translate("MainWindow", "Ctrl+Z", None))
        self.redoAction.setText(_translate("MainWindow", "Redo last undone thing", None))
        self.redoAction.setStatusTip(_translate("MainWindow", "Redo last undone thing", None))
        self.redoAction.setShortcut(_translate("MainWindow", "Ctrl+Y", None))

import pad_rc
