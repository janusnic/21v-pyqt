# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'notepad1.ui'
#
# Created: Tue Dec  8 19:08:28 2015
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
        self.menu_File.addAction(self.newAction)
        self.menu_File.addAction(self.openAction)
        self.menu_File.addAction(self.saveAction)
        self.menu_File.addAction(self.closeAction)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.newAction)
        self.toolbar.addAction(self.openAction)
        self.toolbar.addAction(self.saveAction)
        self.toolbar.addSeparator()

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

import pad_rc
