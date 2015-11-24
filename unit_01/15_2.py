#!/usr/bin/python
# -*- coding: utf-8 -*-
 
import sys
from PyQt4 import QtGui, QtCore
 
class Emit(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
 
        self.setWindowTitle(self.trUtf8('Собственный сигнал'))
        self.resize(250, 150)
        self.connect(self, QtCore.SIGNAL('ourSignal()'), QtCore.SLOT('close()'))
 
    def mousePressEvent(self, event):
        self.emit(QtCore.SIGNAL('ourSignal()'))
 
app = QtGui.QApplication(sys.argv)
qb = Emit()
qb.show()
sys.exit(app.exec_())