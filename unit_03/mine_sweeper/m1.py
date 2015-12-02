#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Mine Sweeper Game
"""
import sys

from PyQt4 import QtCore, QtGui

class MyButton(QtGui.QPushButton):
  def __init__(self, parent=None):
    super(MyButton, self).__init__(parent)

class MainWindow(QtGui.QWidget):
  """ Main Wrapper For GUI """
  def __init__(self, parent=None):
    super(MainWindow, self).__init__(parent)
    setting = QtCore.QSettings()
    layout = QtGui.QGridLayout()
    layout.setMargin(1)
    layout.setSpacing(1)
    self.button = []
    for r in range(16):
      self.button.append( [] )
      for c in range(16):
        self.button[r].append( MyButton() )
        self.button[r][c].setFixedSize(20,20)
        self.button[r][c].row = r
        self.button[r][c].col = c
        self.button[r][c].parent = self
        self.button[r][c].revealed = False
        layout.addWidget( self.button[r][c], r, c)
    mainLayout = QtGui.QGridLayout()

    mainLayout.addLayout(layout,1,0)

    self.setLayout(mainLayout)
    self.layout().setSizeConstraint(QtGui.QLayout.SetFixedSize)

  
### Main script
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MainWindow()
    myapp.show()
    sys.exit(app.exec_())
