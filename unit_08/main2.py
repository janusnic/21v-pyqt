# -*- coding:utf-8 -*-
import os
import sys
from PyQt4.QtCore import (QVariant, Qt)
from PyQt4.QtGui import (QApplication, QDialog, QTableView, QVBoxLayout)
from PyQt4.QtSql import (QSqlTableModel)
from PyQt4 import QtSql
from db import Database

ID, DATE, TIME, CUSTOMER, ORDER, PRODUCT = range(6)

class OrderDlg(QDialog):

    def __init__(self, parent=None):
        super(OrderDlg, self).__init__(parent)
        self.create_widgets()
        self.layout_widgets()

        self.setMinimumWidth(850)
        self.setWindowTitle(u'Список Order Item')

    def create_widgets(self):

        self.model = QtSql.QSqlRelationalTableModel(self)
        self.model.setTable("CustomerOrder")
        
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
        
        self.model.setRelation(CUSTOMER, QtSql.QSqlRelation('customerview', 'CustomerID', 'Name'))
                
        self.model.setSort(ID, Qt.AscendingOrder)
        self.model.setHeaderData(ID, Qt.Horizontal, QVariant("Order"))
        self.model.setHeaderData(DATE, Qt.Horizontal, QVariant("DATE"))
        self.model.setHeaderData(TIME, Qt.Horizontal, QVariant("TIME"))

        self.model.setHeaderData(CUSTOMER, Qt.Horizontal,
                QVariant("CUSTOMER"))
        
        
        self.model.select()

        self.view = QTableView()
        self.view.setModel(self.model)
        
        self.view.resizeColumnsToContents()

    def layout_widgets(self):
        layout = QVBoxLayout()
        layout.addWidget(self.view)
        self.setLayout(layout)

def main():
    app = QApplication(sys.argv)

    db = Database("myshop.db")
    
    form = OrderDlg()
    form.show()

    sys.exit(app.exec_())

main()
