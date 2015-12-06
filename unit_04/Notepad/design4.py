# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'notepad4.ui'
#
# Created: Sun Dec  6 16:33:03 2015
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
        MainWindow.resize(640, 480)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 0, 621, 451))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu_File = QtGui.QMenu(self.menubar)
        self.menu_File.setObjectName(_fromUtf8("menu_File"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.closeAction = QtGui.QAction(MainWindow)
        self.closeAction.setObjectName(_fromUtf8("closeAction"))
        self.newAction = QtGui.QAction(MainWindow)
        self.newAction.setObjectName(_fromUtf8("newAction"))
        self.openAction = QtGui.QAction(MainWindow)
        self.openAction.setObjectName(_fromUtf8("openAction"))
        self.saveAction = QtGui.QAction(MainWindow)
        self.saveAction.setObjectName(_fromUtf8("saveAction"))
        self.menu_File.addAction(self.newAction)
        self.menu_File.addAction(self.openAction)
        self.menu_File.addAction(self.saveAction)
        self.menu_File.addAction(self.closeAction)
        self.menubar.addAction(self.menu_File.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Блокнот", None))
        self.menu_File.setTitle(_translate("MainWindow", "&File", None))
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

