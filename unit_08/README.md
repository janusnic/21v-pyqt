# 21v-pyqt

Работа с базами данных в Qt
===========================

Соединение с базой данных
--------------------------
Чтобы получить доступ к базе данных с помощью QSqlQuery и QSqlQueryModel, создайте и откройте одно или более соединений с базой данных. Соединения с базой данных обычно идентифицируется по имени соединения, а не по имени базы данных. Вы можете иметь множество соединений с одной и той же базой данных. QSqlDatabase также поддерживает концепцию соединения по умолчанию, которое является неименованным. Когда вызываются функции-члены QSqlQuery или QSqlQueryModel, которые получают имя соединения как аргумент, то если вы не указываете имя соединения, будет использоваться соединение по умолчанию. Создание соединения по умолчанию удобно, когда вашему приложению требуется только одно соединение с базой данных.

Обратите внимание на отличие между созданием соединения и его открытием. Создание соединения включает в себя создание экземпляра класса QSqlDatabase. Соединение не пригодно к использованию до тех пор, пока оно не будет открыто.


Qt может работать со следующими базами данных (из-за несовместимости с GPL лицензией, не все плагины поставляются с Qt Open Source Edition):
- QDB2 — IBM DB2 (версия 7.1 и выше
- QIBASE — Borland InterBase
- QMYSQL — MySQL
- QOCI — Драйвер Oracle Call Interface
- QODBC — Open Database Connectivity (ODBC) — Microsoft SQL Server и другие ODBC-совместимые базы данных
- QPSQL — PostgreSQL (версия 7.3 и выше)
- QSQLITE2 — SQLite версии 2
- QSQLITE — SQLite версии 3
- QTDS — Драйвер Sybase Adaptive Server

Соединиться с базой данных можно вот так:
-----------------------------------------
```
   filename = os.path.join(os.path.dirname(__file__), "myshop.db")
    create = not QFile.exists(filename)

    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName(filename)
    if not db.open():
        QMessageBox.warning(None, "Reference Data",
            QString("Database Error: %1").arg(db.lastError().text()))
        sys.exit(1)
```

строка db = QSqlDatabase.addDatabase("QSQLITE") создает объект соединения, а db.open() открывает его. В промежутке инициализируется некоторая информация о соединении, включая имя соединения, имя базы данных, имя узла, имя пользователя, пароль. 

Если open() потерпит неудачу, он вернет false. В этом случае, можно получить информацию об ошибке, вызвав db.lastError().
```
if not db.open():
        QMessageBox.warning(None, "Reference Data",
            QString("Database Error: %1").arg(db.lastError().text()))
        sys.exit(1)
```

Для удаления соединения с базой данных, надо сначала закрыть базу данных с помощью db.close(), а затем, удалить соединение с помощью статического метода db.removeDatabase().

Работа с базами данных в Qt:
----------------------------
1.Слой драйверов — Включает классы QSqlDriver, QSqlDriverCreator, QSqlDriverCreatorBase, QSqlDriverPlugin и QSqlResult. Этот слой предоставляет низкоуровневый мост между определенными базами данных и слоем SQL API.

2.Слой SQL API — Этот слой предоставляет доступ к базам данных. Соединения устанавливаются с помощью класса QSqlDatabase. Взаимодействие с базой данных осуществляется с помощью класса QSqlQuery. В дополнение к классам QSqlDatabase и QSqlQuery слой SQL API опирается на классы QSqlError, QSqlField, QSqlIndex и QsqlRecord.

3.Слой пользовательского интерфейса — Этот слой связывает данные из базы данных с дата-ориентироваными виджетами. Сюда входят такие классы, как QSqlQueryModel, QSqlTableModel и QSqlRelationalTableModel.

Модель таблицы SQL Класс QSqlTableModel
----------------------------------------

QSqlTableModel предлагает модель для чтения и записи, которая работает одновременно только с одной таблицей SQL.

QSqlTableModel - это высокоуровневый интерфейс к записям одной таблицы базы данных с возможностью и чтения и записи. Он является надстройкой нижнего уровня QSqlQuery и может быть использован, чтобы предоставлять данные для классов представлений, таких как QTableView. 

Класс QTableView предоставляет реализацию модель / представление (по умолчанию представления) таблицы.

Мы устанавливаем имя SQL таблицы и стратегию редактирования, затем мы устанавливаем метки отображаемые в заголовках представления. 
```
    def create_widgets(self):

        self.model = QtSql.QSqlTableModel(self)
        self.model.setTable("OrderItem")
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)

```
Стратегия редактирования
------------------------
Стратегия редактирования предписывает, когда изменения сделанные пользователем в представлении применяются в базе данных. Возможные значения стратегии - это OnFieldChange, OnRowChange и OnManualSubmit.

QSqlTableModel - это высокоуровневая альтернатива QSqlQuery для изменения отдельной SQL таблицы и навигации по ней. Обычно это требует меньше кода и не требует знания SQL синтаксиса.

Для получения строки таблицы используйте QSqlTableModel.record(), а для ее изменения - QSqlTableModel.setRecord(). 

Для доступа к данным вы можете также использовать QSqlTableModel.data() и QSqlTableModel.setData(), которые унаследованы от QAbstractItemModel.

После окончания редактирования записи, вы должны вызвать QSqlTableModel.submitAll() для того, чтобы гарантировать запись изменений в базу данных.

Когда и необходимо ли вообще вам вызывать submitAll(), зависит от стратегии редактирования таблицы. По умолчанию установлена стратегия QSqlTableModel.OnRowChange, которая указывает, что произведенные изменения будут внесены в базу данных при выборе пользователем другой строки. Другие стратегии - это QSqlTableModel.OnManualSubmit (все изменения кэшируются в модели до вызова submitAll()) и QSqlTableModel.OnFieldChange (где изменения не кэшируются). Они, в основном, полезны, когда используется QSqlTableModel с представлением.

Хотя кажется, что QSqlTableModel.OnFieldChange обещает, что вам никогда не придется вызывать submitAll(). Есть два нюанса:

Без кэширования может снизиться скорость работы.
Если вы изменили первичный ключ, то запись может ускользнуть от вас, пока вы пытаетесь ее заполнить.

Отображение данных в таблице-представлении
------------------------------------------
Классы QSqlQueryModel, QSqlTableModel и QSqlRelationalTableModel могут использоваться в качестве источников данных для классов представлений Qt, таких как QListView, QTableView и QTreeView. На практике наиболее часто используется QTableView в связи с тем, что результирующая SQL выборка, по существу, представляет собой двумерную структуру данных.

Если модель является моделью для чтения-записи (например, QSqlTableModel), то представление позволяет редактировать поля. 

Можно использовать одну и ту-же модель в качестве источника данных для нескольких представлений. Если пользователь изменяет данные модели с помощью одного из представлений, другие представления немедленно отобразят изменения.

Классы-представления для обозначения колонок наверху отображают заголовки. Для изменения текста заголовка, используется функция setHeaderData() модели. 

Например:
```
ID, ORDER, PRODUCT = range(3)

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

```
QTableView также имеет вертикальные заголовки слева, содержащие номера строк. Если вы программно вставляете строки с помощью QSqlTableModel.insertRows(), новые колонки будут обозначены звездочкой (*) до тех пор, пока они не будут помещены в базу данных с помощью submitAll() или автоматически при переходе пользователя к другой записи (если стратегия редактирования равна QSqlTableModel.OnRowChange).

Аналогично, если вы удаляете строки с помощью removeRows(), они будут отмечены восклицательным знаком (!), пока изменения не будут внесены в базу данных.

Элементы представления отображаются с помощью делегата. Делегат по умолчанию QItemDelegate содержит большинство общих типов данных (int, QString, QImage и т.д.). Также делегат отвечает за предоставление виджета-редактора (например, combobox), когда пользователь начинает редактировать элемент представления. Вы можете создавать свои собственные делегаты, наследуя QAbstractItemDelegate или QItemDelegate. 

QSqlTableModel оптимизирован для работы с одной таблицей в один момент времени. Если Вам нужна модель для чтения-записи, которая может работать с произвольной результирующей выборкой, вы можете создать подкласс QSqlQueryModel и переопределить flags() и setData() для возможности осуществлять чтение-запись.

Создание подклассов модели делает возможной настройку собственной модели различными способами: вы можете предоставить подсказки к элементам, изменить цвет фона, отобразить вычисляемые значения, разрешать различным значениям быть отображенными и отредактированными, отдельно обработать нулевые значения и т.д. 

main1.py:
---------
```
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

```

Модель реляционной таблицы SQL
==============================
QSqlRelationalTableModel
------------------------

Если вам требуется разрешить внешний ключ для более понятного представления, вы можете использовать QSqlRelationalTableModel. Для получения лучшего результата, вам следует использовать делегат QSqlRelationalDelegate, который предоставляет для изменения значения внешнего ключа виджет-редактор в виде выпадающего списка.

QSqlRelationalTableModel расширяет QSqlTableModel для предоставления поддержки внешних ключей. Внешний ключ - это связь один-к-одному, установленная между полем одной таблицы и полем первичного ключа другой таблицы. 

QSqlRelationalTableModel используется для работы с таблицами которые имеют поле foreign key. Для работы с foreign key достаточно использовать метод setRelation с параметрами состоящими из номера поля, таблицы от куда подставляют значения, поле идентификатора и поле  значений идентификатора. Также при использовании QSqlRelationalTableModel есть возможность использовать QComboBox в связанных полях в QTableView. Для этого нужно использовать метод setItemDelegate класса QTableView.

create view customerview
-------------------------
```
create view customerview as select CustomerID, ("FirstName" || " " || "LastName") AS Name, Street, Town, PostCode, TelephoneNumber from Customer;
```
db.py
--------
```
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
```
main2.py
--------
```
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

```

main3.py создаем Layout
------------------------
```
# -*- coding:utf-8 -*-
import os
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class ShopWindow(QMainWindow):
    def __init__(self, parent=None):
        super(ShopWindow, self).__init__(parent)

        self.setMinimumWidth(850)
        self.setWindowTitle(u'Магазин Все Продается')

        # create actions - these can be used in menus/toolbars etc.
        self.open_database = QAction("Open Database",self)
        self.close_database = QAction("Close Database",self)
        self.add_customer = QAction("Add Customer",self)
        self.browse_customers = QAction("Browse Customers",self)
        self.add_order = QAction("Add Order",self)
        self.browse_orders = QAction("Browse Orders",self)
        self.add_product = QAction("Add Product",self)
        self.browse_products = QAction("Browse Products",self)

        # создаем menubar
        self.menu_bar = self.menuBar()
        self.database_menu = self.menu_bar.addMenu("Database")
        self.customer_menu = self.menu_bar.addMenu("Customer")
        self.order_menu = self.menu_bar.addMenu("Order")
        self.product_menu = self.menu_bar.addMenu("Product")


        #add the actions to the menubar
        self.database_menu.addAction(self.open_database)
        self.database_menu.addAction(self.close_database)
        self.customer_menu.addAction(self.add_customer)
        self.customer_menu.addAction(self.browse_customers)
        self.order_menu.addAction(self.add_order)
        self.order_menu.addAction(self.browse_orders)
        self.product_menu.addAction(self.add_product)
        self.product_menu.addAction(self.browse_products)

        # создаем toolbars
        self.database_toolbar = QToolBar("Manage Databases")
        self.customer_toolbar = QToolBar("Manage Customers")
        self.order_toolbar = QToolBar("Manage Orders")
        self.product_toolbar = QToolBar("Manage Products")

        # добавим toolbars к window
        self.addToolBar(self.database_toolbar)
        self.addToolBar(self.customer_toolbar)
        self.addToolBar(self.order_toolbar)
        self.addToolBar(self.product_toolbar)

        #add actions to toolbars
        self.database_toolbar.addAction(self.open_database)
        self.database_toolbar.addAction(self.close_database)
        self.customer_toolbar.addAction(self.add_customer)
        self.customer_toolbar.addAction(self.browse_customers)
        self.order_toolbar.addAction(self.add_order)
        self.order_toolbar.addAction(self.browse_orders)
        self.product_toolbar.addAction(self.add_product)
        self.product_toolbar.addAction(self.browse_products)

        #connections
        self.open_database.triggered.connect(self.openDatabase)
        self.add_customer.triggered.connect(self.addCustomer)
        self.add_order.triggered.connect(self.addOrder)

    def openDatabase(self):
        pass

    def addCustomer(self):
        pass

    def saveCustomer(self):
        pass

    def addOrder(self):
        pass

def main():
    app = QApplication(sys.argv)
    window = ShopWindow()
    window.show()
    window.raise_()
    sys.exit(app.exec_())

main()

```

sqldb.py SQLConnection
-----------------------

```
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


```

main4.py openDatabase
----------------------
```
# -*- coding:utf-8 -*-
import os
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from sqldb import *

class ShopWindow(QMainWindow):
    def __init__(self, parent=None):
        super(ShopWindow, self).__init__(parent)

        self.setMinimumWidth(850)
        self.setWindowTitle(u'Магазин Все Продается')

        #create actions - these can be used in menus/toolbars etc.
        self.open_database = QAction("Open Database",self)
        self.close_database = QAction("Close Database",self)
        self.add_customer = QAction("Add Customer",self)
        self.browse_customers = QAction("Browse Customers",self)
        self.add_order = QAction("Add Order",self)
        self.browse_orders = QAction("Browse Orders",self)
        self.add_product = QAction("Add Product",self)
        self.browse_products = QAction("Browse Products",self)

        # создаем menubar
        self.menu_bar = self.menuBar()
        self.database_menu = self.menu_bar.addMenu("Database")
        self.customer_menu = self.menu_bar.addMenu("Customer")
        self.order_menu = self.menu_bar.addMenu("Order")
        self.product_menu = self.menu_bar.addMenu("Product")


        #add the actions to the menubar
        self.database_menu.addAction(self.open_database)
        self.database_menu.addAction(self.close_database)
        self.customer_menu.addAction(self.add_customer)
        self.customer_menu.addAction(self.browse_customers)
        self.order_menu.addAction(self.add_order)
        self.order_menu.addAction(self.browse_orders)
        self.product_menu.addAction(self.add_product)
        self.product_menu.addAction(self.browse_products)

        # создаем toolbars
        self.database_toolbar = QToolBar("Manage Databases")
        self.customer_toolbar = QToolBar("Manage Customers")
        self.order_toolbar = QToolBar("Manage Orders")
        self.product_toolbar = QToolBar("Manage Products")

        # добавим toolbars к window
        self.addToolBar(self.database_toolbar)
        self.addToolBar(self.customer_toolbar)
        self.addToolBar(self.order_toolbar)
        self.addToolBar(self.product_toolbar)

        #add actions to toolbars
        self.database_toolbar.addAction(self.open_database)
        self.database_toolbar.addAction(self.close_database)
        self.customer_toolbar.addAction(self.add_customer)
        self.customer_toolbar.addAction(self.browse_customers)
        self.order_toolbar.addAction(self.add_order)
        self.order_toolbar.addAction(self.browse_orders)
        self.product_toolbar.addAction(self.add_product)
        self.product_toolbar.addAction(self.browse_products)

        #connections
        self.open_database.triggered.connect(self.openDatabase)
        self.add_customer.triggered.connect(self.addCustomer)
        self.add_order.triggered.connect(self.addOrder)

    def openDatabase(self):
        path = QFileDialog.getOpenFileName(caption="Open Database",filter="Database file (*.db *.dat)")
        self.connection = SQLConnection(path)
        self.connection.open_database()

    def addCustomer(self):
        pass

    def saveCustomer(self):
        pass
    def addOrder(self):
        pass


def main():
    app = QApplication(sys.argv)
    window = ShopWindow()
    window.show()
    window.raise_()
       
    sys.exit(app.exec_())

main()

```
main5.py addCustomer
--------------------
```
    def addCustomer(self):
        self.add_customer_widget = AddCustomerWidget()
        self.setCentralWidget(self.add_customer_widget)
        #connect the custom signal in the widget to our method
        self.add_customer_widget.customerAddedSignal.connect(self.saveCustomer)
```

AddCustomerWidget add_customer.py
----------------------------------
```
# -*- coding:utf-8 -*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class AddCustomerWidget(QWidget):
    #customer signal to fire when details added
    customerAddedSignal = pyqtSignal()

    def __init__(self, parent=None):
        super(AddCustomerWidget, self).__init__(parent)

        #create widgets
        self.title_label = QLabel("Add New Customer")

        self.first_name_label = QLabel("First Name")
        self.last_name_label = QLabel("Last Name")
        self.house_no_label = QLabel("House Number")
        self.street_label = QLabel("Street")
        self.town_label = QLabel("Town")
        self.post_code_label = QLabel("Post Code")
        self.telephone_label = QLabel("Telephone")
        self.email_label = QLabel("E-Mail")

        self.first_name_edit = QLineEdit()
        self.last_name_edit = QLineEdit()
        self.house_no_edit = QLineEdit()
        self.street_edit = QLineEdit()
        self.town_edit = QLineEdit()
        self.post_code_edit = QLineEdit()
        self.telephone_edit = QLineEdit()
        self.email_edit = QLineEdit()

        self.clear_button = QPushButton("Clear")
        self.save_button = QPushButton("Save")

        #layouts
        self.layout = QVBoxLayout()
        self.details_layout = QGridLayout()

        self.details_layout.addWidget(self.first_name_label,0,0)
        self.details_layout.addWidget(self.first_name_edit,0,1)
        self.details_layout.addWidget(self.last_name_label,0,2)
        self.details_layout.addWidget(self.last_name_edit,0,3)

        self.details_layout.addWidget(self.house_no_label,1,0)
        self.details_layout.addWidget(self.house_no_edit,1,1)
        self.details_layout.addWidget(self.street_label,1,2)
        self.details_layout.addWidget(self.street_edit,1,3)
        self.details_layout.addWidget(self.town_label,2,0)
        self.details_layout.addWidget(self.town_edit,2,1)
        self.details_layout.addWidget(self.post_code_label,2,2)
        self.details_layout.addWidget(self.post_code_edit,2,3)
        self.details_layout.addWidget(self.telephone_label,3,0)
        self.details_layout.addWidget(self.telephone_edit,3,1)
        self.details_layout.addWidget(self.email_label,3,2)
        self.details_layout.addWidget(self.email_edit,3,3)
        self.details_layout.addWidget(self.save_button,4,1)
        self.details_layout.addWidget(self.clear_button,4,0)

        self.layout.addWidget(self.title_label)
        self.layout.addLayout(self.details_layout)
        self.setLayout(self.layout)

        #connections
        self.clear_button.clicked.connect(self.clear_details)
        self.save_button.clicked.connect(self.save_details)

    def save_details(self):
        self.customerAddedSignal.emit()

    def clear_details(self):
        self.first_name_edit.clear()
        self.last_name_edit.clear()
        self.house_no_edit.clear()
        self.street_edit.clear()
        self.town_edit.clear()
        self.post_code_edit.clear()
        self.telephone_edit.clear()
        self.email_edit.clear()

    def customer_details(self):
        details = {'first_name':self.first_name_edit.text(),
                    'last_name':self.last_name_edit.text(),
                    'house_number':self.house_no_edit.text(),
                    'street':self.street_edit.text(),
                    'town':self.town_edit.text(),
                    'post_code':self.post_code_edit.text(),
                    'telephone':self.telephone_edit.text(),
                    'email':self.email_edit.text()}
        return details
```

main6.py saveCustomer
---------------------
```
    def saveCustomer(self):
        details = self.add_customer_widget.customer_details()
        self.connection.add_new_customer(details)
        self.add_customer_widget.clear_details()

```
Выполнение инструкций SQL
-------------------------
Класс QSqlQuery обеспечивает интерфейс для выполнения SQL запросов и навигации по результирующей выборке. Для выполнения SQL запросов, просто создают объект QSqlQuery и вызывают QSqlQuery.exec_(). 
```
            query = QSqlQuery()
            query.prepare("""INSERT INTO customer (FirstName,LastName,Street,Town,PostCode,TelephoneNumber) VALUES(?,?,?,?,?,?)""")
            query.exec_()

```
Конструктор QSqlQuery принимает необязательный аргумент QSqlDatabase, который уточняет, какое соединение с базой данных используется. Если его не указать, то используется соединение по умолчанию. Если возникает ошибка, exec() возвращает false. Доступ к ошибке можно получить с помощью QSqlQuery.lastError().

QSqlQuery предоставляет единовременный доступ к результирующей выборке одного запроса. После вызова exec(), внутренний указатель QSqlQuery указывает на позицию перед первой записью. Если вызвать метод QSqlQuery.next() один раз, то он переместит указатель к первой записи. После этого необходимо повторять вызов next(), чтобы получать доступ к другим записям, до тех пор пока он не вернет false. 

QSqlQuery может выполнять не только SELECT, но также и любые другие запросы. 

При вставке множества записей требуется вызвать QSqlQuery.prepare() только однажды. Далее можно вызвать bindValue() или addBindValue() с последующим вызовом exec() столько раз, сколько потребуется.

sqldb.py add_new_customer
-------------------------

```
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
```


addOrder main7.py
---------
```
def addOrder(self):
        self.add_order_widget = CustomerOrderWidget(self.connection)
        self.setCentralWidget(self.add_order_widget)
```
CustomerOrderWidget
-------------------
```
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from find_customer import *
from create_order import *

class CustomerOrderWidget(QWidget):
    """creates a form allowing you to create an order for a particular customer"""
    def __init__(self, connection, **kwargs):
        super(CustomerOrderWidget, self).__init__(**kwargs)
        self.connection = connection

        self.customer = FindCustomerWidget(self.connection)
        self.order = OrderWidget(self.connection)
        self.confirm_order = QPushButton("Confirm Order")

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.customer)
        self.layout.addWidget(self.order)
        self.layout.addWidget(self.confirm_order)

        self.setLayout(self.layout)

        #connections
        self.customer.createdNewOrder.connect(self.new_order)

    def new_order(self):
        order_details = self.customer.most_recent_created_order_details()
        self.order.order_details = order_details
        self.order.enable_selection()

```

find_customer.py
----------------
```
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class FindCustomerWidget(QWidget):
    """finds and displays all customers with given values"""

    #fire when order created
    createdNewOrder = pyqtSignal()

    def __init__(self,connection,**kwargs):
        super(FindCustomerWidget,self).__init__(**kwargs)

        self.connection = connection

        self.stacked_layout = QStackedLayout()
        self.setLayout(self.stacked_layout)
        self.find_customer_layout()


        #connections
        self.radio_button_group.buttonClicked.connect(self.change_search)
        self.find_customer_button.clicked.connect(self.find_customer)

    def find_customer_layout(self):
        #create widgets
        self.customer_number_label = QLabel("Customer Number")
        self.customer_first_name_label = QLabel("First Name")
        self.customer_last_name_label = QLabel("Last Name")
        self.customer_house_number_label = QLabel("House No")
        self.customer_postcode_label = QLabel("Postcode")

        self.customer_number_edit = QLineEdit()
        self.customer_first_name_edit = QLineEdit()
        self.customer_first_name_edit.setEnabled(False)
        self.customer_last_name_edit = QLineEdit()
        self.customer_last_name_edit.setEnabled(False)
        self.customer_house_number_edit = QLineEdit()
        self.customer_house_number_edit.setEnabled(False)
        self.customer_postcode_edit = QLineEdit()
        self.customer_postcode_edit.setEnabled(False)

        self.find_customer_button = QPushButton("Find Customer")

        self.radio_button_box = QGroupBox()
        self.radio_button_group = QButtonGroup()

        self.number_radio = QRadioButton()
        self.postcode_radio = QRadioButton()
        self.name_radio = QRadioButton()

        self.number_radio.setChecked(True)

        self.radio_button_group.addButton(self.number_radio)
        self.radio_button_group.setId(self.number_radio,0)
        self.radio_button_group.addButton(self.name_radio)
        self.radio_button_group.setId(self.name_radio,1)
        self.radio_button_group.addButton(self.postcode_radio)
        self.radio_button_group.setId(self.postcode_radio,2)


        self.customer_number_layout = QGridLayout()
        self.customer_number_layout.addWidget(self.customer_number_label,0,0)
        self.customer_number_layout.addWidget(self.customer_number_edit,0,1)

        self.customer_name_layout = QGridLayout()
        self.customer_name_layout.addWidget(self.customer_first_name_label,0,0)
        self.customer_name_layout.addWidget(self.customer_first_name_edit,0,1)
        self.customer_name_layout.addWidget(self.customer_last_name_label,1,0)
        self.customer_name_layout.addWidget(self.customer_last_name_edit,1,1)

        self.customer_postcode_layout = QGridLayout()
        self.customer_postcode_layout.addWidget(self.customer_house_number_label,0,0)
        self.customer_postcode_layout.addWidget(self.customer_house_number_edit,0,1)
        self.customer_postcode_layout.addWidget(self.customer_postcode_label,1,0)
        self.customer_postcode_layout.addWidget(self.customer_postcode_edit,1,1)

        self.grid_layout = QGridLayout()
        self.grid_layout.addWidget(self.number_radio,0,0)
        self.grid_layout.addWidget(self.name_radio,1,0)
        self.grid_layout.addWidget(self.postcode_radio,2,0)
        self.grid_layout.addLayout(self.customer_number_layout,0,1)
        self.grid_layout.addLayout(self.customer_name_layout,1,1)
        self.grid_layout.addLayout(self.customer_postcode_layout,2,1)
        self.grid_layout.addWidget(self.find_customer_button,3,1)

        self.radio_button_box.setLayout(self.grid_layout)

        self.final_layout = QVBoxLayout()
        self.final_layout.addWidget(self.radio_button_box)

        self.find_customer_widget = QWidget()
        self.find_customer_widget.setLayout(self.final_layout)
        self.stacked_layout.addWidget(self.find_customer_widget)


    def select_customer_layout(self):
        self.customer_table = QTableView()
        self.customer_table.setSelectionBehavior(1)
        self.customer_table.setModel(self.model)

        self.customer_table_layout = QVBoxLayout()
        self.customer_table_layout.addWidget(self.customer_table)

        self.create_order_button = QPushButton("Create New Order")
        self.customer_table_layout.addWidget(self.create_order_button)

        self.select_customer_widget = QWidget()
        self.select_customer_widget.setLayout(self.customer_table_layout)
        self.stacked_layout.addWidget(self.select_customer_widget)

        #connections
        self.create_order_button.clicked.connect(self.selected_customer_details)


    def change_search(self):
        if self.radio_button_group.checkedId() == 0:
            self.customer_number_edit.setEnabled(True)
            self.customer_first_name_edit.setEnabled(False)
            self.customer_last_name_edit.setEnabled(False)
            self.customer_house_number_edit.setEnabled(False)
            self.customer_postcode_edit.setEnabled(False)
        elif self.radio_button_group.checkedId() == 1:
            self.customer_number_edit.setEnabled(False)
            self.customer_first_name_edit.setEnabled(True)
            self.customer_last_name_edit.setEnabled(True)
            self.customer_house_number_edit.setEnabled(False)
            self.customer_postcode_edit.setEnabled(False)
        elif self.radio_button_group.checkedId() == 2:
            self.customer_number_edit.setEnabled(False)
            self.customer_first_name_edit.setEnabled(False)
            self.customer_last_name_edit.setEnabled(False)
            self.customer_house_number_edit.setEnabled(True)
            self.customer_postcode_edit.setEnabled(True)

    def find_customer(self):
        if self.radio_button_group.checkedId() == 0:
            self.search_values = (self.customer_number_edit.text(),)
            self.model = self.connection.find_existing_customers_by_number(self.search_values)
        elif self.radio_button_group.checkedId() == 1:
            self.search_values = (self.customer_first_name_edit.text(),self.customer_last_name_edit.text())
            self.model = self.connection.find_existing_customers_by_name(self.search_values)
        elif self.radio_button_group.checkedId() == 2:
            self.search_values = (self.customer_house_number_edit.text(),self.customer_postcode_edit.text())
            self.model = self.connection.find_existing_customers_by_postcode(self.search_values)
        self.select_customer_layout()
        self.stacked_layout.setCurrentIndex(1)

    def selected_customer_details(self):
        indexes = self.customer_table.selectedIndexes()
        self.customer_id = self.customer_table.model().data(indexes[0])
        self.customer_table.setDisabled(True)
        self.create_order_button.setDisabled(True)
        self.date, self.time = self.connection.create_new_order_for_customer(self.customer_id)
        self.createdNewOrder.emit()

    def most_recent_created_order_details(self):
        return {'customer':self.customer_id,'date':self.date,'time':self.time}

```

create_order.py
---------------
```
# -*- coding:utf-8 -*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class OrderWidget(QWidget):
    """provides a widget that enables you to create an order full of products"""
    def __init__(self,connection, **kwargs):
        super(OrderWidget,self).__init__(**kwargs)
        self.connection = connection
        self.product_model = self.connection.current_products()
        self.order_details = None


        self.product_table = QTableView()
        self.product_table.setModel(self.product_model)
        self.product_table.setSelectionBehavior(1)

        self.order_item_table = QTableView()

        self.add_product_button = QPushButton("Add Product")
        self.remove_product_button = QPushButton("Remove Product")

        self.order_button_layout = QVBoxLayout()
        self.order_button_layout.addWidget(self.add_product_button)
        self.order_button_layout.addWidget(self.remove_product_button)

        self.layout = QHBoxLayout()
        self.layout.addWidget(self.order_item_table)
        self.layout.addLayout(self.order_button_layout)
        self.layout.addWidget(self.product_table)

        self.total_layout = QVBoxLayout()

        self.total_label = QLabel()

        self.total_layout.addLayout(self.layout)
        self.total_layout.addWidget(self.total_label)

        self.setLayout(self.total_layout)

        self.disable_selection()

        #connections
        self.add_product_button.clicked.connect(self.add_product)
        self.remove_product_button.clicked.connect(self.remove_product)

    def add_product(self):
        selected_indexes = self.product_table.selectedIndexes()
        product_index = self.product_table.model().data(selected_indexes[0]) #get product id
        self.connection.add_product_to_order_with_details(self.order_details,product_index)
        self.order_item_table.model().select()
        self.calculate_total()

    def remove_product(self):
        pass

    def disable_selection(self):
        self.product_table.setDisabled(True)
        self.add_product_button.setDisabled(True)
        self.remove_product_button.setDisabled(True)

    def enable_selection(self):
        self.product_table.setEnabled(True)
        self.add_product_button.setEnabled(True)
        self.remove_product_button.setEnabled(True)

        self.order_model = self.connection.current_order_items(self.order_details)
        self.order_item_table.setModel(self.order_model)
        self.order_item_table.hideColumn(0)
        self.order_item_table.hideColumn(1)
        self.order_model.dataChanged.connect(self.calculate_total)

    def calculate_total(self):
        total = self.connection.current_order_total(self.order_details)
        self.total_label.setText("Total Cost: £{0:.2f}".format(total))


```
sqldb.py
--------
```
    def current_products(self):
        model = QSqlRelationalTableModel()
        print(self.db.tables())
        model.setTable(self.db.tables()[2])
        model.setRelation(3,QSqlRelation("ProductType","ProductTypeID","Description"))
        model.select()
        return model

```

main8.py
````````
```
from sqlconnection import *
```
sqlconnection.py
----------------
```
    def find_existing_customers_by_number(self,values):
        model = QSqlQueryModel()
        query = QSqlQuery()
        query.prepare("""SELECT * FROM customer WHERE CustomerID = ?""")
        query.addBindValue(values[0])
        query.exec_()
        model.setQuery(query)
        return model

import datetime

    def create_new_order_for_customer(self,customer_id):
        query = QSqlQuery()
        query.prepare("""INSERT INTO CustomerOrder(Date,Time,CustomerID) values (?,?,?)""")
        today = datetime.datetime.today()
        date = today.strftime("%Y-%m-%d")
        time = today.strftime("%H:%M:%S")
        query.addBindValue(date)
        query.addBindValue(time)
        query.addBindValue(customer_id)
        query.exec_()
        return date, time

    def current_order_number(self,order_details):
        query = QSqlQuery()
        query.prepare("""SELECT * FROM CustomerOrder WHERE CustomerID = ? AND Date = ? AND Time = ?""")
        query.addBindValue(order_details['customer'])
        query.addBindValue(order_details['date'])
        query.addBindValue(order_details['time'])
        query.exec_()
        query.first()
        order = query.record()
        order_id = order.value("OrderID")
        return order_id

    def add_product_to_order_with_details(self,order_details,product_id):
        order_id = self.current_order_number(order_details)
        query = QSqlQuery()
        query.prepare("""INSERT INTO OrderItem(OrderID,ProductID,Quantity) values(?,?,1)""")
        query.addBindValue(order_id)
        query.addBindValue(product_id)
        query.exec_()

    def current_order_items(self,order_details):
        order_id = self.current_order_number(order_details)
        model = QSqlRelationalTableModel()
        model.setEditStrategy(QSqlTableModel.OnFieldChange)
        model.setTable("OrderItem")
        model.setFilter("OrderID = {0}".format(order_id))
        model.setRelation(2,QSqlRelation("Product","ProductID","Name"))
        model.select()
        return model

    def current_order_total(self,order_details):
        order_id = self.current_order_number(order_details)
        query = QSqlQuery()
        query.prepare("""SELECT SUM(Product.Price * OrderItem.Quantity) AS Total
                         FROM Product, OrderItem
                         WHERE OrderItem.OrderID = ?
                         AND OrderItem.ProductID = Product.ProductID""")
        query.addBindValue(order_id)
        query.exec_()
        query.first()
        total = query.value(0)
        return total
```

sqlconnection.py
----------------

```
# -*- coding:utf-8 -*-
import datetime
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

    def find_existing_customers_by_number(self,values):
        model = QSqlQueryModel()
        query = QSqlQuery()
        query.prepare("""SELECT * FROM customer WHERE CustomerID = ?""")
        query.addBindValue(values[0])
        query.exec_()
        model.setQuery(query)
        return model

    def find_existing_customers_by_name(self,values):
        model = QSqlQueryModel()
        query = QSqlQuery()
        query.prepare("""SELECT * FROM customer WHERE FirstName = ? and LastName = ?""")
        query.addBindValue(values[0])
        query.addBindValue(values[1])
        query.exec_()
        model.setQuery(query)
        return model

    def find_existing_customers_by_postcode(self,values):
        model = QSqlQueryModel()
        query = QSqlQuery()
        query.prepare("""SELECT * FROM customer WHERE PostCode = ?""")
        query.addBindValue(values[1])
        query.exec_()
        model.setQuery(query)
        return model

    def current_products(self):
        model = QSqlRelationalTableModel()
        print(self.db.tables())
        model.setTable(self.db.tables()[2])
        model.setRelation(3,QSqlRelation("ProductType","ProductTypeID","Description"))
        model.select()
        return model

    def create_new_order_for_customer(self,customer_id):
        query = QSqlQuery()
        query.prepare("""INSERT INTO CustomerOrder(Date,Time,CustomerID) values (?,?,?)""")
        today = datetime.datetime.today()
        date = today.strftime("%Y-%m-%d")
        time = today.strftime("%H:%M:%S")
        query.addBindValue(date)
        query.addBindValue(time)
        query.addBindValue(customer_id)
        query.exec_()
        return date, time

    def current_order_number(self,order_details):
        query = QSqlQuery()
        query.prepare("""SELECT * FROM CustomerOrder WHERE CustomerID = ? AND Date = ? AND Time = ?""")
        query.addBindValue(order_details['customer'])
        query.addBindValue(order_details['date'])
        query.addBindValue(order_details['time'])
        query.exec_()
        query.first()
        order = query.record()
        order_id = order.value("OrderID")
        return order_id

    def add_product_to_order_with_details(self,order_details,product_id):
        order_id = self.current_order_number(order_details)
        query = QSqlQuery()
        query.prepare("""INSERT INTO OrderItem(OrderID,ProductID,Quantity) values(?,?,1)""")
        query.addBindValue(order_id)
        query.addBindValue(product_id)
        query.exec_()

    def current_order_items(self,order_details):
        order_id = self.current_order_number(order_details)
        model = QSqlRelationalTableModel()
        model.setEditStrategy(QSqlTableModel.OnFieldChange)
        model.setTable("OrderItem")
        model.setFilter("OrderID = {0}".format(order_id))
        model.setRelation(2,QSqlRelation("Product","ProductID","Name"))
        model.select()
        return model

    def current_order_total(self,order_details):
        order_id = self.current_order_number(order_details)
        query = QSqlQuery()
        query.prepare("""SELECT SUM(Product.Price * OrderItem.Quantity) AS Total
                         FROM Product, OrderItem
                         WHERE OrderItem.OrderID = ?
                         AND OrderItem.ProductID = Product.ProductID""")
        query.addBindValue(order_id)
        query.exec_()
        query.first()
        total = query.value(0).toFloat()
        return total[0]


```
