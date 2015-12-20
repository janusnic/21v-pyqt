# -*- coding:utf-8 -*-
import os
import sys
from PyQt4.QtCore import (QFile, QString, QVariant, Qt)
from PyQt4.QtGui import (QApplication, QDialog, QMessageBox, QTableView, QVBoxLayout)
from PyQt4.QtSql import (QSqlDatabase, QSqlTableModel)
from PyQt4 import QtSql

ID, ORDER, PRODUCT = range(3)

class OrderDlg(QDialog):

    def __init__(self, parent=None):
        super(OrderDlg, self).__init__(parent)
        self.create_widgets()
        self.layout_widgets()

        self.setMinimumWidth(850)
        self.setWindowTitle(u'Список Order Item')

    def create_widgets(self):

        self.model = QtSql.QSqlTableModel(self)
        self.model.setTable("OrderItem")
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
        
        self.model.setSort(ID, Qt.AscendingOrder)
        self.model.setHeaderData(ID, Qt.Horizontal, QVariant("Order Item"))

        self.model.setHeaderData(ORDER, Qt.Horizontal,
                QVariant("Order"))
        self.model.setHeaderData(PRODUCT, Qt.Horizontal,
                QVariant("Product"))
        
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

    filename = os.path.join(os.path.dirname(__file__), "myshop.db")
    create = not QFile.exists(filename)

    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName(filename)
    if not db.open():
        QMessageBox.warning(None, "Reference Data",
            QString("Database Error: %1").arg(db.lastError().text()))
        sys.exit(1)

    form = OrderDlg()
    form.show()

    sys.exit(app.exec_())

main()
