# 21v-pyqt

Настройку соединения следует проводить сразу после открытия и до его использования.

PRAGMA encoding
----------------
```
PRAGMA encoding = "UTF-8";  // тип данных БД, всегда используйте UTF-8
```

добавление к схеме базы данных внешнего ключа SQL, который бы принудительно обеспечивал сохранение связей между таблицами «artist» и «track». Чтобы это сделать, нужно модифицировать декларацию таблицы «track» добавив к нему определение внешнего ключа следующим образом:
```
CREATE TABLE track(
  trackid     INTEGER, 
  trackname   TEXT, 
  trackartist INTEGER,
  FOREIGN KEY(trackartist) REFERENCES artist(artistid)
);
```
Таким образом устанавливается ограничение для SQLite. Теперь попытки вставить строку в таблицу «track», для которой нет соответствующей строки в таблице «artist», будут неуспешны, равно как и удаление строки из таблицы «artist», имеющей зависимые строки в таблице «track».

Но есть одно исключение: если столбец внешнего ключа в таблице «track» имеет значение NULL, то существования соответствующей ему строки в таблице «artist» не требуется. В выражениях SQL это означает, что для каждой строки в таблице «track» следующие выражение должно быть истинным:

trackartist IS NULL OR EXISTS(SELECT 1 FROM artist WHERE artistid=trackartist)
Совет: если приложение требует строгого соответствия между «artist» и «track», то значения NULL следует запретить в столбце «trackartist». Это можно сделать просто добавив в схему соответствующее ограничение NOT NULL.

Включение поддержки внешних ключей
==================================

При условии, что библиотека скомпилирована с поддержкой ограничений внешнего ключа, приложение получает возможность включать их в реальном режиме времени с помощью команды «PRAGMA foreign_keys». Например, так:
```
sqlite> PRAGMA foreign_keys = ON;
```
Внешние ключи по умолчанию отключены (для обратной совместимости). Поэтому их необходимо специально включать при каждом отдельном соединении с базой данных. 

В приложении можно также использовать оператор «PRAGMA foreign_keys» чтобы определить включены ли в данный момент внешние ключи. Это демонстрирует следующий сеанс работы в командной строке:
```
sqlite> PRAGMA foreign_keys;
0
sqlite> PRAGMA foreign_keys = ON;
sqlite> PRAGMA foreign_keys;
1

```

PRAGMA foreign_keys
-------------------
```
PRAGMA foreign_keys = 1; // включить поддержку foreign keys, по умолчанию - ОТКЛЮЧЕНА
```
foreign key
===========
```
    sql = """create table ProductType (
             ProductTypeID integer,
             Description text,
             primary key (ProductTypeID))"""

    sql = """create table Product (
             ProductID integer,
             Name text,
             Price decimal,
             ProductTypeID integer,
             primary key (ProductID),
             foreign key (ProductTypeID) references ProductType(ProductTypeID)
             ON UPDATE CASCADE ON DELETE Restrict)"""

```

01/1.py
--------
```
import sqlite3
import decimal
D=decimal.Decimal

def adapt_decimal(d):
    return str(d)

def convert_decimal(s):
    return D(s)

# Register the adapter
sqlite3.register_adapter(D, adapt_decimal)

# Register the converter
sqlite3.register_converter("decimal", convert_decimal)

db = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_DECLTYPES)
cur = db.cursor()

sql = """create table ProductType (
             ProductTypeID integer,
             Description text,
             primary key (ProductTypeID))"""

cur.execute(sql)

sql = """create table Product (
             ProductID integer,
             Name text,
             Price decimal,
             ProductTypeID integer,
             primary key (ProductID),
             foreign key (ProductTypeID) references ProductType(ProductTypeID)
             ON UPDATE CASCADE ON DELETE Restrict)"""

cur.execute(sql)

cur.execute("insert into ProductType values (?, ?)", (0, 'test description'))
cur.execute("insert into ProductType values (?, ?)", (1, 'test1 description'))
cur.execute("insert into ProductType values (?, ?)", (2, 'test2 description'))

cur.execute("insert into Product values (?, ?, ?, ?)", (0, 'test', D('4.12'), 0))

cur.execute("insert into Product values (?, ?, ?, ?)", (1, 'test1', D('5.12'), 1))

cur.execute("insert into Product values (?, ?, ?, ?)", (2, 'test2', D('5.7'), 2))

cur.execute("select * from Product")

data=cur.fetchall()
print data

cur.close()
db.close()
```

## ВСТАВКА ПУСТЫХ УКАЗАТЕЛЕЙ (NULL)

Так как значение NULL - это специальный маркер, а не просто символьное значение, он не включается в одиночные кавычки.

## ИМЕНОВАНИЕ СТОЛБЦА ДЛЯ ВСТАВКИ (INSERT)

Вы можете также указывать столбцы, куда вы хотите вставить значение имени. Это позволяет вам вставлять имена в любом порядке. 

По умолчанию может быть введено или значение NULL или другое значе- ние определяемое как - по умолчанию. Если ограничение запрещает использование значения NULL в данном столбце, и этот столбец не установлен как по умолчанию, этот столбец должен быть обеспечен значением для любой команды INSERT которая относится к таблице.

# None in Python maps to NULL in sqlite3
01/2.py
-------
```
import sqlite3
import decimal
D=decimal.Decimal

def adapt_decimal(d):
    return str(d)

def convert_decimal(s):
    return D(s)

# Register the adapter
sqlite3.register_adapter(D, adapt_decimal)

# Register the converter
sqlite3.register_converter("decimal", convert_decimal)

db = sqlite3.connect("test.db", detect_types=sqlite3.PARSE_DECLTYPES)
cur = db.cursor()

# None in Python maps to NULL in sqlite3

cur.execute("insert into ProductType values (?, ?)", (None,'test3 description'))
cur.execute("insert into ProductType values (?, ?)", (None,'test4 description'))
cur.execute("insert into ProductType values (?, ?)", (None,'test5 description'))

cur.execute("insert into Product values (?, ?, ?, ?)", (None,'test3', D('4.12'), 2))

cur.execute("insert into Product values (?, ?, ?, ?)", (None,'test4', D('5.12'), 3))

cur.execute("insert into Product values (?, ?, ?, ?)", (None,'test5', D('5.7'), 3))
db.commit()

cur.execute("select * from Product")

data=cur.fetchall()
print data

cur.close()
db.close()

```
AUTOINCREMENT
--------------
```
import sqlite3
import decimal
D=decimal.Decimal

def adapt_decimal(d):
    return str(d)

def convert_decimal(s):
    return D(s)

# Register the adapter
sqlite3.register_adapter(D, adapt_decimal)

# Register the converter
sqlite3.register_converter("decimal", convert_decimal)

db = sqlite3.connect("test1.db", detect_types=sqlite3.PARSE_DECLTYPES)
cur = db.cursor()
sql = """create table ProductType (
             ProductTypeID INTEGER PRIMARY KEY AUTOINCREMENT,
             Description text
             )"""

cur.execute(sql)

sql = """create table Product (
             ProductID INTEGER PRIMARY KEY AUTOINCREMENT,
             Name text,
             Price decimal,
             ProductTypeID INTEGER,
             foreign key (ProductTypeID) references ProductType(ProductTypeID)
             ON UPDATE CASCADE ON DELETE Restrict)"""

cur.execute(sql)

cur.execute("insert into ProductType (Description) values (?)", ('test description',))
cur.execute("insert into ProductType (Description) values (?)", ('test1 description',))
cur.execute("insert into ProductType (Description) values (?)", ('test2 description',))

cur.execute("insert into Product (Name,Price,ProductTypeID) values (?, ?, ?)", ('test', D('4.12'), 0))

cur.execute("insert into Product (Name,Price,ProductTypeID) values (?, ?, ?)", ('test1', D('5.12'), 1))

cur.execute("insert into Product (Name,Price,ProductTypeID) values (?, ?, ?)", ('test2', D('5.7'), 2))
db.commit()

cur.execute("select * from Product")

data=cur.fetchall()
print data

cur.close()
db.close()

```    

## SQL LEFT JOIN Syntax
```
SELECT column_name(s)
FROM table1
LEFT JOIN table2
ON table1.column_name=table2.column_name;

SELECT column_name(s)
FROM table1
LEFT OUTER JOIN table2
ON table1.column_name=table2.column_name;
```
Запрос вернет объединенные данные, которые пересекаются по условию, указанному в LEFT JOIN <..> ON. 
```
select * from Product w left join ProductType t on t.ProductTypeID = w.ProductTypeID;Prod  

Name           Pric  Prod  Prod  Description  
----  -------------  ----  ----  ----  -------------
0     test           4.12  0     0     test description
1     test1          5.12  1     1     test1 description
2     test2          5.7   2     2     test2 description

```

## INNER JOIN ON
```
SELECT p.ProductID, p.name, t.description AS t_description FROM Product p INNER JOIN ProductType t ON p.ProductTypeID = t.ProductTypeID
 ```
Запрос вернет объединенные данные, которые пересекаются по условию, указанному в INNER JOIN ON <..>. 

Внутреннее объединение INNER JOIN (синоним JOIN, ключевое слово INNER можно опустить). 

Выбираются только совпадающие данные из объединяемых таблиц. Чтобы получить данные, которые не подходят по условию, необходимо использовать 

- внешнее объединение - OUTER JOIN. 

Такое объединение вернет данные из обеих таблиц совпадающими по одному из условий.

Существует два типа внешнего объединения OUTER JOIN - LEFT OUTER JOIN и RIGHT OUTER JOIN. 

Работают они одинаково, разница заключается в том что LEFT - указывает что "внешней" таблицей будет находящаяся слева (в нашем примере это таблица ProductType). 
Ключевое слово OUTER можно опустить. Запись LEFT JOIN идентична LEFT OUTER JOIN.

```
SELECT p.ProductID, p.name, t.description AS t_description FROM Product p INNER JOIN ProductType t ON p.ProductTypeID = t.ProductTypeID;
Prod  Name           t_de
----  -------------  ----
2     test1          test description
3     test2          test1 description

```
### оператор IN
Вы можете использовать подзапросы которые производят любое число строк если вы используете специальный оператор IN ( операторы BETWEEN, LIKE, и IS NULL не могут использоваться с подзапросами ). IN определяет набор значений, одно из которых должно совпадать с другим термином уравнения предиката в порядке, чтобы предикат был верным. Когда вы используете IN с подзапросом, SQL просто формирует этот набор из вывода подзапроса.
```
SELECT * FROM Product WHERE Name NOT IN ('test1', 'test2');
Prod  Name           Pric  Prod
----  -------------  ----  ----
1     test           4.12  0  

select * from Product where NOT (Name IN ('test1', 'test2'));
Prod  Name           Pric  Prod
----  -------------  ----  ----
1     test           4.12  0   

```

## ALTER TABLE
SQLite версия команды ALTER TABLE позволяет пользователю переименовать или добавить новые поля в существующую таблицу. Нет возможности удалить поле из таблицы.

Синтаксис RENAME TO используется при переименовании таблицы из [database-name.]table-name в new-table-name. Эта команда не может применяться для переноса таблиц между базами данных, только переименование в пределах одной базы.
Если переименованная таблица имеет триггеры или индексы, то они остаются связанными с таблицей и после переименования. Однако, если имеются представления (view) или запросы выполняемые триггерами, ссылаются на переименованную таблицу, то они автоматически не изменяются. Если необходимо то триггеры и представления, должны быть удалены и повторно созданы вручную. 

### Синтаксис ADD [COLUMN]
Синтаксис ADD [COLUMN] используется для добавления нового поля в существующую таблицу. Новый столбец всегда добавляется в конец списка полей. Описание добавляемого столбца должен соответствовать формату, разрешенному в CREATE TABLE, со следующими ограничениями: 
- Столбец не может иметь ограничений PRIMARY KEY или UNIQUE.
- Столбец не может иметь значений по умолчанию CURRENT_TIME, CURRENT_DATE или CURRENT_TIMESTAMP.
- Если наложено ограничение NOT NULL, столбец должен иметь значение по умолчанию, отличное от NULL.
Время выполнения команды ALTER TABLE не зависит от количества данных в таблице. ALTER TABLE работает также быстро на таблице с 10 миллионами записей, как и на таблице с 1 записью. 
После выполнения ADD COLUMN, база данных не будет читаться SQLite версии 3.1.3 и ниже, до применения команды VACUUM.

Добавим к нашей таблице Product column updatedon. 

sqlite> alter table Product add column updatedon date;
```

sqlite> .schema Product
```
.schema Product
CREATE TABLE Product (
             ProductID INTEGER PRIMARY KEY AUTOINCREMENT,
             Name text,
             Price decimal,
             ProductTypeID INTEGER, updatedon date,
             foreign key (ProductTypeID) references ProductType(ProductTypeID)
             ON UPDATE CASCADE ON DELETE Restrict);

```

## CREATE TRIGGER Триггеры в SQLite 
Триггеры в SQLite – это функции, которые выполняются по какому-то событию. Например, вставка строки в базу, удаление строки, обновление поля. Причем триггеры могут срабатывать как до выполнения действий по некоторому событию, так и после. 

#### create trigger

Product_update_trg.sql
```
create trigger product_update_trg after update on Product
begin
  update Product set updatedon = datetime('NOW') where ProductID = new.ProductID;
end;
```
create trigger
---------------
```
sqlite3 test1.db   < Product_update_trg.sql
```
Тестируем триггер. 
------------------
```
.schema Product
CREATE TABLE Product (
             ProductID INTEGER PRIMARY KEY AUTOINCREMENT,
             Name text,
             Price decimal,
             ProductTypeID INTEGER, updatedon date,
             foreign key (ProductTypeID) references ProductType(ProductTypeID)
             ON UPDATE CASCADE ON DELETE Restrict);
CREATE TRIGGER product_update_trg after update on Product
begin
  update Product set updatedon = datetime('NOW') where ProductID = new.ProductID;
end;

```
Тестируем триггер. update Product
----------------------------------
```
sqlite> update Product set name='Tom Cat' where ProductID=2;

```

Тестируем триггер.  sqlite> select * from Product;
--------------------------------------------------
```
select * from Product;
1|test|4.12|0|
2|Tom Cat|5.12|1|2015-12-15 18:45:50
3|test2|5.7|2|

```

### UPDATE
```
UPDATE [ OR conflict-algorithm ] [database-name .] table-name
SET column1=expression1, column2=expression2, ... 
[WHERE expr]
assignment ::=
column-name = expr
```
Оператор UPDATE используется для изменения значения столбцов в выбранных записях таблицы. Каждое присваивание в UPDATE определяется именем колонки слева от знака равенства и вычисляемым выражением в правой. Выражение может использовать значения других полей. Все выражения вычисляются перед выполнением присваивания (например, в MySQL это не так) Оператор WHERE может использоваться для задания обновляемых записей.
Опциональный оператор конфликта, позволяет определить правила альтернативного алгоритма разрешения конфликтных ситуаций, которые будут применяться при выполнении команды, смотрите ON CONFLICT.

## Представление (VIEW)
Представление (VIEW) - объект данных который не содержит никаких данных его владельца. Это - тип таблицы, чье содержание выбирается из других таблиц с помощью выполнения запроса. Поскольку значения в этих таблицах меняются, то авто- матически, их значения могут быть показаны представлением. В этой главе, вы узнаете что такое представления, как они создаются, и не- много об их возможностях и ограничениях. Использование представлений основанных на улучшенных средствах запросов, таких как объединение и под- запрос, разработанных очень тщательно, в некоторых случаях даст больший выигрыш по сравнению с запросами.

### ЧТО ТАКОЕ ПРЕДСТАВЛЕНИЕ ?

Типы таблиц, с которыми вы имели дело до сих пор, назывались - базовыми таблицами. Это - таблицы, которые содержат данные. Однако имеется другой вид таблиц: - представления. Представления - это таблицы чье содержание выбирается или получается из других таблиц. Они работают в запросах и операторах DML точно также как и основные таблицы, но не содержат ника- ких собственных данных. Представления - подобны окнам, через которые вы просматриваете информа- цию( как она есть, или в другой форме, как вы потом увидите ), которая фактически хранится в базовой таблице. Представление - это фактически запрос, который выполняется всякий раз, когда представление становится темой ко- манды. Вывод запроса при этом в каждый момент становится содержанием представления.

### КОМАНДА CREATE VIEW

Вы создаете представление командой CREATE VIEW. Она состоит из слов CREATE VIEW (СОЗДАТЬ ПРЕДСТАВЛЕНИЕ), имени представления которое нужно создать, слова AS (КАК), и далее запроса, как в следующем примере:
  
```
create view protype as select ProductID, p.Name, Price, t.Description, p.updatedon from Product p, ProductType t where p.ProductTypeID = t.ProductTypeID;
```

Теперь Вы имеете представление, называемое protype. Вы можете использовать это представление точно так же как и любую другую таблицу. Она может быть запрошена, модифицирована, вставлена в, удалена из, и соединена с, другими таблицами и представлениями. 

```
select * from protype;

2|Tom Cat|5.12|test description|2015-12-15 18:45:50
3|test2|5.7|test1 description|

```
## ПРЕДСТАВЛЕНИЯ И ОБЪЕДИНЕНИЯ

Представления не требуют чтобы их вывод осуществлялся из одной базовой таблицы. Так как почти любой допустимый запрос SQL может быть использован в представлении, он может выводить информацию из любого числа базовых таблиц, или из других представлений. 


start of a library module for talking with databases
----------------------------------------------------
database_functions.py:

```
import sqlite3
import decimal
D=decimal.Decimal

def adapt_decimal(d):
    return str(d)

def convert_decimal(s):
    return D(s)

# Register the adapter
sqlite3.register_adapter(D, adapt_decimal)

# Register the converter
sqlite3.register_converter("decimal", convert_decimal)
DATABASE = "myshop.db"

def query(sql,data):
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        cursor.execute(sql,data)
        db.commit()
```

Работа с датами и временем в Sqlite
------------------------------------

SQLite не поддерживает дату в нормальном виде!
----------------------------------------------
дату предлагают хранить в 3-х форматах:

- Текст (TEXT) в формате ISO8601 который записывается вот так: ("YYYY-MM-DD HH:MM:SS.SSS")
- Дробное (REAL) как количество дней юлианского календаря с полудня 24 ноября 4714 до Н.Э. по Гринвичу
- Целое (INTEGER) в формате Unix Time, который представляет из себя количество секунд с  1970-01-01 00:00:00 UTC

Строки занимают огромное количество места, что черевато на маломощных устройствах. Плюс к тому обработка строк происходит довольно медленно по тем же причинам. 

Целые числа занимают мало места, быстро обрабатываются

init.py:
---------
```
import sqlite3
import decimal
D=decimal.Decimal

def adapt_decimal(d):
    return str(d)

def convert_decimal(s):
    return D(s)

# Register the adapter
sqlite3.register_adapter(D, adapt_decimal)

# Register the converter
sqlite3.register_converter("decimal", convert_decimal)


def create_customer(db,cursor):
    sql = """create table Customer (
             CustomerID INTEGER PRIMARY KEY AUTOINCREMENT,
             FirstName varchar(50),
             LastName  varchar(50),
             Street text,
             Town varchar(20),
             PostCode varchar(10),
             TelephoneNumber varchar(20)
             )"""

    cursor.execute(sql)
    db.commit()

def create_product_type(db,cursor):
    sql = """create table ProductType (
             ProductTypeID INTEGER PRIMARY KEY AUTOINCREMENT,
             Description text
             )"""
    
    cursor.execute(sql)
    db.commit()

def create_product(db,cursor):
    sql = """create table Product (
             ProductID INTEGER PRIMARY KEY AUTOINCREMENT,
             Name varchar(50),
             Price decimal,
             ProductTypeID integer,
             foreign key (ProductTypeID) references ProductType(ProductTypeID)
             ON UPDATE CASCADE ON DELETE Restrict)"""
    
    cursor.execute(sql)
    db.commit()

def create_customer_order(db,cursor):
    sql = """create table CustomerOrder (
             OrderID INTEGER PRIMARY KEY AUTOINCREMENT,
             Date date,
             Time date,
             CustomerID integer,
             foreign key (CustomerID) references Customer(CustomerID)
             ON UPDATE CASCADE ON DELETE Restrict)"""
    
    cursor.execute(sql)
    db.commit()

def create_order_items(db,cursor):
    sql = """create table OrderItem (
             OrderItemID INTEGER PRIMARY KEY AUTOINCREMENT,
             OrderID integer,
             ProductID integer,
             foreign key (OrderID) references CustomerOrder(OrderID)
             ON UPDATE CASCADE ON DELETE Restrict,
             foreign key (ProductID) references Product(ProductID)
             ON UPDATE CASCADE ON DELETE Restrict)"""
    
    cursor.execute(sql)
    db.commit()


if __name__ == "__main__":

    db = sqlite3.connect("myshop.db")
    cursor = db.cursor()
    create_customer(db,cursor)
    create_product_type(db,cursor)
    create_product(db,cursor)
    create_customer_order(db,cursor)
    create_order_items(db,cursor)

```
seed.py:
--------
```
#inserting data into tables with reference to other tables

from database_functions import query, D

def insert_product_data(records):
    sql = "insert into Product (Name,Price,ProductTypeID) values (?,?,?)"
    for record in records:
        query(sql, record)

def insert_product_type_data(records):
    sql = "insert into ProductType(Description) values (?)"
    for record in records:
        query(sql, record)

if __name__ == "__main__":
    product_types = [("Hot Chocolate",),('Cats',),('Dogs',),('Bids',),('Beers',),('Bears',)]
    insert_product_type_data(product_types)
    products = [("Signature",D('4.0'),4),("Delight",D('3.5'),4)]
    insert_product_data(products)
    
```
main.py:
--------
```

#product menu

import sqlite3


def query(sql,data):
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        cursor.execute(sql,data)
        db.commit()

def query_with_results(sql,data):
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        if data == None:
            cursor.execute(sql)
        else:
            cursor.execute(sql,data)
        results = cursor.fetchall()
        return results

def query_with_single_result(sql,data):
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        cursor.execute(sql,data)
        result = cursor.fetchone()
        return result

def delete_product(data):
    sql = "delete from Product where Name=?"
    query(sql,data)

def insert_data(values):
    sql = "insert into Product (Name,Price) values(?,?)"
    query(sql,values)

def update_product(data):
    sql = "update Product set Name=?, Price=? where ProductID=?"
    query(sql,data)

def select_all_products():
    sql = "select * from Product"
    return query_with_results(sql,None)

def select_product(id):
    sql = "select * from Product where ProductID=?"
    return query_with_single_result(sql,(id,))

def select_product_with_name(name):
    sql = "select * from Product where Name=?"
    return query_with_single_result(sql,(name,))

def display_menu():
    print("Product Table Menu")
    print()
    print("1. Help")
    print("2. Add new product")
    print("3. Edit existing product")
    print("4. Delete existing product")
    print("5. Search for products")
    print("0. Exit")
    print()

def get_menu_choice():
    accepted = False
    while not accepted:
        choice = int(input("Please select an option: "))
        if 0 <= choice <= 5:
            accepted = True
        else:
            print("Pleae enter a valid value")
    return choice

def display_select_results(results):
    if results[0] != None:
        print()
        print("{0:<15} {1:<15} {2:<15}".format("Product ID","Product Name", "Product Price"))
        for result in results:
            print("{0:<15} {1:<15} {2:<15}".format(result[0],result[1],result[2]))
        print()
    else:
        print("The query returned no results")


def main():
    finished = False
    while not finished:
        display_menu()
        choice = get_menu_choice()
        if choice == 1:
            sql = """create table Product
            (ProductID integer,
            Name text,
            Price real,
            primary key(ProductID))"""
            create_table("Product",sql)
        elif choice == 2:
            name = input("Please enter name of new product: ")
            price = float(input("Please enter the price of {0}: ".format(name)))
            insert_data((name,price))
        elif choice == 3:
            products = select_all_products()
            display_select_results(products)
            product_id = int(input("Please enter the id of the product to edit: "))
            name = input("Please enter new name for the product: ")
            price = float(input("Please enter the price of {0}: ".format(name)))
            update_product((name,price,product_id))
        elif choice == 4:
            products = select_all_products()
            display_select_results(products)
            product_id = int(input("Please enter the id of the product to delete: "))
            product = select_product(product_id)
            delete_product((product[1],))
        elif choice == 5:
            name = input("Please enter the name of the product to search for: ")
            product = select_product_with_name(name)
            display_select_results([product])
        elif choice == 0:
            finished = True


if __name__ == "__main__":
    DATABASE = "myshop.db"
    main()



```


controller_class.py
-------------------
```
import sqlite3

class ShopController:

    def __init__(self):
        self.dbtext = "myshop.db"
        
    def query(self,sql,data):
        with sqlite3.connect(self.dbtext) as db:
            cursor = db.cursor()
            cursor.execute("PRAGMA foreign_keys = ON")
            cursor.execute(sql,data)
            db.commit()

    def select_query(self,sql,data=None):
        with sqlite3.connect(self.dbtext) as db:
            cursor = db.cursor()
            cursor.execute("PRAGMA foreign_keys = ON")
            if data:
                cursor.execute(sql,data)
            else:
                cursor.execute(sql)
            results = cursor.fetchall()
        return results


```
customer_controller.py:
-----------------------
```
from controller_class import *

class CustomerController(ShopController):

    """creates a controller to add/delete/amend customer records in the
       myshop database"""

    def __init__(self):
        super().__init__()

    def add_customer(self,fn,ln,sa,t,pc,tn):
        sql = """insert into Customer
                 (FirstName,LastName,Street,Town,PostCode,TelephoneNumber)
                 values
                 (?,?,?,?,?,?)"""
        self.query(sql,(fn,ln,sa,t,pc,tn))
        
    def delete_customer(self,customer_id):
        sql = """delete from Customer
                 where CustomerID = ?"""
        self.query(sql,(customer_id,))
        
    def customer_details(self,customer_id=None,first_name=None,last_name=None):
        sql = None
        if customer_id != None:
            sql = "select * from Customer where CustomerID = ?"
            data = (customer_id,)
        elif first_name != None and last_name != None:
            sql = "select * from Customer where FirstName = ? and LastName = ?"
            data = (first_name,last_name)
        elif first_name != None:
            sql = "select * from Customer where FirstName = ?"
            data = (first_name,)
        elif last_name != None:
            sql = "select * from Customer where LastName = ?"
            data = (last_name,)
        if sql != None:
            return self.select_query(sql,data)
        else:
            return None
        
    def amend_customer(self,customer_id,first_name=None,last_name=None,street_address=None,town=None,post_code=None,telephone_number=None):
        updates = []
        data = []
        if first_name != None:
            updates.append(("FirstName",first_name))
        if last_name != None:
            updates.append(("LastName",last_name))
        if street_address != None:
            updates.append(("Street",street_address))
        if town != None:
            updates.append(("Town",town))
        if post_code != None:
            updates.append(("PostCode",post_code))
        if telephone_number != None:
            updates.append(("TelephoneNumber",telephone_number))
        
        sql = "update Customer set "
        for item in updates:
            sql += "{0}=?, ".format(item[0])
            data.append(item[1])
        
        #remove last ', '
        sql = sql[:-2]
        sql += " where CustomerID=?"
        data.append(customer_id)
        self.query(sql,data)

    def customer_headings(self):
        sql = "PRAGMA table_info(Customer)"
        return self.select_query(sql)

```

OrderController
---------------
```
from controller_class import *
import datetime

class OrderController(ShopController):
    """creates a controller to add/delete/amend product orders in the
       myshop database"""

    def __init__(self):
        super().__init__()

    def new_empty_order(self,customer_id):
        sql = "insert into CustomerOrder (Date,Time,CustomerID) values (?,?,?)"
        date = datetime.datetime.now()
        time = datetime.datetime.now()
        self.query(sql,(date,time, customer_id))
        sql = "select OrderID from CustomerOrder where CustomerID = ? and Date = ?"
        return self.select_query(sql,(customer_id,date))

    def add_order_items(self,order_id,items):
        sql = "insert into OrderItem (OrderID,ProductID) values (?,?)"
        for item in items:
            self.query(sql,(order_id,item))

    def new_order_with_items(self,customer_id,items):
        order_id = self.new_empty_order(customer_id)
        self.add_order_items(order_id, items)

    def delete_order(self,customer_id,date):
        sql = "delete from CustomerOrder where CustomerID = ? and Date = ?"
        self.query(sql,(customer_id,date))

    def delete_order_items(self,order_id,items):
        sql = "delete from OrderItem where OrderID = ? and ProductID = ?"
        for item in items:
            self.query(sql,(order_id,item))

    def order_details(self,customer_id,date):
        sql = """select CustomerOrder.Date, CustomerOrder.OrderID, product.ProductID
                 from CustomerOrder, OrderItem, Product
                 where CustomerOrder.CustomerID = ? 
                 and CustomerOrder.Date = ? 
                 and OrderItem.OrderID = CustomerOrder.OrderID 
                 and Product.ProductID = OrderItem.ProductID"""
        return self.select_query(sql,(customer_id,date))

    def customer_orders(self,customer_id):
        sql = "select * from CustomerOrder where CustomerID=?"
        return self.select_query(sql,(customer_id,))

    def orders_on_date(self,date):
        sql = "select * from CustomerOrder where Date like ?%"
        return self.select_query(sql,(date,))


```

product_controller.py:
----------------------
```
from controller_class import *

class ProductController(ShopController):
    """creates a controller to add/delete/amend product records in the
       myshop database"""

    def __init__(self):
        super().__init__()

    def add_product(self,name,price,product_type):
        sql = """insert into Product (Name, ProductTypeID, Price)
                 values (?,?,?)"""
        self.query(sql,(name,product_type,price))

    def delete_product(self,product_id):
        sql = "delete from Product where ProductID = ?"
        self.query(sql,(product_id,))

    def product_details(self,product_id=None,name=None):
        sql = None
        data = []
        if product_id != None:
            sql = "select * from Product where ProductID = ?"
            data = (product_id,)
        elif name != None:
            sql = "select * from Product where Name = ?"
            data = (name,)
        else:
            sql = "select * from Product"
        return self.select_query(sql,data)

    def amend_product(self,product_id,name=None,product_type_id=None,price=None):
        updates = {}
        data = []
        if name != None:
            updates["Name"] = name
        if product_type_id != None:
            updates["ProductTypeID"] = product_type_id
        if price != None:
            updates["Price"] = price

        sql = "update Product set "
        for key, value in updates.items():
            sql += "{0}=?, ".format(key)
            data.append(value)

        sql = sql[:-2]
        sql += " where ProductID = ?"
        data.append(product_id)

        self.query(sql,data)

    def product_headings(self):
        sql = "PRAGMA table_info(Product)"
        return self.select_query(sql)

    def add_product_type(self,name):
        sql = "insert into ProductType (Description) values (?)"
        self.query(sql,(name,))

    def delete_product_type(self,product_type_id):
        sql = "delete from ProductType where ProductTypeID = ?"
        self.query(sql,(product_type_id,))

    def amend_product_type(self,product_type_id,name):
        sql = "update ProductType set Name = ? where ProductTypeID = ?"
        self.query(sql,(name,product_type_id))

    def product_type_details(self,product_type_id=None,name=None):
        if product_type_id != None:
            sql = "select * from ProductType where ProductTypeID = ?"
            data = (product_type_id,)
        elif name != None:
            sql = "select * from ProductType where Name = ?"
            data = (name,)
        return self.select_query(sql,data)

    def product_type_headings(self):
        sql = "PRAGMA table_info(ProductType)"
        return self.select_query(sql)
```
test.py
```
from customer_controller import *
from product_controller import *
from order_controller import *

test = CustomerController()

test.add_customer("Adam","McNicol","1 Python Street","Cambridge","CB3 2YU","01223 467893")
test.amend_customer("16",first_name="Bob")
print(test.customer_headings())

test = OrderController()
print(test.new_empty_order("1"))

```