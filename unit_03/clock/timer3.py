#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys

class myLCDNumber(QLCDNumber):

  @pyqtSlot()
  def showTime(self):
    #Show Current Time in "hh:mm:ss" format
    self.display(QTime.currentTime().toString(QString("hh:mm:ss")))
    

def main():    
    app      = QApplication(sys.argv)
    lcdNumber    = myLCDNumber()
    timer    = QTimer()

    #Resize width and height
    lcdNumber.resize(250,250)    
    lcdNumber.setWindowTitle("PyQt QLcdNumber-Current Time")  
    lcdNumber.setDigitCount(8)
    
    lcdNumber.connect(timer,SIGNAL("timeout()"),lcdNumber,SLOT("showTime()"))
    timer.start(1000) 

    lcdNumber.show()    
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()