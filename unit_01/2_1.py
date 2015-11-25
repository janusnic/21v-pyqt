#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Code PyQt4
Первое GUI-приложение

"""

import sys
from PyQt4 import QtGui, QtCore
        
class Example(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
 
        self.setGeometry(600, 300, 500, 150)
        self.setWindowTitle(u"Первое GUI-приложение")

def main():

    app = QtGui.QApplication(sys.argv)

    ex = Example()

    ex.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()