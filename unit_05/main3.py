# -*- coding: utf-8 -*-
#! /usr/bin/python

import sys
import os
from PyQt4 import QtGui
from PyQt4.QtCore import Qt

import design3

class Notepad(QtGui.QMainWindow, design3.Ui_MainWindow):
    def __init__(self, parent=None):
        super(Notepad, self).__init__(parent)

        self.filename = ""

        self.setupUi(self)


        self.closeAction.triggered.connect(self.close)
        self.newAction.triggered.connect(self.newFile) 
        self.saveAction.triggered.connect(self.saveFile) 
        self.openAction.triggered.connect(self.openFile)

        self.printAction.triggered.connect(self.printHandler)
        self.previewAction.triggered.connect(self.preview)

        self.cutAction.triggered.connect(self.textEdit.cut)
        self.copyAction.triggered.connect(self.textEdit.copy)
        self.pasteAction.triggered.connect(self.textEdit.paste)
        self.undoAction.triggered.connect(self.textEdit.undo)
        self.redoAction.triggered.connect(self.textEdit.redo)

    def newFile(self):
        #self.textEdit.clear()
        spawn = Notepad(self)
        spawn.show()

        
    def saveFile(self):
        
        # Only open dialog if there is no filename yet
        if not self.filename:
          self.filename = QtGui.QFileDialog.getSaveFileName(self, 'Save File','.')

        # Append extension if not there yet if you use python3:
        # if not self.filename.endswith(".wrt"):
        if not self.filename.endsWith(".wrt"):
          self.filename += ".wrt"

        # We just store the contents of the text file along with the
        # format in html, which Qt does in a very nice way for us
        with open(self.filename,"wt") as file:
            file.write(self.textEdit.toHtml())

    def openFile(self):
        # Get filename and show only .writer files
        self.filename = QtGui.QFileDialog.getOpenFileName(self, 'Open File',".",filter= "All (*);;txt(*.wrt *.txt)")

        if self.filename:
            with open(self.filename,"rt") as file:
                self.textEdit.setText(file.read())

    def preview(self):

        # Open preview dialog
        preview = QtGui.QPrintPreviewDialog()

        # If a print is requested, open print dialog
        preview.paintRequested.connect(lambda p: self.textEdit.print_(p))

        preview.exec_()

    def printHandler(self):

        # Open printing dialog
        dialog = QtGui.QPrintDialog()

        if dialog.exec_() == QtGui.QDialog.Accepted:
            self.textEdit.document().print_(dialog.printer())

def main():
    app = QtGui.QApplication(sys.argv)
    form = Notepad()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()