from PyQt4 import QtGui
from PyQt4 import QtCore
import sys

class myPushButton(QtGui.QPushButton):

  def mouseReleaseEvent(self,event):    
  
      # Mouse Right Button Release Event
      if event.button() == QtCore.Qt.RightButton:
        QtGui.QMessageBox.information(self, "Mouse Right Button Release Detected!","Detected Mouse Right Button Release")   
    
    
def main():    

    app      = QtGui.QApplication(sys.argv)
    pushButton   = myPushButton("My QPushButton")
    
    #Resize width and height
    pushButton.resize(300,120)    
    pushButton.setWindowTitle('PyQT QPushButton: Mouse Right Button Released!')  
    pushButton.show()     

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()