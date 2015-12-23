import sys
from PyQt4.QtCore import * 
from PyQt4.QtGui import * 


class myWin(QMainWindow):
     def __init__(self, parent=None):
         QWidget.__init__(self, parent)
         
     def keyPressEvent(self, event):
         if type(event) == QKeyEvent:
             #here accept the event and do something
             print event.key()
             event.accept()
         else:
             event.ignore()


if __name__ == "__main__":
     app = QApplication(sys.argv)
     mainW = myWin()
     mainW.show()
     sys.exit(app.exec_())