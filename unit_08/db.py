# -*- coding:utf-8 -*-
import os
import sys
from PyQt4.QtCore import (QFile, QString)
from PyQt4.QtGui import QMessageBox
from PyQt4.QtSql import QSqlDatabase
from PyQt4 import QtSql

class Database:
    def __init__(self, dbname, parent = None):
        self.data = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        
        filename = os.path.join(os.path.dirname(__file__), dbname)
        create = not QFile.exists(filename)

        self.data.setDatabaseName(filename)

        if not self.data.open():
            QMessageBox.warning(None, "Reference Data", QString("Database Error: %1").arg(self.data.lastError().text()))
            sys.exit(1)

