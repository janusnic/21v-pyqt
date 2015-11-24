import sys
import os.path as osp
from PyQt4 import QtGui
path = osp.join(osp.dirname(sys.modules[__name__].__file__), 'icon.png')

class HelloWorldWindow(QtGui.QMainWindow):
        def __init__(self, parent = None):
                QtGui.QMainWindow.__init__(self, parent)
                self.setWindowTitle("My First Qt Window")
                self.setGeometry(300,300,250,150)
                #base_dir = os.path.dirname(os.path.abspath(__file__))
                #TrayIcon = (r'%s\icons/favicon.ico' % (os.chdir(base_dir)))
                self.setWindowIcon(QtGui.QIcon(path))
                #self.setWindowIcon(QtGui.QPixmap("icons/favicon.ico"))
                self.setToolTip("Hello to this Wiz and Chips example!")

app = QtGui.QApplication(sys.argv)
main_window = HelloWorldWindow()
main_window.show()
app.exec_()