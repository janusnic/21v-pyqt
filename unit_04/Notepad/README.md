# 21v-pyqt unit 04

Qt Designer
===========

Notepad
=======
- Главная форма QMainWindow

- Размер экрана - альбом 640х480

- Создать

- WindowTitle - Блокнот

save notepad.ui
---------------
```
<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>640</width>
    <height>480</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Блокнот</string>
  </property>
  <widget class="QWidget" name="centralwidget"/>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>640</width>
     <height>27</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>

```
pyuic4 notepad.ui -o design1.py
-------------------------------
```
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'notepad.ui'
#
# Created: Sun Dec  6 15:22:25 2015
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", u"Блокнот", None))

```

main1.py
--------
```
#! /usr/bin/python

import sys
import os
from PyQt4 import QtGui

import design1

class Notepad(QtGui.QMainWindow, design1.Ui_MainWindow):
    def __init__(self, parent=None):
        super(Notepad, self).__init__(parent)
        self.setupUi(self)

def main():
    app = QtGui.QApplication(sys.argv)
    form = Notepad()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()

```
design2.py menu
----------------

- setTitle - &File
- closeAction.setText - Close
- closeAction.setToolTip - Close Notepad
- closeAction.setShortcut - Ctrl+Q

```
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'notepad2.ui'
#
# Created: Sun Dec  6 15:49:12 2015
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
        self.menu_File.addAction(self.closeAction)
        self.menubar.addAction(self.menu_File.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Блокнот", None))
        self.menu_File.setTitle(_translate("MainWindow", "&File", None))
        self.closeAction.setText(_translate("MainWindow", "Close", None))
        self.closeAction.setToolTip(_translate("MainWindow", "Close Notepad", None))
        self.closeAction.setShortcut(_translate("MainWindow", "Ctrl+Q", None))


```

main2.py - menu
---------------
```
# -*- coding: utf-8 -*-
#! /usr/bin/python

import sys
import os
from PyQt4 import QtGui

import design2

class Notepad(QtGui.QMainWindow, design2.Ui_MainWindow):
    def __init__(self, parent=None):
        super(Notepad, self).__init__(parent)
        self.setupUi(self)

        self.closeAction.triggered.connect(self.close)

def main():
    app = QtGui.QApplication(sys.argv)
    form = Notepad()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
```

design3.py
----------
```
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'notepad3.ui'
#
# Created: Sun Dec  6 16:14:19 2015
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
        self.newAction.setObjectName(_fromUtf8("newFile"))
        self.openAction = QtGui.QAction(MainWindow)
        self.openAction.setObjectName(_fromUtf8("openFile"))
        self.saveAction = QtGui.QAction(MainWindow)
        self.saveAction.setObjectName(_fromUtf8("saveFile"))
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


```


main3.py - QObject.Signal.connect(doSomething())
------------------------------------------------
```
# -*- coding: utf-8 -*-
#! /usr/bin/python

import sys
import os
from PyQt4 import QtGui

import design3

class Notepad(QtGui.QMainWindow, design3.Ui_MainWindow):
    def __init__(self, parent=None):
        super(Notepad, self).__init__(parent)
        self.setupUi(self)

        self.closeAction.triggered.connect(self.close)
        self.newAction.triggered.connect(self.newFile) 
        self.saveAction.triggered.connect(self.saveFile) 
        self.openAction.triggered.connect(self.openFile)

    def newFile(self):
            pass
    def saveFile(self):
            pass
    def openFile(self):
            pass

def main():
    app = QtGui.QApplication(sys.argv)
    form = Notepad()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
```
QTextEdit design4.py
---------------------
```
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'notepad3.ui'
#
# Created: Sun Dec  6 16:14:19 2015
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
        self.newAction.setObjectName(_fromUtf8("newFile"))
        self.openAction = QtGui.QAction(MainWindow)
        self.openAction.setObjectName(_fromUtf8("openFile"))
        self.saveAction = QtGui.QAction(MainWindow)
        self.saveAction.setObjectName(_fromUtf8("saveFile"))
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


```

main4.py - QTextEdit
--------------------
```
# -*- coding: utf-8 -*-
#! /usr/bin/python

import sys
import os
from PyQt4 import QtGui

import design4

class Notepad(QtGui.QMainWindow, design4.Ui_MainWindow):
    def __init__(self, parent=None):
        super(Notepad, self).__init__(parent)
        self.setupUi(self)

        self.closeAction.triggered.connect(self.close)
        self.newAction.triggered.connect(self.newFile) 
        self.saveAction.triggered.connect(self.saveFile) 
        self.openAction.triggered.connect(self.openFile)

    def newFile(self):
            pass
    def saveFile(self):
            pass
    def openFile(self):
            pass

def main():
    app = QtGui.QApplication(sys.argv)
    form = Notepad()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
```


main5.py - Action
------------------

```
# -*- coding: utf-8 -*-
#! /usr/bin/python

import sys
import os
from PyQt4 import QtGui

import design4

class Notepad(QtGui.QMainWindow, design4.Ui_MainWindow):
    def __init__(self, parent=None):
        super(Notepad, self).__init__(parent)
        self.setupUi(self)


        self.closeAction.triggered.connect(self.close)
        self.newAction.triggered.connect(self.newFile) 
        self.saveAction.triggered.connect(self.saveFile) 
        self.openAction.triggered.connect(self.openFile)

    def newFile(self):
        self.textEdit.clear()
        
    def saveFile(self):
        filename = QtGui.QFileDialog.getSaveFileName(self, 'Save File', os.getenv('HOME')) 
        f = open(filename, 'w') 
        filedata = self.textEdit.toPlainText() 
        f.write(filedata) 
        f.close()

    def openFile(self):
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Open File', os.getenv('HOME')) 
        f = open(filename, 'r') 
        filedata = f.read() 
        self.textEdit.setText(filedata) 
        f.close()

def main():
    app = QtGui.QApplication(sys.argv)
    form = Notepad()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
```
