# -*- coding: utf-8 -*-
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