# -*- coding:utf-8 -*-

from PyQt4.QtSql import *

class SQLConnection:
    def __init__(self, path, parent = None):
        self.path = path
        self.db = None

    def open_database(self):
        if self.db:
            self.close_database()

        self.db = QSqlDatabase.addDatabase("QSQLITE")
        
        self.db.setDatabaseName(self.path)
        ok = self.db.open()
        return ok

    def close_database(self):
        """closes the datbase that is currently open"""
        
        self.db.close()
        QSqlDatabase.removeDatabase("conn")

    def closeEvent(self, event):
        """closes the database if a close event occurs -
        such as close window/quit application"""
        self.close_database()

    #customer queries
    def add_new_customer(self,details):
        query = QSqlQuery()
        query.prepare("""INSERT INTO customer (FirstName,LastName,Street,Town,PostCode,TelephoneNumber) VALUES
                        (?,?,?,?,?,?)""")
        query.addBindValue(details['first_name'])
        query.addBindValue(details['last_name'])
        query.addBindValue(details['street'])
        query.addBindValue(details['town'])
        query.addBindValue(details['post_code'])
        query.addBindValue(details['telephone'])
        query.exec_()

    def current_products(self):
        model = QSqlRelationalTableModel()
        print(self.db.tables())
        model.setTable(self.db.tables()[2])
        model.setRelation(3,QSqlRelation("ProductType","ProductTypeID","Description"))
        model.select()
        return model

