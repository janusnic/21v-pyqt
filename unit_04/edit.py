import sys, time
from PyQt4.QtGui import *
from PyQt4 import QtGui, QtCore

class Prog(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        
        self.setWindowTitle('grid layout')

        #Craete line and text area
        self.Line = QtGui.QLabel('Line')
        self.Text = QtGui.QLabel('Text')

        self.LineEdit = QtGui.QLineEdit()
        self.TextEdit = QtGui.QTextEdit()
        
        #checkered layout, 5 - cell spacing
        grid = QtGui.QGridLayout()
        grid.setSpacing(5)

        grid.addWidget(self.Line, 1, 0) #1 and 0 - coordinates
        grid.addWidget(self.LineEdit, 1, 1)

        grid.addWidget(self.Text, 3, 0)
        grid.addWidget(self.TextEdit, 3, 1, 5, 1) # 5,1 - number of columns and cells

        self.setLayout(grid)
        
        #dialog window
        self.button = QtGui.QPushButton('editLine', self)
        grid.addWidget(self.button, 12, 1)
        self.connect(self.button, QtCore.SIGNAL('clicked()'), self.editLine)
        
        self.resize(350, 300)
    

    def editLine(self):
        text, ok = QtGui.QInputDialog.getText(self, 'Input in line', 'Enter string:')

        if ok:
            self.LineEdit.setText(text)
    
app = QtGui.QApplication(sys.argv)
prog = Prog()
prog.show()
sys.exit(app.exec_())