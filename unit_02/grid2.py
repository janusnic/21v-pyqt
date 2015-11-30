#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Code PyQt4

QtGui.QGridLayout()

"""
import sys, os
from PyQt4 import QtGui, QtCore

class Button(QtGui.QToolButton):
    def __init__(self, text, parent=None):
        super(Button, self).__init__(parent)

        self.setSizePolicy(QtGui.QSizePolicy.Expanding,
                QtGui.QSizePolicy.Preferred)
        self.setText(text)


class Calculator(QtGui.QDialog):
    
    NumDigitButtons = 10
    
    def __init__(self, parent=None):
        super(Calculator, self).__init__(parent)


        self.digitButtons = []
        
        for i in range(Calculator.NumDigitButtons):
            self.digitButtons.append(self.createButton(str(i)))

        mainLayout = QtGui.QGridLayout()
        mainLayout.setSizeConstraint(QtGui.QLayout.SetFixedSize)

        for i in range(1, Calculator.NumDigitButtons):
            row = ((9 - i) / 3) + 2
            column = ((i - 1) % 3) + 1
            mainLayout.addWidget(self.digitButtons[i], row, column)

        mainLayout.addWidget(self.digitButtons[0], 5, 1)
        self.setLayout(mainLayout)

        self.setWindowTitle("Calculator")

    def createButton(self, text):
        button = Button(text)

        return button

def main():
    app = QtGui.QApplication(sys.argv)
    calc = Calculator()
    sys.exit(calc.exec_())

if __name__ == '__main__':
    main()
