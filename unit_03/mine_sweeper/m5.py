#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Mine Sweeper Game
"""
import sys
import os
import random
from PyQt4 import QtCore, QtGui

class MyButton(QtGui.QPushButton):
  def __init__(self, parent=None):
    super(MyButton, self).__init__(parent)

class MainWindow(QtGui.QWidget):
  """ Main Wrapper For GUI """
  def __init__(self, parent=None):
    super(MainWindow, self).__init__(parent)
    setting = QtCore.QSettings()
    tmp = setting.value("position", QtCore.QPoint(0,0))

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

    layouttop = QtGui.QHBoxLayout()
    layouttop.addWidget(QtGui.QLabel("BombCount"))
    self.bombcount = QtGui.QLabel("0/40")
    layouttop.addWidget(self.bombcount)
    self.timer = QtCore.QTimer()
    self.timelabel = QtGui.QLabel("0.0 secs")
    self.timelabel.setStyleSheet("background-color: rgb(0, 0, 0); color: rgb(0,255,0)")
    self.newGame()
    layouttop.addWidget(self.timelabel)
    newgameButton = QtGui.QPushButton("&NewGame")
    newgameButton.setEnabled(True)
    layouttop.addWidget(newgameButton)
    topscore = QtGui.QPushButton("Top&Score>>")
    topscore.setCheckable(True)
    layouttop.addWidget(topscore)
    self.scoreframe = QtGui.QFrame()
    self.scoreframe.setFrameStyle(QtGui.QFrame.StyledPanel|QtGui.QFrame.Sunken)
    scorelayout = QtGui.QVBoxLayout()
    scorelayout.addWidget(QtGui.QLabel(u"<b>Игра «Сапёр»</b> <i>Данное приложение является реализацией игры «Сапёр» <br>и может быть использовано как по прямому назначению, <br>так и в качестве reference solution.</i> <br>" ) )
    self.scoreframe.setLayout(scorelayout)
    self.scoreframe.setVisible(False)
    mainLayout = QtGui.QGridLayout()
    mainLayout.addLayout(layouttop,0,0)
    mainLayout.addLayout(layout,1,0)
    mainLayout.addWidget(self.scoreframe,0,1,2,1)
    self.setLayout(mainLayout)
    self.layout().setSizeConstraint(QtGui.QLayout.SetFixedSize)
    QtCore.QObject.connect(newgameButton, QtCore.SIGNAL("clicked()"), self.newGame)
    QtCore.QObject.connect(self.timer, QtCore.SIGNAL("timeout()"), self.updateTime)
    QtCore.QObject.connect(topscore, QtCore.SIGNAL("clicked(bool)"), self.scoreframe.setVisible )

#-----------------------------------------------------
#-----------------------------------------------------
#-----------------------------------------------------
  def newGame(self):
    self.populateBombs()
    self.marked = 0
    self.gamestarted = 0
    self.timer.stop()
    self.time = QtCore.QTime(0,0,0)
    self.timelabel.setText("0.0 secs")
    self.bombcount.setText("0/40")

    for r in range(16):
      for c in range(16):
        self.button[r][c].revealed  = False
        self.button[r][c].setText("")
        self.button[r][c].setFlat(False)
        self.button[r][c].setEnabled(True)
        self.button[r][c].setPalette(QtGui.QPalette(QtGui.QColor(222,222,222)))
#-----------------------------------------------------
  def updateTime(self):
    tmp = round(self.time.elapsed() / 1000, 1)
    self.timelabel.setText( str(tmp) + " secs" )
#-----------------------------------------------------
  def closeEvent(self, event):
    setting = QtCore.QSettings()
    setting.setValue("position", self.pos())
#-----------------------------------------------------
  def populateBombs(self):
    bomblocation = random.sample(range(256), 40)
    x = 0
    for r in range(16):
      for c in range(16):
        self.button[r][c].bomb = True if x in bomblocation else False
        x = x + 1

### Main script
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MainWindow()
    myapp.show()
    sys.exit(app.exec_())
#__________________________________________________________________________
#__________________________________________________________________________