#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Code PyQt4

In this example, we create a simple
window in PyQt4.

"""
from PyQt4 import QtCore, QtGui
import sys
app = QtGui.QApplication(sys.argv)
button = QtGui.QPushButton(u"Завершить работу")
QtCore.QObject.connect(button, QtCore.SIGNAL("clicked()"), app, QtCore.SLOT("quit()"))
button.show()
sys.exit(app.exec_())