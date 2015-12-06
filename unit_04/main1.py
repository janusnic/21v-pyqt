# -*- coding: utf-8 -*-
# пример без использования дизайнера, все Gui определяется тут
from PyQt4 import QtCore
from PyQt4 import QtGui
# создадим "алиас" для этого метода, чтобы писать меньше кода
fromUtf8 = QtCore.QString.fromUtf8

class Ui(QtGui.QWidget):
    def __init__(self, parent=None):
        super(Ui,self).__init__(parent)
        # Меняем заголовок у окна, обратите внимание,
        # что кириллицу нельзя указывать напрямую
        # только через QString, тут мы и исползуем
        # алиас fromUtf8
        self.setWindowTitle(fromUtf8('Пример'))
        # Определяем компоновщик элементов, с ним
        # приложение будет опрятнее, в данном случае
        # используется табличный компоновщик, в который
        # мы позже разместим элементы интерфейса
        self.layout = QtGui.QGridLayout()
        # создаем два виджета текстового редактирования
        # левый и правый
        self.leftText = QtGui.QTextEdit()
        self.rightText = QtGui.QTextEdit()
        # Создаем виджет - кнопку
        self.buttonForward = QtGui.QPushButton()
        # меняем ее текст
        self.buttonForward.setText(fromUtf8('туда ->'))
        self.buttonBack = QtGui.QPushButton()
        self.buttonBack.setText(fromUtf8('<- сюда'))
        # Располагаем в компоновщике элементы
        # представьте себе таблицу 2х2
        # в первой ячейке размещается leftText, который
        # занимает одну ячейку
        self.layout.addWidget(self.leftText,  0, 0, 1, 1)
        self.layout.addWidget(self.rightText,  0, 1, 1, 1)
        self.layout.addWidget(self.buttonForward, 1, 0, 1, 1)
        self.layout.addWidget(self.buttonBack, 1, 1, 1, 1)
        # применяем компоновку
        self.setLayout(self.layout)
        # соединяем сигналы со слотами
        # в конкретном случае мы сами определили слоты forward и back
        self.connect(self.buttonForward, QtCore.SIGNAL("clicked()"), self.forward)
        self.connect(self.buttonBack, QtCore.SIGNAL("clicked()"), self.back)
        # в forward() и back() мы просто работаем с "родными методами" Qt
    def forward(self):
        self.leftText.selectAll()
        self.leftText.cut()
        self.rightText.clear()
        self.rightText.paste()
    def back(self):
        self.rightText.selectAll()
        self.rightText.cut()
        self.leftText.clear()
        self.leftText.paste()
      
if __name__=='__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    exampleWindow = Ui()
    exampleWindow.show()
    sys.exit(app.exec_())
