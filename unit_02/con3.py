##!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Code PyQt4

In this example, we create a simple
window in PyQt4.

"""
from PyQt4 import QtCore, QtGui
class MyWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.button1 = QtGui.QPushButton(u"Кнопка 1. Нажми меня")
        self.button2 = QtGui.QPushButton(u"Кнопка 2")
        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(self.button1)
        vbox.addWidget(self.button2)
        self.setLayout(vbox)
        self.resize(300, 100)
        # Передача сигнала от кнопки 1 к кнопке 2
        self.connect(self.button1, QtCore.SIGNAL("clicked()"), self.button2, QtCore.SIGNAL('clicked()'))
        # Способ 1 (4 параметра)
        self.connect(self.button2, QtCore.SIGNAL("clicked()"), self, QtCore.SLOT("on_clicked_button2()"))
        # Способ 2 (3 параметра)
        self.connect(self.button2, QtCore.SIGNAL("clicked()"), QtCore.SLOT("on_clicked_button2()"))
    @QtCore.pyqtSlot()
    def on_clicked_button2(self):
        print("Сигнал получен кнопкой 2")


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())