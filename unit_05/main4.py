# -*- coding: utf-8 -*-
#! /usr/bin/python

import sys
import os
from PyQt4 import QtGui
from PyQt4.QtCore import Qt

import design4

class Notepad(QtGui.QMainWindow, design4.Ui_MainWindow):
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

        self.bulletAction.triggered.connect(self.bulletList)
        self.numberedAction.triggered.connect(self.numberList)

        self.fontColor.triggered.connect(self.fontColorChanged)
        self.backColor.triggered.connect(self.highlight)

        self.boldAction.triggered.connect(self.bold)
        self.italicAction.triggered.connect(self.italic)
        self.underlAction.triggered.connect(self.underline)
        self.strikeAction.triggered.connect(self.strike)
        self.superAction.triggered.connect(self.superScript)
        self.subAction.triggered.connect(self.subScript)


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

    def bulletList(self):

        cursor = self.textEdit.textCursor()

        # Insert bulleted list
        cursor.insertList(QtGui.QTextListFormat.ListDisc)

    def numberList(self):

        cursor = self.textEdit.textCursor()

        # Insert list with numbers
        cursor.insertList(QtGui.QTextListFormat.ListDecimal)

    def fontColorChanged(self):

        # Get a color from the text dialog
        color = QtGui.QColorDialog.getColor()

        # Set it as the new text color
        self.textEdit.setTextColor(color)

    def highlight(self):

        color = QtGui.QColorDialog.getColor()

        self.textEdit.setTextBackgroundColor(color)

    def bold(self):

        if self.textEdit.fontWeight() == QtGui.QFont.Bold:

            self.textEdit.setFontWeight(QtGui.QFont.Normal)

        else:

            self.textEdit.setFontWeight(QtGui.QFont.Bold)

    def italic(self):

        state = self.textEdit.fontItalic()

        self.textEdit.setFontItalic(not state)

    def underline(self):

        state = self.textEdit.fontUnderline()

        self.textEdit.setFontUnderline(not state)

    def strike(self):

        # Grab the text's format
        fmt = self.textEdit.currentCharFormat()

        # Set the fontStrikeOut property to its opposite
        fmt.setFontStrikeOut(not fmt.fontStrikeOut())

        # And set the next char format
        self.textEdit.setCurrentCharFormat(fmt)

    def superScript(self):

        # Grab the current format
        fmt = self.textEdit.currentCharFormat()

        # And get the vertical alignment property
        align = fmt.verticalAlignment()

        # Toggle the state
        if align == QtGui.QTextCharFormat.AlignNormal:

            fmt.setVerticalAlignment(QtGui.QTextCharFormat.AlignSuperScript)

        else:

            fmt.setVerticalAlignment(QtGui.QTextCharFormat.AlignNormal)

        # Set the new format
        self.textEdit.setCurrentCharFormat(fmt)

    def subScript(self):

        # Grab the current format
        fmt = self.textEdit.currentCharFormat()

        # And get the vertical alignment property
        align = fmt.verticalAlignment()

        # Toggle the state
        if align == QtGui.QTextCharFormat.AlignNormal:

            fmt.setVerticalAlignment(QtGui.QTextCharFormat.AlignSubScript)

        else:

            fmt.setVerticalAlignment(QtGui.QTextCharFormat.AlignNormal)

        # Set the new format
        self.textEdit.setCurrentCharFormat(fmt)

def main():
    app = QtGui.QApplication(sys.argv)
    form = Notepad()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()