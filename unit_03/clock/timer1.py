#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4.QtGui import * 
from PyQt4.QtCore import * 
import sys

class myLCDNumber(QLCDNumber):
  value = 60
  # Следующий метод (слот) вызывется при каждом переполнении таймера  
  @pyqtSlot()
  def count(self):
    self.display(self.value)
    self.value = self.value-1


def main():    
    app      = QApplication(sys.argv)
    lcdNumber    = myLCDNumber()

    # Изменяем width и height
    lcdNumber.resize(250,250)    
    lcdNumber.setWindowTitle(u'PyQt QTimer Секундомер')
    # Обновляем значение времени на форме  
    lcdNumber.display(60)
    # Создаем экземплят объекта
    timer = QTimer()
    # Связываем сигнал переполнения таймера со слотом
    lcdNumber.connect(timer,SIGNAL("timeout()"),lcdNumber,SLOT("count()"))
    # Задаем время срабатывания таймера (в мс)
    timer.start(1000) 

    lcdNumber.show()    
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()