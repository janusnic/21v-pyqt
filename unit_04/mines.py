#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Mine Sweeper Game
"""
import sys
import os
import random
from PyQt4 import QtCore, QtGui

var = True
 
class MyButton(QtGui.QPushButton):
  def __init__(self, parent=None):
    super(MyButton, self).__init__(parent)

class MainWindow(QtGui.QWidget):
  """ Main Wrapper For GUI """
  def __init__(self, parent=None):
    super(MainWindow, self).__init__(parent)
    setting = QtCore.QSettings()
    tmp = setting.value("position", QtCore.QPoint(0,0))

    self.alayout = QtGui.QGridLayout()
    self.alayout.setMargin(1)
    self.alayout.setSpacing(1)
    self.button = []

    self.layouttop = QtGui.QHBoxLayout()
    self.layouttop.addWidget(QtGui.QLabel("BombCount"))
    self.bombcount = QtGui.QLabel("0/40")
    self.layouttop.addWidget(self.bombcount)
    self.timer = QtCore.QTimer()
    self.timelabel = QtGui.QLabel("0.0 secs")
    self.timelabel.setStyleSheet("background-color: rgb(0, 0, 0); color: rgb(0,255,0)")
    self.newGame()
    self.layouttop.addWidget(self.timelabel)
    
    self.r1 = QtGui.QRadioButton("16",self)
    self.layouttop.addWidget(self.r1)
    self.r2 = QtGui.QRadioButton("32",self)
    self.layouttop.addWidget(self.r2)

    newgameButton = QtGui.QPushButton("&NewGame")
    newgameButton.setEnabled(True)
    self.layouttop.addWidget(newgameButton)
    topscore = QtGui.QPushButton("Top&Score>>")
    topscore.setCheckable(True)
    self.layouttop.addWidget(topscore)
    self.scoreframe = QtGui.QFrame()
    self.scoreframe.setFrameStyle(QtGui.QFrame.StyledPanel|QtGui.QFrame.Sunken)
    scorelayout = QtGui.QVBoxLayout()
    scorelayout.addWidget(QtGui.QLabel(u"<b>Игра «Сапёр»</b> <i>Данное приложение является реализацией игры «Сапёр» <br>и может быть использовано как по прямому назначению, <br>так и в качестве reference solution.</i> <br>" ) )
    self.scoreframe.setLayout(scorelayout)
    self.scoreframe.setVisible(False)
    self.mainLayout = QtGui.QGridLayout()

    self.mainLayout.addLayout(self.layouttop,0,0)
    self.mainLayout.addLayout(self.alayout,1,0)
    self.mainLayout.addWidget(self.scoreframe,0,1,2,1)
    self.setLayout(self.mainLayout)

    self.layout().setSizeConstraint(QtGui.QLayout.SetFixedSize)
    QtCore.QObject.connect(newgameButton, QtCore.SIGNAL("clicked()"), self.newGame)
    QtCore.QObject.connect(self.timer, QtCore.SIGNAL("timeout()"), self.updateTime)
    QtCore.QObject.connect(topscore, QtCore.SIGNAL("clicked(bool)"), self.scoreframe.setVisible )

    
    self.r1.toggled.connect(self.togg16)
    self.r2.toggled.connect(self.togg32)
    
    self.resizes()
       
  def togg16(self):
    global var
    var = True
    self.resizes()

  def togg32(self):
    global var
    var = False
    self.resizes()

  def resizes(self):

    if var == True:
        self.removeButtons()
        self.button = []
        self.row = 16
        self.col = 16
   
    else:
        self.row = 32
        self.col = 32
   
    for r in range(self.row):
      self.button.append( [] )
      for c in range(self.col):
        self.button[r].append( MyButton() )
        self.button[r][c].setFixedSize(20,20)
        self.button[r][c].row = r
        self.button[r][c].col = c
        self.button[r][c].parent = self
        self.button[r][c].revealed = False
        self.alayout.addWidget( self.button[r][c], r, c)
        
  def removeButtons(self):
    for cnt in reversed(range(self.alayout.count())):
        # takeAt does both the jobs of itemAt and removeWidget
        # namely it removes an item and returns it
        widget = self.alayout.takeAt(cnt).widget()

        if widget is not None: 
            # widget will be None if the item is a layout
            widget.deleteLater()

  def newGame(self):

    self.marked = 0
    self.gamestarted = 0
    self.timer.stop()
    self.time = QtCore.QTime(0,0,0)
    self.timelabel.setText("0.0 secs")
    self.bombcount.setText("0/40")

#-----------------------------------------------------
  def updateTime(self):
    tmp = round(self.time.elapsed() / 1000, 1)
    self.timelabel.setText( str(tmp) + " secs" )
#-----------------------------------------------------
  def closeEvent(self, event):
    setting = QtCore.QSettings()
    setting.setValue("position", self.pos())

### Main script
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MainWindow()
    myapp.show()
    sys.exit(app.exec_())
