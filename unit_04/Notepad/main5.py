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