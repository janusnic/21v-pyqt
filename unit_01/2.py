#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

"""
Code PyQt4

In this example, we create a simple
window in PyQt4.

"""

import sys
from PyQt4 import QtGui, QtCore

# set app icon    

app_icon = QtGui.QIcon()
# app_icon.addFile('gui/icons/24x24.png', QtCore.QSize(24,24))
#app_icon.addFile('gui/icons/32x32.png', QtCore.QSize(32,32))
#app_icon.addFile('gui/icons/48x48.png', QtCore.QSize(48,48))
#app_icon.addFile('gui/icons/256x256.png', QtCore.QSize(256,256))
#app.setWindowIcon(app_icon)

class Example(QtGui.QMainWindow):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()


    def initUI(self):

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Icon')
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":./icon.png"), QtGui.QIcon.Normal)
        self.setWindowIcon(QtGui.QIcon(icon2))

        heartXPM = ['7 6 2 1','N c None','. c #e2385a','N..N..N','.......','.......','N.....N','NN...NN','NNN.NNN']

        #self.setWindowIcon(QtGui.QIcon(heartXPM))
        
        # self.setWindowIcon(app_icon)
        
        self.show()


def main():

    app = QtGui.QApplication(sys.argv)
    

    # ico = QtGui.QIcon('icons/web.png')
    
    # app_icon.addFile('icons/web.png', QtCore.QSize(32,32))

    # app.setWindowIcon(app_icon)
    ex = Example()
    # ex.setWindowIcon(QtGui.QIcon(':/icons/web.png'))

    ex.show()


    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
