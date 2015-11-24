import sys
from PyQt4 import QtGui, QtCore
 
def main():
    app = QtGui.QApplication(sys.argv)
    heartXPM = ['7 6 2 1','N c None','. c #e2385a','N..N..N',\
    '.......','.......','N.....N','NN...NN','NNN.NNN']
    w = QtGui.QWidget()
    w.setWindowTitle('XPM Test')
    w.setWindowIcon(QtGui.QIcon(QtGui.QPixmap(heartXPM)))
    w.button = QtGui.QPushButton('XPM Bitmaps', w)
    w.button.setIcon(QtGui.QIcon(QtGui.QPixmap(heartXPM)))
    w.button.setIconSize(QtCore.QSize(24,24))
    w.show()
 
    sys.exit(app.exec_())
 
if __name__ == '__main__':
    main()