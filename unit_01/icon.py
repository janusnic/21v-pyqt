import sys
import os.path as osp
from PyQt4 import QtGui

#setting the path variable for icon
path = osp.join(osp.dirname(sys.modules[__name__].__file__), 'icon.png')

class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Icon_test')
        self.setWindowIcon(QtGui.QIcon(path))        

        self.show()

def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()