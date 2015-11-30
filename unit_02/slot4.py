#!/usr/bin/python
# -*- coding: utf-8 -*-
 
import sys, random
from PyQt4 import QtGui, QtCore
 
class withSlot(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
 
        self.setWindowTitle(self.trUtf8('Свой слот в PyQt'))
        self.resize(300, 50)
        self.button=QtGui.QPushButton('Get!', self)
        self.button.show()
 
        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(self.button)
        self.setLayout(vbox)
        self.connect(self.button, QtCore.SIGNAL('clicked()'), self.getIt)
 
    def getIt(self):
        self.button.setText(str(random.randint(1, 10)))
 
app = QtGui.QApplication(sys.argv)
qb = withSlot()
qb.show()
sys.exit(app.exec_())