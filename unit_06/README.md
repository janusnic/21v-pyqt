# 21v-pyqt

SQLite http://sqlite.org/
=========================
Страница скачивания: http://sqlite.org/download.html
-----------------------------------------------------
SQLite это библиотека написанная на языке C, которая предоставляет легковесную, находящуюся на диске базу данных, которой не требуется отдельный серверный процесс и которая позволяет получать доступ используя нестандартные диалекты языка SQL. Некоторые приложения могут использовать SQLite для внутреннего хранения данных. Также возможно сделать прототип приложения используя SQLite и затем перенести код для больших баз данных, таких как PostgreSQL или Oracle.

sqlite3 была написана Gerhard Häring и предоставляет SQL интерфейс совместимый с DB-API 2.0 спецификациями описанными в PEP 249.

Насколько SQLite популярна?
---------------------------
она везде. Как минимум, на любом смартфоне.

SQLite является открытым и полностью свободным программным обеспечением, распространяющимся как общественное достояние (public domain). Лицензия не накладывает никаких ограничений на то, как будет использоваться код, в том числе она позволяет взять его как часть закрытого проекта. Поэтому, SQLite может использоваться где угодно. В частности, SQLite используется в iPhone и iTunes, в Symbian и Android, встроен в Python и PHP, и предполагается, что он используется в клиенте Skype. С учётом того, куда встроена SQLite, вероятно, это сегодня наиболее распространённая в мире СУБД.

sqlite3
========
Доступна консольная утилита для работы с базами (sqlite3.exe, «a command-line shell for accessing and modifying SQLite databases»).

SQLite — встраиваемая в процесс реализация SQL-машины. Слово SQL-сервер здесь не используем, потому что как таковой сервер там не нужен — весь функционал, который встраивается в SQL-сервер, реализован внутри библиотеки (и, соответственно, внутри программы, которая её использует).

Особенности реализации
-----------------------
База данных в SQLite представлена в виде отдельного файла. Блокировка на запись реализована очень просто -- файл блокируется целиком. Не поддерживается запись в виды (views). Только частично поддерживаются триггеры.

Как известно, в своем развитии SQL устремился в разные стороны. Крупные производители начали впихивать всякие расширения. И хотя принимаются всякие стандарты (SQL 92), в реальной жизни все крупные БД не поддерживают стандартов полностью + имеют что-то свое. Так вот, SQLite старается жить по принципу «минимальный, но полный набор». Она не поддерживает сложные штуки, но во многом соответствует SQL 92.
И вводит некие свои особенности, которые очень удобны, но — не стандартны.

Что конкретно в поддержке SQL может вызвать недоумение?
--------------------------------------------------------
- Нельзя удалить или изменить столбец в таблице (ALTER TABLE DROP COLUMN…, ALTER TABLE ALTER COLUMN… ).
- Есть триггеры, но не настолько мощные как у крупных RDBMS.
- Есть поддержка foreign key, но по умолчанию — она ОТКЛЮЧЕНА.
- Нет встроенной поддержки UNICODE (но ее, вообщем, нетрудно добиться).
- Нет хранимых процедур.

a) каждая запись содержит виртуальный столбец rowid, который равен 64-битному номеру (уникальному для таблицы).
Можно объявить свой столбец INTEGER PRIMARY KEY и тогда этот столбец станет rowid (со своим именем, имя rowid все равно работает).
При вставке записи можно указать rowid, а можно — не указывать (и система тогда вставит уникальный). 

b) можно без труда организовать БД в памяти;

c) легко переносить: по умолчанию, БД — это один файл (в кроссплатформенном формате); 

d) тип столбца не определяет тип хранимого значения в этом поле записи, то есть в любой столбец можно занести любое значение;

e) много встроенных функций (которые можно использовать в SQL): www.sqlite.org/lang_corefunc.html;

Тип столбца определяет как сравнивать значения.
Но не обязывает заносить значения именно такого типа в столбец. Нечто вроде weak typing.

Допустим, мы объявили столбец как «A INTEGER».
SQlite позволяет занести в этот столбец значения любого типа (999, «abc», «123», 678.525).
Если вставляемое значение — не целое, то SQlite пытается привести его к целому. 
Т.е. строка «123» превратится в целое 123, а остальные значения запишутся «как есть».

можно вообще не задавать тип столбца
------------------------------------
Очень часто так и делается: CREATE TABLE foo (a,b,c,d).

Сервера нету, само приложение является сервером. 
------------------------------------------------
Доступ к БД происходит через «подключения» к БД (нечто вроде хэндла файла ОС), которые мы открываем через вызов соот-й функции. При открытии указывается имя файла БД. Если такого нету — он автоматически создается.
```
sqlite3 test.db
sqlite> .tables
sqlite> .exit
```
Допустимо открывать множество подключений к одной и тоже БД (через имя файла) в одном или разных приложениях.

Система использует механизмы блокировки доступа к файлу на уровне ОС, чтобы это все работало (эти механизмы обычно плохо работают на сетевых дисках, так что не рекомендуется использовать SQlite с файлом на сети).

Изначально SQlite работал по принципу «многие читают — один пишет». 
То есть только одно соединение пишет в БД в данный момент времени. Если другие соединения попробуют тоже записать, то словят ошибку SQLITE_BUSY.
Можно, однако, ввести таймаут операций. Тогда подключение, столкнувшись с занятостью БД, будет ждать N секунду прежде, чем отвалиться с ошибкой SQLITE_BUSY.

Write Ahead Log, WAL.
---------------------
Есть и еще одна возможность: не так давно появился новый вид лога SQlite: Write Ahead Log, WAL.
Если включить для БД именно этот режим лога, то несколько подключений смогут одновременно модифицировать БД. 
Но в этом режиме БД уже занимает несколько файлов.

у SQlite нет ГЛОБАЛЬНОГО КЭША
------------------------------
все современные RDBMS немыслимы без глобального разделяемого кэша, который может хранить несколько скомпилированных параметризованных запросов. Этим занят сервер, которого тут нет. Однако, в рамках одного приложения SQlite может разделять кэш между несколькими подключениями (www.sqlite.org/sharedcache.html) и немного сэкономить память.

настройки по умолчанию. 
-----------------------
Они работают на надежность, а не на производительность.

непонимание механизма фиксации транзакций. 
------------------------------------------
По умолчанию после любой команды SQlite будет фиксировать транзакцию (то есть ожидать пока БД окажется в целостном состоянии для отключения питания). В зависимости от режима паранойи SQLite потратит на это от 50 до 300 мс (ожидая окончания записи данных на диск).

Мне нужно вставить 100 тыс записей и быстро!
--------------------------------------------
Удалить индексы, включить режим синхронизации OFF (или NORMAL), вставлять порциями по N тысяч (N — подобрать, для начала взять 5000). Перед вставкой порции сделать BEGIN TRANSACTION, после — COMMIT.

sqlite> .help
--------------
```
.backup ?DB? FILE      Backup DB (default "main") to FILE
.bail ON|OFF           Stop after hitting an error.  Default OFF
.databases             List names and files of attached databases
.dump ?TABLE? ...      Dump the database in an SQL text format
                         If TABLE specified, only dump tables matching
                         LIKE pattern TABLE.
.echo ON|OFF           Turn command echo on or off
.exit                  Exit this program
.explain ?ON|OFF?      Turn output mode suitable for EXPLAIN on or off.
                         With no args, it turns EXPLAIN on.
.header(s) ON|OFF      Turn display of headers on or off
.help                  Show this message
.import FILE TABLE     Import data from FILE into TABLE
.indices ?TABLE?       Show names of all indices
                         If TABLE specified, only show indices for tables
                         matching LIKE pattern TABLE.
.load FILE ?ENTRY?     Load an extension library
.log FILE|off          Turn logging on or off.  FILE can be stderr/stdout
.mode MODE ?TABLE?     Set output mode where MODE is one of:
                         csv      Comma-separated values
                         column   Left-aligned columns.  (See .width)
                         html     HTML <table> code
                         insert   SQL insert statements for TABLE
                         line     One value per line
                         list     Values delimited by .separator string
                         tabs     Tab-separated values
                         tcl      TCL list elements
.nullvalue STRING      Use STRING in place of NULL values
.open ?FILENAME?       Close existing database and reopen FILENAME
.output FILENAME       Send output to FILENAME
.output stdout         Send output to the screen
.print STRING...       Print literal STRING
.prompt MAIN CONTINUE  Replace the standard prompts
.quit                  Exit this program
.read FILENAME         Execute SQL in FILENAME
.restore ?DB? FILE     Restore content of DB (default "main") from FILE
.schema ?TABLE?        Show the CREATE statements
                         If TABLE specified, only show tables matching
                         LIKE pattern TABLE.
.separator STRING      Change separator used by output mode and .import
.show                  Show the current values for various settings
.stats ON|OFF          Turn stats on or off
.tables ?TABLE?        List names of tables
                         If TABLE specified, only list tables matching
                         LIKE pattern TABLE.
.timeout MS            Try opening locked tables for MS milliseconds
.trace FILE|off        Output each SQL statement as it is run
.vfsname ?AUX?         Print the name of the VFS stack
.width NUM1 NUM2 ...   Set column widths for "column" mode
.timer ON|OFF          Turn the CPU timer measurement on or off
```

CREATE
-------
```
sqlite> create table mytable (id INTEGER PRIMARY KEY,f TEXT,l TEXT);
```
.table
-------
```
sqlite> .table
mytable
```

.schema ?TABLE?        Show the CREATE statements
-------------------------------------------------
If TABLE specified, only show tables matching LIKE pattern TABLE.
```
sqlite> .schema mytable
CREATE TABLE mytable (id INTEGER PRIMARY KEY,f TEXT,l TEXT);
```
INSERT INTO
-----------

```
insert into mytable (f,l) values ('john','smith');
```

SELECT
------
```
sqlite> select * from mytable;
1|john|smith

```
.read
------
```
sqlite> .read my.sql
```
my.sql
------
```
insert into mytable (f,l) values ('Mary','Ann');
insert into mytable (f,l) values ('Sam','Broun');
insert into mytable (f,l) values ('Chat','Gor');
```

sqlite> select * from mytable;
------------------------------
```
1|john|smith
2|Mary|Ann
3|Sam|Broun
4|Chat|Gor
```

.show Show the current values for various settings
--------------------------------------------------
```
     echo: off
  explain: off
  headers: off
     mode: list
nullvalue: ""
   output: stdout
separator: "|"
    stats: off
    width: 
```
.explain
---------
```
sqlite> .explain on
sqlite> select * from mytable;
id    f              l   
----  -------------  ----
1     john           smith
2     Mary           Ann 
3     Sam            Broun
4     Chat           Gor 
```
.dump
------
```
sqlite> .dump mytable
PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE mytable (id INTEGER PRIMARY KEY,f TEXT,l TEXT);
INSERT INTO "mytable" VALUES(1,'john','smith');
INSERT INTO "mytable" VALUES(2,'Mary','Ann');
INSERT INTO "mytable" VALUES(3,'Sam','Broun');
INSERT INTO "mytable" VALUES(4,'Chat','Gor');
COMMIT;
```

Python и база данных sqlite
============================
```
python
Python 2.7.6 (default, Mar 22 2014, 22:59:56) 
[GCC 4.8.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import sqlite3
>>> sqlite3.version
'2.6.0'

```
Connection объект 
------------------
Для использования модуля, сначала нужно создать Connection объект олицетворяет базу данных.

```
con = sqlite3.connect('test.db')
```
## cwd+'/db/test.db'
```
import os
cwd = os.getcwd()
print cwd
conn=sqlite3.connect(cwd+'/db/test.db')
```
Также можно использовать специальное имя :memory: для создания базы данных в ОЗУ

version1.py
----------
```
#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

con = None

try:
    con = lite.connect('test.db')
    
    cur = con.cursor()    
    cur.execute('SELECT SQLITE_VERSION()')
    
    data = cur.fetchone()
    
    print "SQLite version: %s" % data                
    
except lite.Error, e:
    
    print "Error %s:" % e.args[0]
    sys.exit(1)
    
finally:
    
    if con:
        con.close()

```
python version1.py 
------------------
```
SQLite version: 3.8.2
```
version2.py
-----------
```
#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

con = lite.connect('test.db')

with con:
    
    cur = con.cursor()    
    cur.execute('SELECT SQLITE_VERSION()')
    
    data = cur.fetchone()
    
    print "SQLite version: %s" % data  
```
python3:
--------
creating a new database with SQLite3
------------------------------------
```
import sqlite3

def create_database(db_name):
    with sqlite3.connect(db_name) as db:
        print("new database called {0} created".format(db_name))

if __name__ == "__main__":
    name = input("Please enter the name of the database you wish to create: ")
    create_database(name)
```
python2
-------
```
import sqlite3

def create_database(db_name):
    with sqlite3.connect(db_name) as db:
        print("new database called {0} created".format(db_name))

if __name__ == "__main__":
    name = raw_input("Please enter the name of the database you wish to create: ")
    create_database(name)
```

объект Cursor
=============
Создав объект Connection можно создать объект Cursor и вызвать его метод execute() для выполнения SQL команд:
```
db = sqlite3.connect("myshop.db")
cursor = db.cursor()

```
Создание таблицы 
-----------------
```
    sql = """create table Customer (
             CustomerID integer,
             FirstName text,
             LastName text,
             Street text,
             Town text,
             PostCode text,
             TelephoneNumber text,
             primary key (CustomerID))"""

    cursor.execute(sql)

```
Вставка ряда данных 
--------------------
```
cursor.execute('''insert into Customer values(1, "Adam","McNicol","1 Python Street","Cambridge","CB3 2YU","01223 467893")''') 

```
Сохранение (commit) изменений 
------------------------------
```
    db.commit()
```
Закрытие курсора, в случае если он больше не нужен 
---------------------------------------------------
```
cursor.close()
```
Test myshop.py
--------------
```
python myshop.py

sqlite3
SQLite version 3.8.2 2013-12-06 14:53:30
Enter ".help" for instructions
Enter SQL statements terminated with a ";"
sqlite> 


sqlite> .open myshop.db
sqlite> .table
Customer
sqlite> select * from Customer;
1|Adam|McNicol|1 Python Street|Cambridge|CB3 2YU|01223 467893
sqlite> .explain on
sqlite> select * from Customer;
Cust  FirstName      Last  Stre  Town  PostCode       Te
----  -------------  ----  ----  ----  -------------  --
1     Adam           McNicol  1 Python Street  Cambridge  CB3 2YU        01223 467893


```
Чтобы получить данные, после выполнения оператора SELECT, можно обработать курсор как итератор, вызвать метод fetchone() чтобы получить одиночный ряд, или вызвать fetchall() чтобы получить список соответствующих строк. Например:

print raw
---------
```
for row in cursor:
     print row

```
table1.py: fetchall
-------------------
```
import sqlite3

db = sqlite3.connect("myshop.db")
cursor = db.cursor()

cursor.execute('''insert into Customer values(2, "Nicol","McAdam","2 Cython Street","Cambridge","CB3 2YU","04567 467893")''') 

db.commit()

cursor.execute('SELECT * FROM Customer')

print cursor.fetchall()

cursor.close()

python table1.py 

```

cwd+'/db/example.db
-------------------
```
import sqlite3
import os

cwd = os.getcwd()
print cwd

db=sqlite3.connect(cwd+'/db/example.db')


```
with connect: table2.py
-----------------------
```
import sqlite3

db = sqlite3.connect("myshop.db")

with db:
    cursor = db.cursor()
    cursor.execute('''insert into Customer values(3, "Nic","Adam","2 Pillow Street","London","BB3 2YU","04567 467888")''') 
    cursor.execute('''insert into Customer values(4, "Ann","McDonald","55 Flowers Street","Glasgj","DB3 2YU","04567 466666")''') 
    cursor.execute('''insert into Customer values(5, "Tom","Adams","2 Django Street","Dublin","CE3 2YU","04567 467777")''') 

db.commit()

cursor.execute('SELECT * FROM Customer')

print cursor.fetchall()

cursor.close()

```
DB-API подстановка параметров
-----------------------------
Обычно для выполнения SQL операций необходимо использовать значения из переменных Python. Не рекомендуется собирать запрос используя строковые операции Питона потому что это может быть не безопасным, это делает программу уязвимой к инъекционным SQL атакам.

Вместо этого используйте DB-API подстановку параметров. Вставьте символ ? в качестве заполнителя в месте где вы хотите использовать значение и предоставьте кортеж значений в качестве второго аргумента метода курсора execute(). (Другие модули баз данных могут использовать другие заполнители, такие как %s или :l). Пример:

```
# Никогда не делайте так – это небезопасно! 
FirstName = 'Adam' 
cursor.execute("... where FirstName = '%s'" % FirstName) 
# Вместо этого делайте так 
t = (FirstName,) 
cursor.execute('select * from Customer where FirstName=?', t) 
```

values (?,?,?,?,?)', t) table3.py 
---------------------------------
```
import sqlite3

db = sqlite3.connect("myshop.db")
cursor = db.cursor()

val = [(6, "Trevor","Adams","25 Django Street","Dublin","CE3 5YU","04567 468777"),(7, "Tim","Doo","5 Django Street","Dublin","CE3 5YU","04567 468700"),(8, "Marry","Ann","7 Django Street","Dublin","CE3 5YU","04567 468700")]

for t in val: 
    cursor.execute('insert into Customer values (?,?,?,?,?,?,?)', t)

db.commit()

cursor.execute('SELECT * FROM Customer')

print cursor.fetchall()

cursor.close()

```
fetchone() table4.py 
--------------------
```
import sqlite3

db = sqlite3.connect("myshop.db")
cursor = db.cursor()

cursor.execute('SELECT * FROM Customer order by Town')
while True: 
    tmp=cursor.fetchone() 
    if tmp: 
        print tmp 
    else: 
        break 
cursor.close()
db.close()
```

DROP TABLE IF EXISTS 
--------------------
table5.py
```
import sqlite3

db = sqlite3.connect("myshop.db")


customers = (
    (1, "Adam","McNicol","1 Python Street","Cambridge","CB3 2YU","01223 467893"),
    (2, "Nicol","McAdam","2 Cython Street","Cambridge","CB3 2YU","04567 467893"),
    (3, "Nic","Adam","2 Pillow Street","London","BB3 2YU","04567 467888"),
    (4, "Ann","McDonald","55 Flowers Street","Glasgj","DB3 2YU","04567 466666"),
    (5, "Tom","Adams","2 Django Street","Dublin","CE3 2YU","04567 467777"),
    (6, "Trevor","Adams","25 Django Street","Dublin","CE3 5YU","04567 468777"),
    (7, "Tim","Doo","5 Django Street","Dublin","CE3 5YU","04567 468700"),
    (8, "Marry","Ann","7 Django Street","Dublin","CE3 5YU","04567 468700")
    )

sql = """create table Customer (
             CustomerID integer,
             FirstName text,
             LastName text,
             Street text,
             Town text,
             PostCode text,
             TelephoneNumber text,
             primary key (CustomerID))"""
with db:
    
    cursor = db.cursor()
    
    cursor.execute("DROP TABLE IF EXISTS Customer")
    cursor.execute(sql)
    cursor.executemany("INSERT INTO Customer VALUES(?, ?, ?, ?, ?, ?, ?)", customers)

cursor.execute('SELECT * FROM Customer order by Town')
while True: 
    tmp=cursor.fetchone() 
    if tmp: 
        print tmp 
    else: 
        break 
cursor.close()
db.close()
```

table6.py executescript()
-------------------------

```
import sqlite3
import sys

try:
    db = sqlite3.connect("myshop.db")

    cursor = db.cursor()  

    cursor.executescript("""
        DROP TABLE IF EXISTS Customer,
        create table Customer(CustomerID integer, FirstName text, LastName text, Street text, Town text, PostCode text, TelephoneNumber text, primary key (CustomerID));
        INSERT INTO Customer VALUES(1, "Adam","McNicol","1 Python Street","Cambridge","CB3 2YU","01223 467893");
        INSERT INTO Customer VALUES(2, "Nicol","McAdam","2 Cython Street","Cambridge","CB3 2YU","04567 467893");
        INSERT INTO Customer VALUES(3, "Nic","Adam","2 Pillow Street","London","BB3 2YU","04567 467888");
        INSERT INTO Customer VALUES(4, "Ann","McDonald","55 Flowers Street","Glasgj","DB3 2YU","04567 466666");
        INSERT INTO Customer VALUES(5, "Tom","Adams","2 Django Street","Dublin","CE3 2YU","04567 467777");
        INSERT INTO Customer VALUES(6, "Trevor","Adams","25 Django Street","Dublin","CE3 5YU","04567 468777");
        INSERT INTO Customer VALUES(7, "Tim","Doo","5 Django Street","Dublin","CE3 5YU","04567 468700");
        INSERT INTO Customer VALUES(8, "Marry","Ann","7 Django Street","Dublin","CE3 5YU","04567 468700");
        """)

    cursor.commit()
    
except sqlite3.Error, e:
    
    if db:
        db.rollback()
        
    print "Error %s:" % e.args[0]
    sys.exit(1)
    
finally:
    
    if db:
        cursor.execute('SELECT * FROM Customer order by Town')
        while True: 
            tmp=cursor.fetchone() 
            if tmp: 
                print tmp 
            else: 
                break 
        cursor.close()
        db.close() 

```


## Порядок работы:

- Создание соединения с базой данных. Если БД не существует то она будет создана, иначе файл будет открыт.
- Создание объекта курсора для взаимодействия с БД.
- Вставка кортежа со значениями
- db.commit()

Выборка данных 
==============

Выборка нескольких строк с данными table7.py:
---------------------------------------------
```
import sqlite3

db = sqlite3.connect("myshop.db")
cursor = db.cursor()

cursor.execute('SELECT * FROM Customer order by Town')

for row in cursor:
    print '-'*10
    print 'ID:', row[0]
    print 'First name:', row[1]
    print 'Second name:', row[2]
    print '-'*10

cursor.close()
db.close()
```

Выборка одной строки с данными table8.py:
-----------------------------------------
import sqlite3

db = sqlite3.connect("myshop.db")

with db:
    cursor = db.cursor()
    cursor.execute('SELECT * FROM Customer')
    data = cursor.fetchone()
    print data[0]

cursor.close()
db.close()
```

Есть возможность выбрать заданное количество строк, передав желаемое значение в курсор:
---------------------------------------------------------------------------------------
table9.py
```
import sqlite3

db = sqlite3.connect("myshop.db")

with db:
    cursor = db.cursor()
    cursor.execute('SELECT * FROM Customer')
    print cursor.fetchmany(2)

cursor.close()
db.close()
```

База данных в памяти
=====================
Если в вызове sqlite3_open() передать имя файла как ":memory:", то SQLite создаст соединение к новой (чистой) БД в памяти.

Это соединение абсолютно неотличимо от соединения к БД в файле по логике использования: доступен тот же набор SQL команд.

можно открыть два соединения к одной БД в памяти.
--------------------------------------------------
```
rc = sqlite3_open("file:memdb1?mode=memory&cache=shared", &db);

ATTACH DATABASE 'file:memdb1?mode=memory&cache=shared' AS aux1;
```

# last inserted row id
mem0.py
```
#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

con = lite.connect(':memory:')

with con:
    
    cur = con.cursor()    
    cur.execute("CREATE TABLE Friends(Id INTEGER PRIMARY KEY, Name TEXT);")
    cur.execute("INSERT INTO Friends(Name) VALUES ('Tom');")
    cur.execute("INSERT INTO Friends(Name) VALUES ('Rebecca');")
    cur.execute("INSERT INTO Friends(Name) VALUES ('Jim');")
    cur.execute("INSERT INTO Friends(Name) VALUES ('Robert');")
        
    lid = cur.lastrowid
    print "The last Id of the inserted row is %d" % lid
```

lastrowid returns None when you insert more than one row at a time with executemany
-----------------------------------------------------------------------------------
memory1.py:
```
import sqlite3


customers = (
    (1, "Adam","McNicol","1 Python Street","Cambridge","CB3 2YU","01223 467893"),
    (2, "Nicol","McAdam","2 Cython Street","Cambridge","CB3 2YU","04567 467893"),
    (3, "Nic","Adam","2 Pillow Street","London","BB3 2YU","04567 467888"),
    (4, "Ann","McDonald","55 Flowers Street","Glasgj","DB3 2YU","04567 466666"),
    (5, "Tom","Adams","2 Django Street","Dublin","CE3 2YU","04567 467777"),
    (6, "Trevor","Adams","25 Django Street","Dublin","CE3 5YU","04567 468777"),
    (7, "Tim","Doo","5 Django Street","Dublin","CE3 5YU","04567 468700"),
    (8, "Marry","Ann","7 Django Street","Dublin","CE3 5YU","04567 468700")
    )

sql = """create table Customer (
             CustomerID integer,
             FirstName text,
             LastName text,
             Street text,
             Town text,
             PostCode text,
             TelephoneNumber text,
             primary key (CustomerID))"""

db = sqlite3.connect(":memory:")

with db:
    
    cursor = db.cursor()
        
    cursor.execute(sql)
    cursor.executemany("INSERT INTO Customer VALUES(?, ?, ?, ?, ?, ?, ?)", customers)

# Note that lastrowid returns None when you insert more than one row at a time with executemany.
lid = cursor.lastrowid
print cursor.lastrowid

cursor.execute('SELECT * FROM Customer order by Town')
while True: 
    tmp=cursor.fetchone() 
    if tmp: 
        print tmp 

    else: 

        break 
cursor.close()
db.close()

```
memory2.py
-----------
```
import sqlite3

db = sqlite3.connect(":memory:")

with db:
    cursor = db.cursor() 
    cursor.execute('CREATE TABLE Customer(CustomerID integer, FirstName text, LastName text, Street text, Town text, PostCode text, TelephoneNumber text, primary key (CustomerID));')
    cursor.execute('INSERT INTO Customer VALUES(1, "Adam","McNicol","1 Python Street","Cambridge","CB3 2YU","01223 467893");')
    cursor.execute('INSERT INTO Customer VALUES(2, "Nicol","McAdam","2 Cython Street","Cambridge","CB3 2YU","04567 467893");')
    cursor.execute('INSERT INTO Customer VALUES(3, "Nic","Adam","2 Pillow Street","London","BB3 2YU","04567 467888");')
    cursor.execute('INSERT INTO Customer VALUES(4, "Ann","McDonald","55 Flowers Street","Glasgj","DB3 2YU","04567 466666");')
    cursor.execute('INSERT INTO Customer VALUES(5, "Tom","Adams","2 Django Street","Dublin","CE3 2YU","04567 467777");')
    cursor.execute('INSERT INTO Customer VALUES(6, "Trevor","Adams","25 Django Street","Dublin","CE3 5YU","04567 468777");')
    cursor.execute('INSERT INTO Customer VALUES(7, "Tim","Doo","5 Django Street","Dublin","CE3 5YU","04567 468700");')
    cursor.execute('INSERT INTO Customer VALUES(8, "Marry","Ann","7 Django Street","Dublin","CE3 5YU","04567 468700");')

    lid = cursor.lastrowid
    print cursor.lastrowid

```

Функции и константы модуля.
===========================
## sqlite3.PARSE_DECLTYPES
Эта константа предназначена для использования с параметром detect_types функции connect(). 

Установка ее позволяет модулю sqlite3 разбирать заявленный тип для каждой возвращаемой колонки. Разбор первого слова объявленного типа, такого как «целочисленное значение первичного ключа» будет воспринято как целочисленное число или для «number(10)» будет воспринято как «число». Далее для выбранной колонки будет просмотрен словарь конвертеров и будет использована та функция конвертера что зарегистрирована для данного типа.

## sqlite3.PARSE_COLNAMES
Эта константа предназначена для использования с параметром detect_types функции connect(). 
Установка этого параметра позволяет интерфейсу SQLite проанализировать имя каждого возвращаемого столбца. Он будет искать строки сформированные [mytype], и затем решит, что ‘mytype’ - тип столбца. Он попытается найти запись ‘mytype’ в словаре преобразователей и затем использует функцию преобразователя что бы возвратить значение. Имя столбца, найденное в Cursor.description, является только первым словом имени столбца, то есть если Вы используете что-то наподобие ‘as "x [datetime]"’ в SQL-запросе, тогда будет проанализировано все до первого пробела для имени столбца: имя столбца просто было бы “x”.

## sqlite3.connect(database[, timeout, detect_types, isolation_level, check_same_thread,factory, cached_statements])
Создает соединение с файлом database базы данных SQLite. Возможно использование “:memory:” для открытия соединения с базой данных находящейся в оперативной памяти вместо жесткого диска.

Когда к базе данных получают доступ многократные соединения, и один из процессов изменяет базу данных, база данных SQLite блокируется, до тех пор пока та транзакция не зафиксируется (commit). Параметр timeout определяет, сколько времени соединение должно ждать блокировки, чтобы уйти до возбуждения исключения. Значение по умолчанию для параметра тайм-аута 5.0 (пять секунд).

SQLite нативно поддерживает только следующие типы данных: TEXT, INTEGER, FLOAT, BLOB, NULL. Если имеется необходимость использовать другие типы, то реализация их поддержки является самостоятельной задачей. Использование параметра detect_types и специальных конверторов, зарегистрированных с помощью функции register_convertor(), позволит легко сделать это.

detect_types по умолчанию равен 0 (т.е., обнаружение типов выключено), возможные значения представляют собой любые комбинации PARSE_DECLTYPES и PARSE_COLNAMES.

По умолчанию модуль sqlite3 использует класс Connection для соединений. Тем не менее, возможно разделить на подклассы класс Connection и сделать connect() используя свой класс, указав его в параметре factory.
sqlite3 модуль использует внутренний кэш операторов что бы избежать издержек при парсинге SQL запросов. Что бы явно задать число операторов для кеширования, необходимо задать параметр cashed_statements. По умолчанию он равен значению 100.

## sqlite3.register_convertor(typename, callable)
Регистрирует вызываемый объект для преобразования строки байтов из базы данных в специальный тип данных Питона. Вызываемый объект будет вызываться для всех значений базы данных которые являются типа typename. Присвойте параметр detect_type функции connect() что бы посмотреть как работает детектирование типов. Помните что в случае typename и имя типа должны совпадать в вашем запросе.

## sqlite3.register_adapter(type, callable)
Регистрирует вызываемый объект для преобразования специального Питоновского типа данных type в один из типов поддерживаемых SQLite. Вызываемый объект callable принимает в качестве одиночного параметра значение Питона и должно возвращать значение следующих типов: int, long, float, str (в кодировке UTF-8), unicode, buffer.

convert Python decimal to SQLite numeric const2.py
---------------------------------------------------
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

d = D('4.12')

con = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_DECLTYPES)
cur = con.cursor()
cur.execute("create table test(d decimal)")

cur.execute("insert into test(d) values (?)", (d,))
cur.execute("select d from test")
data=cur.fetchone()[0]
print(data)
print(type(data))

cur.close()
con.close()
```

regtype1.py:
-------------
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

sql = """create table Product (
             ProductID integer,
             Name text,
             Price decimal,
             ProductTypeID integer,
             primary key (ProductID))
             """

db = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_DECLTYPES)
cur = db.cursor()
cur.execute(sql)

d = D('4.12')

cur.execute("insert into Product values (?, ?, ?, ?)", (1, 'test', d, 1,))
cur.execute("select * from Product")
data=cur.fetchone()
print data
print data[2]
print(type(data))

cur.close()
db.close()

```

## sqlite3.complete_statement(sql)
Возвращает True если строка sql содержит одно или более SQL операторов оканчивающихся точкой с запятой. Это не проверяет корректность синтаксиса SQL запроса, только то что не содержится не закрытых строковых символов и выражение заканчивается точкой с запятой.

## sqlite3.enable_callback_tracebacks(flag)
По умолчанию вы не будете получать traceback информацию в функциях определяемых пользователем преобразователях и т.д. Если вы хотите отладить их, то нужно вызвать эту функцию с параметром flag равным True. После этого вы будете получать traceback информацию на стандартное устройство вывода ошибок sys.stderr. Использование значения параметра flag равным False отключит данную функцию.

# Объекты Connection
## Class sqlite3.Connection
Класс соединения базы данных SQLite имеет следующие атрибуты и методы:
### Connection.isolation_level
Возвращает или устанавливает текущий уровень изоляции. Принимает значение None для режима автоматического принятия изменений (autocommit) или один из «DEFFERED», «IMMEDIATE», «EXCLUSIVE».

### Connection.cursor([cursorClass])
Параметр cursorClass должен быть частным классом курсора который бы расширил sqlite3.Cursor.

### Connection.commit()
Этот метод фиксирует текущую транзакцию. Если не вызвать этот метод, то все изменения сделанные с момента прошлого вызова commit() не будут видимы другим соединениям.

### Connection.rollback()
Этот метод отменяет все изменения сделанные прошлым вызовом commit().

### Connection.close()
Закрытие соединения с базой данных. Внимание!Этот метод не вызывает автоматически commit(), поэтмоу для сохранения всех изменений следует сперва вызывать commit().
```
Connection.execute(sql[,parameters]) 
Connection.executemany(sql[,parameters]) 
Connection.executescript(sql_script)
```
Это не стандартный ярлык, который создает промежуточный объект курсора вызывая метод курсора. Затем вызывая метод курсора execute/executemany/executescript с заданными параметрами.

### Connection.create_function(name, num_params, func)
Создает пользовательскую функцию с именем name которую потом можно использовать внутри SQL выражения. Параметр num_params задает число параметров принимаемой функцией, func это вызываемый объект Питона.
Функция может возвращать любой тип данных поддерживаемый SQLite: unicode, str, int, long, float,buffer,None.

## Пример func1.py:
-------------------
```
import sqlite3 
import md5 

def md5sum(t): 
    return md5.md5(t).hexdigest() 

con = sqlite3.connect(":memory:") 
con.create_function("md5", 1, md5sum) 
cur = con.cursor() 
cur.execute("select md5(?)", ("foo",)) 

print cur.fetchone()[0]

Результат:
cbd18db4cc2f85cedef654fccc4a4d8

```

### Connection.create_aggregate(name, num_params, aggregate_class)
Создать пользовательскую агрегированную (совокупную) функцию.
Агрегированный класс должен предоставлять метод step, который принимает число параметров num_params, и метод finalize, который будет возвращать окончательный результат.

Метод finalize может возвращать любой тип данных поддерживаемых SQLite.

## Пример func2.py:

```
import sqlite3 

class MySum: 
    def __init__(self): 
        self.count = 0 

    def step(self, value): 
        self.count += value 

    def finalize(self): 
        return self.count 

con = sqlite3.connect(":memory:") 
con.create_aggregate("mysum", 1, MySum) 
cur = con.cursor() 
cur.execute("create table test(i)") 
cur.execute("insert into test(i) values (1)") 
cur.execute("insert into test(i) values (10)") 
cur.execute("insert into test(i) values (15)") 

cur.execute("select mysum(i) from test") 
print cur.fetchall()
Результат:
[(26,)]
```
### Connection.create_collation(name, callable)
Создает функцию сравнения, параметр name – им функции, callable – вызываемый объект, которому будут передаваться два строковых параметра. Он возвращать -1 если первое значение меньше второго, 0 если равны и 1 если больше. Помните, что это управляется сортировкой (оператором ORDER BY в SQL запросе), поэтому ваше сравнение может не иметь силы для других SQL операций.
Помните, что все вызываемые объекты принимают параметры в качестве строки кодированной в UTF-8 кодировке. 

### Пример func3.py:
```
import sqlite3 

alphabet=[chr(i) for i in xrange(97,123)] 

def collate_reverse(string1, string2): 
    return -cmp(string1, string2) 

con = sqlite3.connect(":memory:") 
con.create_collation("reverse", collate_reverse) 
cur = con.cursor() 
cur.execute("create table test(x)") 
cur.executemany("insert into test(x) values (?)", alphabet) 

cur.execute("select x from test order by x") 
print 'print alphabet' 
print cur.fetchall() 

cur.execute("select x from test order by x collate reverse") 
print 'print reverse alphabet' 
print cur.fetchall() 

con.close()
Результат:
print alphabet 
[(u'a',), (u'b',), (u'c',), (u'd',), (u'e',), (u'f',), (u'g',), (u'h',), (u'i',), (u'j',), (u'k',), (u'l',), (u'm',), (u'n',), (u'o',), (u'p',), (u'q',), (u'r',), (u's',), (u't',), (u'u',), (u'v',), (u'w',), (u'x',), (u'y',), (u'z',)] 
print reverse alphabet 
[(u'z',), (u'y',), (u'x',), (u'w',), (u'v',), (u'u',), (u't',), (u's',), (u'r',), (u'q',), (u'p',), (u'o',), (u'n',), (u'm',), (u'l',), (u'k',), (u'j',), (u'i',), (u'h',), (u'g',), (u'f',), (u'e',), (u'd',), (u'c',), (u'b',), (u'a',)]
```
Чтобы удалить действие сравнения необходимо вызвать create_collation со значением параметра callable равным None:
```
con.create_collation(“reverse”,None)
```
### Connection.interrupt()

Вызов этого метода из различного потока прервет любые запросы, которые могут выполняться на соединении. Запрос будет отменен и вызывающая сторона получит исключение.

### Connection.set_authorizer(authorizer_callback)
Эта подпрограмма регистрирует функцию обратного вызова(callback). Обратный вызов вызывается для каждой попытки получить доступ к столбцу таблицы в базе данных. Обратный вызов должен возвратить SQLITE_OK, если доступ предоставлен, SQLITE_DENY, если весь SQL-оператор должен быть прерван с ошибкой и SQLITE_IGNORE, если столбец должен быть обработан как значение NULL. Эти константы доступны в sqlite3 модуле.
Первый параметр, передаваемый в функцию обратного вызова, означает, какого рода операция должна быть авторизированна. Второй и третий параметры должны быть аргументы или None в зависимости от первого аргумента. Четвертый аргумент это название базы данных (“main”,”temp” и т.д.) если это применимо. Пятый аргумент это имя внутреннего триггера or view that is responsible for the access attempt или None если это попытка доступа из самого SQL запроса.

signature:
----------
```
def select_authorizer(sqltype, arg1, arg2, dbname, source):
```
func4.py:
---------
```
import sqlite3 as sqlite

def select_authorizer(*args):  
    print(args)  
    return sqlite.SQLITE_OK  #should allow all operations           

conn = sqlite.connect(":memory:")
conn.execute("CREATE TABLE A (name integer PRIMARY KEY AUTOINCREMENT)")
conn.set_authorizer(select_authorizer)
conn.execute("SELECT * FROM A").fetchall() #should still work
```

## Connection.set_progress_handler(handler,n)

Эта подпрограмма регистрирует функцию обратного вызова(callback). Обратный вызов вызывается каждые n инструкций виртуальной машины SQLite. Это полезно если вы хотите быть вызванными из SQLite во время продолжительных операций, например для обновления GUI. Присвоение параметру значения None отключит работу данного метода.

## Connection.enable_load_extension(enabled)

Этот метод позволяет или не позволяет движку SQLite загружать библиотеки расширений, которые могут определять новые функции, агрегаты или реализации новых виртуальных таблиц. Хорошо известно расширение полнотекстового поиска поставляемое с SQLite. 


## Connection.load_extension(path)

Загрузка библиотеки расширений SQLite. Перед использованием необходимо включить поддержку расширений с помощью enable_load_extension(). 

Пример:
```
# пример работает если установлено дополнение полнотектсового поиска 

import sqlite3 
con = sqlite3.connect(":memory:") 
# enable extension loading 
con.enable_load_extension(True) 
# Load the fulltext search extension 
con.execute("select load_extension('./fts3.so')") 
# alternatively you can load the extension using an API call: 
# con.load_extension("./fts3.so") 
# disable extension laoding again 
con.enable_load_extension(False) 
# example from SQLite wiki 
con.execute("create virtual table recipe using fts3(name, ingredients)") 
con.executescript(""" 
        insert into recipe (name, ingredients) values ('broccoli stew', 'broccoli peppers cheese tomatoes'); 
        insert into recipe (name, ingredients) values ('pumpkin stew', 'pumpkin onions garlic celery'); 
        insert into recipe (name, ingredients) values ('broccoli pie', 'broccoli cheese onions flour'); 
        insert into recipe (name, ingredients) values ('pumpkin pie', 'pumpkin sugar flour butter'); 
        """) 
for row in con.execute("select rowid, name, ingredients from recipe where name match 'pie'"): 
    print row
```
### Connection.row_factory
Вы можете изменить этот атрибут на вызываемые объект, который принимает курсор и исходную строку как кортеж и возвращает реальную строку результата. Таким образом, Вы можете реализовать усовершенствованные способы возврата результатов, такие как возврат объекта, который может также получить доступ к столбцам по имени. 
## Пример func6.py:
```
# -*- coding: utf-8 -*- 
import sqlite3 

workers=(('John',3,10000),('Nik',5,15000)) 

def dict_factory(cursor, row): 
    d = {} 
    for idx, col in enumerate(cursor.description): 
        d[col[0]] = row[idx] 
    return d 

con = sqlite3.connect(":memory:") 
con.row_factory = dict_factory 
cur = con.cursor() 
cur.execute("create table test(name text, experience integer, screw integer)") 
cur.executemany('insert into test(name,experience,screw) values (?,?,?)',workers)
cur.execute('select * from test') 

for item in cur.fetchall(): 
    print 'worker %s have %i years of experience and %i $ of screw'%(item['name'],item['experience'],item['screw'])
Результат:

worker John have 3 years of experience and 10000 $ of screw 
worker Nik have 5 years of experience and 15000 $ of screw
```
Если возвращаемого кортежа недостаточно, и вы хотите основанный на имени доступ к столбцам, то вы должны рассматривать настройку row_factory как высоко-оптимизированную sqlite3.Row. Тип Row предоставляет доступ к столбцам, как на основе индексов, так и на основе чувствительным к регистру именам почти без издержек памяти. Это, возможно, даже лучшее решение чем собственный словарь или даже решение основанное на db_row.

## Connection.text_factory
Используя этот атрибут возможно контролировать какие объекты будут возвращены для типа данных TEXT. По умолчанию этот атрибут установлен в unicode и sqlite3 модуль возвратит объекты Unicode для типа данных TEXT. Если необходимо возвратить строки байтов вместо этого, то нужно установить значение str.
По причинам эффективности существует также другой способ возвращать объекты Unicode только для не-ASCII данных и строк байтов. Для его активации установите этот атрибут в значение sqlite3.OptimizedUnicode.

Также возможно присвоение ему любого вызываемого объекта принимающего на входе одиночную строку и возвращающую результирующий объект.

Для наглядности работы функции mystr изменяющей выходную кодировку строки использовалась консоль ОС Windows XP:
```
# -*- encoding: utf-8 -*- 
import sqlite3,sys 

def mystr(input): 
    # здесь можно сделать все что угодно 
    return unicode(input,'u8').encode('cp866') 
# подготавливаем данные 
data=['Россия'.decode('u8'),'England'] 

# создаем таблицу, вносим данные 
con = sqlite3.connect(":memory:") 
cur = con.cursor() 
cur.execute("create table country(name text)") 
for i in data: 
    cur.execute('insert into country values (?)',(i,)) 

print u'По умолчанию все объекты возвращаются типом Unicode' 
cur.execute('select * from country') 
for i in cur.fetchall(): 
    print i[0],type(i[0]) 

print '-'*10 
print u'Выходные данный типа str ' 
con.text_factory=str 
cur.execute('select * from country') 
for i in cur.fetchall(): 
    print i[0],type(i[0]) 

print '-'*10 
print u'Использование преобразующей функции mystr' 
con.text_factory=mystr 
cur.execute('select * from country') 
for i in cur.fetchall(): 
    print i[0],type(i[0]) 

print '-'*10 
print u'Использование OptimizedUnicode ' 
con.text_factory=sqlite3.OptimizedUnicode 
cur.execute('select * from country') 
for i in cur.fetchall(): 
    print i[0],type(i[0])
Результат:

По умолчанию все объекты возвращаются типом Unicode 
Россия <type 'unicode'> 
England <type 'unicode'> 
---------- 
Выходные данный типа str 
¦а¦-TБTБ¦¬TП <type 'str'> 
England <type 'str'> 
---------- 
Использование преобразующей функции mystr 
Россия <type 'str'> 
England <type 'str'> 
---------- 
Использование OptimizedUnicode 
Россия <type 'unicode'> 
England <type 'str'>
```
## Connection.total_changes
Возвращает общее число рядов которые были модифицированы, вставлены, или удалены с тех пор как было открыто соединение с базой данных.

## Connection.iterdump

Возвращает итератор к дампу базы данных в SQL текстовом формате. Полезна для сохранения базы данных в памяти для последующего восстановления. Эта функция обеспечивает те же самые возможности как .dump команда в оболочке sqlite3. 

### func7.py:
```
# -*- encoding: utf-8 -*- 
import sqlite3, sys 
# Подготавливаем данные БД 
alphabet=[chr(i) for i in xrange(97,123)] 
# Создаем первую БД и заполняем ее данными 
con=sqlite3.connect(':memory:') 
cur=con.cursor() 
cur.execute('create table test(s)') 
cur.executemany('insert into test values (?)',alphabet) 
con.commit() 
# делаем файл дамп данных первой базы 
with open('/tmp/dump.sql', 'w') as f: 
    for line in con.iterdump(): 
        f.write('%s\n' % line) 
con.close() 

# создаем вторую БД 
con=sqlite3.connect(':memory:') 

cur=con.cursor() 
# восстанавливаем дамп первой базы во второй 
dump=open('/tmp/dump.sql') 
for i in dump: 
    try: 
        cur.execute(i) 
    except: 
        print sys.exc_info() 
dump.close() 
# проверяем наличия данных 
cur.execute('select * from test') 
print cur.fetchall()

python func7.py 
(<class 'sqlite3.OperationalError'>, OperationalError('cannot commit - no transaction is active',), <traceback object at 0x7f4d178ea170>)
[(u'a',), (u'b',), (u'c',), (u'd',), (u'e',), (u'f',), (u'g',), (u'h',), (u'i',), (u'j',), (u'k',), (u'l',), (u'm',), (u'n',), (u'o',), (u'p',), (u'q',), (u'r',), (u's',), (u't',), (u'u',), (u'v',), (u'w',), (u'x',), (u'y',), (u'z',)]


```

# Объект Cursor
## Class sqlite3.Cursor
Экземпляр класса Cursor имеет следующие атрибуты и методы.
### Cursor.execute(sql[, parameters])
Выполнить SQL выражение, которое может иметь параметры (заполнители вместо SQL литералов). Модуль sqlite3 поддерживает 2 вида заполнителей: вопросительный знак (стиль qmark) и именованные заполнители.
Пример показывает как использовать параметры обоими стилями:
cur1.py
```
import sqlite3 
con = sqlite3.connect(":memory:") 
cur = con.cursor() 
cur.execute("CREATE TABLE people(name_last TEXT, age INTEGER)") 
cur.executemany("INSERT INTO people VALUES(?,?)",[('Smart',32),('Tesla',87),('Yeltsin',72)]) 

who = "Yeltsin" 
age = 72 
cur.execute("select name_last, age from people where name_last=? and age=?", (who, age)) 
print cur.fetchone() 

cur.execute("select name_last, age from people where name_last=:who and age=:age",{"who": who, "age": age}) 
print cur.fetchone()
Результаты:
(u'Yeltsin', 72) 
(u'Yeltsin', 72)
```

car5.py
```
#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

con = lite.connect('test.db')

with con:
    
    cur = con.cursor()    
    cur.execute("SELECT * FROM Cars")

    while True:
      
        row = cur.fetchone()
        
        if row == None:
            break
            
        print row[0], row[1], row[2]
```
# dictionary cursor
car6.py

```
#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite


con = lite.connect('test.db')    

with con:
    
    con.row_factory = lite.Row
       
    cur = con.cursor() 
    cur.execute("SELECT * FROM Cars")

    rows = cur.fetchall()

    for row in rows:
        print "%s %s %s" % (row["Id"], row["Name"], row["Price"])
```
execute() выполняет одиночное SQL выражение. Если попытаться выполнить более чем одно выражение то будет возбуждено Предупреждение. Используйте executescript() если необходимо выполнить многократные SQL выражения за один вызов.

### Cursor.executemany(sql, seq_of_parameters)
Выполнить команду SQL против всех последовательностей параметра или отображения, найденные в последовательности sql. sqlite3 модуль также позволяет использовать итератор вместо последовательности.
Пример с использованием итератора:
cur2.py
```
import sqlite3 

class IterChars: 
    def __init__(self): 
        self.count = ord('a') 
    def __iter__(self): 
        return self 
    def next(self): 
        if self.count > ord('z'): 
            raise StopIteration 
        self.count += 1 
        return (chr(self.count - 1),) # this is a 1-tuple 

con = sqlite3.connect(":memory:") 
cur = con.cursor() 
cur.execute("create table characters(c)") 
theIter = IterChars() 
cur.executemany("insert into characters(c) values (?)", theIter) 
cur.execute("select c from characters") 
print cur.fetchall()
```

car7.py
```
#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

uId = 1
uPrice = 62300 

con = lite.connect('test.db')

with con:

    cur = con.cursor()    

    cur.execute("UPDATE Cars SET Price=? WHERE Id=?", (uPrice, uId))        
    con.commit()
    
    print "Number of rows updated: %d" % cur.rowcount
```

car8.py
```
#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

uId = 4

con = lite.connect('test.db')

with con:

    cur = con.cursor()    

    cur.execute("SELECT Name, Price FROM Cars WHERE Id=:Id", 
        {"Id": uId})        
    con.commit()
    
    row = cur.fetchone()
    print row[0], row[1]
```

# Использование функций Python в SQLite
cript.py
```
import sqlite3

db_filename = 'todo.db'

def encrypt(s):
    print 'Encrypting %r' % s
    return s.encode('rot-13')

def decrypt(s):
    print 'Decrypting %r' % s
    return s.encode('rot-13')


with sqlite3.connect(db_filename) as conn:

    conn.create_function('encrypt', 1, encrypt)
    conn.create_function('decrypt', 1, decrypt)
    cursor = conn.cursor()

    # Raw values
    print 'Original values:'
    query = "select id, details from task"
    cursor.execute(query)
    for row in cursor.fetchall():
        print row

    print '\nEncrypting...'
    query = "update task set details = encrypt(details)"
    cursor.execute(query)
    
    print '\nRaw encrypted values:'
    query = "select id, details from task"
    cursor.execute(query)
    for row in cursor.fetchall():
        print row
    
    print '\nDecrypting in query...'
    query = "select id, decrypt(details) from task"
    cursor.execute(query)
    for row in cursor.fetchall():
        print row
```

Пример с использованием генератора:
cur3.py
```
import sqlite3 
def char_generator(): 
    import string 
    for c in string.letters[:26]: 
        yield (c,) 

con = sqlite3.connect(":memory:") 
cur = con.cursor() 
cur.execute("create table characters(c)") 
cur.executemany("insert into characters(c) values (?)", char_generator()) 
cur.execute("select c from characters") 
print cur.fetchall()
```
Результат в обоих случаях идентичный:
```
[(u'a',), (u'b',), (u'c',), (u'd',), (u'e',), (u'f',), (u'g',), (u'h',), (u'i',), (u'j',), (u'k',), (u'l',), (u'm',), (u'n',), (u'o',), (u'p',), (u'q',), (u'r',), (u's',), (u't',), (u'u',), (u'v',), (u'w',), (u'x',), (u'y',), (u'z',)]
```
### Cursor.executescript(sql_script)
Это не стандартный удобный метод позволяющий выполнить многократные SQL выражения за один раз. Сначала выполняется COMMIT объявление, затем выполняется SQL скрипт заданный как параметр. sql_script может быть как строка так и Unicode. Пример:
cur4.py
```
# -*- encoding: utf-8 -*- 
import sqlite3 

con = sqlite3.connect(":memory:") 
cur = con.cursor() 
cur.executescript(""" 
    create table person( 
        firstname, 
        lastname, 
        age 
        ); 
    create table book( 
        title, 
        author, 
        published 
        ); 
        insert into book(title, author, published) 
    values ( 
        'Dirk Gently''s Holistic Detective Agency', 
        'Douglas Adams', 
        1987 
        ); 
    """)


cur.execute("select * from book") 
print cur.fetchall()
```
### Cursor.fetchone()
Получить следующий ряд набора результатов запроса, возвращает одиночную последовательность или None если более не доступно данных.
### Cursor.fetchmany([size=cursor.arraysize])
Получить следующий набор рядов результатов запроса, возвращает список. Пустой список возвращается когда более нет доступных рядов.
Количество получаемых за раз рядов указывается параметром size. Если он не задан, то количество получаемых рядов определяется параметров arraysize курсора. Метод постарается получить настолько много рядов сколько указано параметром. Если это не возможно, то будет возвращено меньшее число рядов.

Существуют некоторые соображения производительности касательно параметра size. Для оптимальной производительности обычно лучше использовать атрибут arraysize. Если используется параметр size, то лучше для этого сохранить тоже самое значение от одного вызова fetchmany() до другого.

### Cursor.fetchall()
Получить все ряды результата запроса в виде списка. Примечательно что атрибут курсора arraysize может иметь воздействие на производительность данной операции. Пустой лист возвращается в случае отсутствия доступных рядов.
### Cursor.rowcount
Хотя класс Cursor модуля sqlite3 реализует этот атрибут, собственная поддержка его движком базы данных определения «строки на которые влияют/выбранные строки» является изворотливой.
Для выражений DELETE SQLite сообщает rowcont как 0 если сделать DELETE FROM table без каких либо условий.

Для выражения executemany() число модификаций суммируется вплоть до rowcount. Как требуется Спецификацией API DB Python, атрибут rowcount “-1 в случае, если никакой executeXX () не был выполнен на курсоре, или rowcount последней работы не определим интерфейсом”.

Так же это включает в себя оператор SELECT, потому что не возможно определить число рядов в результате запроса пока все строки не были выбраны.

### Cursor.lastrowid
Этот атрибут, доступный только для чтения, предоставляет id последнего модифицированного ряда. Он устанавливается только если был использован оператор INSERT в методе execute().Для других операций отличных от INSERT или когда вызван executemany() атрибут принимает значение None.

### Cursor.description
Этот атрибут доступный только для чтения, предоставляет колонку имен последнего запроса. Для соблюдения совместимости с Python DB API он возвращает кортеж из семи значений, 6 последних значений которого равны None.
Также это установлено для оператора SELECT без любых строк соответствия.


# Объект Row
## class sqlite3.Row
Экземпляр Row служит высоко-оптимизированным row_factory для объектов Connection. Он пытается подражать кортежу в большинстве своих функций. Поддерживает отображающийся доступ по имени столбца, индексу, итерации, представлению, равному тестированию и len().
Если два объекта Row имеют точно такие же столбцы и их элементы равны, то они сравниваются как равные.

## keys()
Этот метод возвращает кортеж с именами столбцов. Непосртедственно после запроса это первый член каждого кортежа в Cursor.description.
Пример row1.py:
```
# -*- coding: utf-8 -*- 
import sqlite3 
# создаем базу и заполянем ее одним значением 
conn = sqlite3.connect(":memory:") 
c = conn.cursor() 
c.execute('''create table stocks(date text, trans text, symbol text, qty real, price real)''') 
c.execute("""insert into stocks values ('2006-01-05','BUY','RHAT',100,35.14)""") 
conn.commit() 
c.close() 

# Демонстрируем возможности Row 
conn.row_factory = sqlite3.Row 
c = conn.cursor() 
c.execute('select * from stocks') 
r = c.fetchone() 
print 'type(r) = ',type(r) 
print 'r = ',r 
print 'len(r) = ',len(r) 
print 'r[2] = ',r[2] 
print 'r.keys() = ',r.keys() 
print 'r[qry] = ',r['qty'] 
for member in r: 
    print member
Результат:

type(r) = <type 'sqlite3.Row'> 
r = (u'2006-01-05', u'BUY', u'RHAT', 100.0, 35.140000000000001) 
len(r) = 5 
r[2] = RHAT 
r.keys() = ['date', 'trans', 'symbol', 'qty', 'price'] 
r[qry] = 100.0 
2006-01-05 
BUY 
RHAT 
100.0 
35.14
```

# SQLite и Python типы данных.

SQLite нативно поддерживает следующие типы: NULL, INTEGER, REAL, TEXT, BLOB. Нижеперечисленные типы Python могут быть посланы SQLite безо всяких проблем: 
```
Типы Python Типы SQLite
None        NULL
int         INTEGER
long        INTEGER
float       REAL
str(UTF-8)  TEXT
uncode      TEXT
buffer      BLOB
```
SQLite типы конвертируются в Python по умолчанию следующим образом:
```
Типы SQLite Типы Python
NULL        None
INTEGER     int или long, в зависимости от размера
REAL        float
TEXT        зависит от text_factory, по умолчанию unicode
BLOB        buffer
```
Система типов модуля sqlite3 позволяет расширяться двумя способами: возможно сохранение дополнительных типов Python в базе данных SQLite через адаптацию объектов или через преобразователи.

### Использование адаптеров для хранения дополнительных типов Python в базах данных SQLite
SQLite поддерживает только ограниченные типы данных нативно. Для использования других типов данных Python в SQLite базах данных необходимо адаптировать их к оному из поддерживаемых модулем sqlite3 типу: None, int, long, float, str,Unicode, buffer.

Модуль sqlite3 использует адаптацию объектов Python, описанную в PEP 246. 

Используется протокол PrepareProtocol.

Существует два способа настроить модуль sqlite3 для адаптации специальных типов Python.

### Объект адаптирующий самого себя.
Это хороший подход, если вы пишете собственный класс. Для того что бы поместить экземпляр класса в колонку базы данных, в первую очередь нужно выбрать один из поддерживаемых типов данных который будет использован для переназначения. Затем нужно назначить классу метод __conform__(self,protocol) который будет возвращать конвертированное значение.

В примере ниже в качестве конвертируемого типа используется str, параметр protocol равен PrepareProtocol proto1.py:
```
import sqlite3 

class Point(object): 
    def __init__(self, x, y): 
        self.x, self.y = x, y 

    def __conform__(self, protocol): 
        if protocol is sqlite3.PrepareProtocol: 
            return "%f;%f" % (self.x, self.y) 

con = sqlite3.connect(":memory:") 
cur = con.cursor() 

p = Point(4.0, -3.2) 
cur.execute("select ?", (p,)) 
print cur.fetchone()[0]
Результат:
4.000000;-3.200000
```
## Регистрация функции адаптера.
Другой возможностью является создание функции которая конвертирует тип в строковое представление и регистрирует функцию с помощью register_adapter().

Тип/класс чтобы адаптироваться должен быть классом нового стиля, т.е. должен иметь object в качестве одного из своих оснований.

Предыдущий пример примет следующий вид proto2.py:
```
import sqlite3 

class Point(object): 
    def __init__(self, x, y): 
        self.x, self.y = x, y 

def adapt_point(point): 
    return "%f;%f" % (point.x, point.y) 

sqlite3.register_adapter(Point, adapt_point) 

con = sqlite3.connect(":memory:") 
cur = con.cursor() 

p = Point(4.0, -3.2) 
cur.execute("select ?", (p,)) 
print cur.fetchone()[0]
Реузльтат:
4.000000;-3.200000
```
Модуль sqlite3 имеет по умолчанию 2 адаптера для Python типов datetime.date и datetime.datetime. 
Пример в котором объект datetime.datetime хранится не в ISO представлении, а как штамп времени UNIX:
proto3.py
```
import sqlite3 
import datetime, time 

def adapt_datetime(ts): 
    return time.mktime(ts.timetuple()) 

sqlite3.register_adapter(datetime.datetime, adapt_datetime) 

con = sqlite3.connect(":memory:") 
cur = con.cursor() 

now = datetime.datetime.now() 
cur.execute("select ?", (now,)) 
print cur.fetchone()[0]
```
Результат:
1299207380.0

## Конвертация SQLite значений в специальные типы Python.
Функции конверторов принимают в качестве параметра строку и возвращают преобразованный Python тип.
Функции конверторов всегда вызываются со строкой, не важно какой тип данных был послан из SQLite.
Интерпретация получаемых данных как типов Python модулем sqlite3 осуществляется либо неявно через объявление типов либо явно через имя столбца (использование констант PARSE_DECTYPES и PARSE_COKNAMES соответственно). 
Пример ниже раскрывает оба этих случая:
convert1.py
```

# -*- coding: utf-8 -*- 
import sqlite3 

class Point(object): 
    def __init__(self, x, y): 
        self.x, self.y = x, y 

    def __repr__(self): 
        return "(%f;%f)" % (self.x, self.y) 

def adapt_point(point): 
    return "%f;%f" % (point.x, point.y) 

def convert_point(s): 
    x, y = map(float, s.split(";")) 
    return Point(x, y) 

# Регистрируем функуию адаптер 
sqlite3.register_adapter(Point, adapt_point) 

# Регистрируем функцию конвертор 
sqlite3.register_converter("point", convert_point) 

p = Point(4.0, -3.2) 

######################### 
# 1) Используем объявление типа 
con = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_DECLTYPES) 
cur = con.cursor() 
cur.execute("create table test(p point)") 
cur.execute("insert into test(p) values (?)", (p,)) 
cur.execute("select p from test") 
result=cur.fetchone()[0] 
print "with declared types:", result,type(result) 
cur.close() 
con.close() 

####################### 
# 2) Используем имена столбцов 
con = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_COLNAMES) 
cur = con.cursor() 
cur.execute("create table test(p)") 
cur.execute("insert into test(p) values (?)", (p,)) 
cur.execute('select p as "p [point]" from test') 
result=cur.fetchone()[0] 
print "with column names:",result,type(result) 
cur.close() 
con.close()
Результат:
with declared types: (4.000000;-3.200000) <class '__main__.Point'> 
with column names: (4.000000;-3.200000) <class '__main__.Point'>
```

## Адаптеры и конверторы по умолчанию.
Для типов date и datetime в модуле datetime существуют базовые адаптеры, которые будут посланы в SQLite как ISO даты / ISO временные метки.
Базовые конверторы зарегистрированы под именем “date” для типа datetime.date и под именем “timestamp” для типа datetime.datetime.

Таким образом, можно использовать даты и временные метки из Python без каких либо дополнительных махинаций в большинстве случаев. Формат адаптеров также совместим с экспериментальными функциями даты и времени SQLite.

convert2.py
```
import sqlite3 
import datetime 

con = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES) 
cur = con.cursor() 
cur.execute("create table test(d date, ts timestamp)") 

today = datetime.date.today() 
now = datetime.datetime.now() 

cur.execute("insert into test(d, ts) values (?, ?)", (today, now)) 
cur.execute("select d, ts from test") 
row = cur.fetchone() 
print today, "=>", row[0], type(row[0]) 
print now, "=>", row[1], type(row[1]) 

cur.execute('select current_date as "d [date]", current_timestamp as "ts [timestamp]"') 
row = cur.fetchone() 
print "current_date", row[0], type(row[0]) 
print "current_timestamp", row[1], type(row[1])
Результат:
2011-03-05 => 2011-03-05 <type 'datetime.date'> 
2011-03-05 12:31:20.712000 => 2011-03-05 12:31:20.712000 <type 'datetime.datetime'> 
current_date 2011-03-05 <type 'datetime.date'> 
current_timestamp 2011-03-05 01:31:20 <type 'datetime.datetime'>
```

## Inserting images
car9.py
```
#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys


def readImage():

    try:
        fin = open("woman.jpg", "rb")
        img = fin.read()
        return img
        
    except IOError, e:

        print "Error %d: %s" % (e.args[0],e.args[1])
        sys.exit(1)

    finally:
        
        if fin:
            fin.close()


try:
    con = lite.connect('test.db')
    
    cur = con.cursor()
    data = readImage()
    binary = lite.Binary(data)
    cur.execute("INSERT INTO Images(Data) VALUES (?)", (binary,) )

    con.commit()    
    
except lite.Error, e:
    
    if con:
        con.rollback()
        
    print "Error %s:" % e.args[0]
    sys.exit(1)
    
finally:
    
    if con:
        con.close()  
```
# Reading images
img2.py

```
#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys


def writeImage(data):
    
    try:
        fout = open('woman2.jpg','wb')
        fout.write(data)
    
    except IOError, e:    
        print "Error %d: %s" % (e.args[0], e.args[1])
        sys.exit(1)
        
    finally:
        
        if fout:
            fout.close()       
    

try:
    con = lite.connect('test.db')
    
    cur = con.cursor()    
    cur.execute("SELECT Data FROM Images LIMIT 1")
    data = cur.fetchone()[0]
    
    writeImage(data)

    
except lite.Error, e:
    
    print "Error %s:" % e.args[0]
    sys.exit(1)
    
finally:
    
    if con:
        con.close()      
```
# Контроль транзакций.
По умолчанию модуль sqlite3 открывает транзакции неявно перед оператором языка модификации данных (DML) таких как INSERT,UPDATE,DELETE,REPLACE и фиксирует транзакции неявно перед выражениями, не относящимися к DML или запросам (т.е. что-либо другое кроме SELECT или вышеупомянутого).
Так, если Вы в пределах транзакции и даете команду как CREATE TABLE..., VACUUM, PRAGMA, sqlite3 модуль будет фиксировать изменения неявно прежде, чем выполнить ту команду. Есть две причины для этого. Прежде всего, некоторые из этих команд не работают в пределах транзакций. Другая причина состоит в том, что sqlite3 должен отследить состояние транзакции (если транзакция является активной или нет).

Вы можете контролировать какого рода выражения BEGIN выполняются (или не выполняются вовсе) неявно через параметр isolation_level при вызове connect() или через свойство соединений isolation_level.

Если вы хотите автоматический режим фиксации изменений, то необходимо установить isolation_level в значение None.

Иначе оставьте этот параметр по умолчанию, результатом которого будет простой оператор BEGIN или установите его в один из поддерживаемых уровней изоляций: DEFERRED, IMMEDIATE, EXCLUSIVE.

transaction.py
```
#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys


try:
    con = lite.connect('test.db')
    cur = con.cursor()    
    cur.execute("DROP TABLE IF EXISTS Friends")
    cur.execute("CREATE TABLE Friends(Id INTEGER PRIMARY KEY, Name TEXT)")
    cur.execute("INSERT INTO Friends(Name) VALUES ('Tom')")
    cur.execute("INSERT INTO Friends(Name) VALUES ('Rebecca')")
    cur.execute("INSERT INTO Friends(Name) VALUES ('Jim')")
    cur.execute("INSERT INTO Friends(Name) VALUES ('Robert')")
    
    #con.commit()
            
except lite.Error, e:
    
    if con:
        con.rollback()
    
    print "Error %s:" % e.args[0]
    sys.exit(1)
    
finally:
    
    if con:
        con.close() 
```
transaction1.py
```
#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys


try:
    con = lite.connect('test.db')
    cur = con.cursor()    
    cur.execute("DROP TABLE IF EXISTS Friends")
    cur.execute("CREATE TABLE Friends(Id INTEGER PRIMARY KEY, Name TEXT)")
    cur.execute("INSERT INTO Friends(Name) VALUES ('Tom')")
    cur.execute("INSERT INTO Friends(Name) VALUES ('Rebecca')")
    cur.execute("INSERT INTO Friends(Name) VALUES ('Jim')")
    cur.execute("INSERT INTO Friends(Name) VALUES ('Robert')")

    cur.execute("CREATE TABLE IF NOT EXISTS Temporary(Id INT)")
            
except lite.Error, e:
    
    if con:
        con.rollback()
    
    print "Error %s:" % e.args[0]
    sys.exit(1)
    
finally:
    
    if con:
        con.close() 
```
transaction2.py
```
#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys


try:
    con = lite.connect('test.db', isolation_level=None)
    cur = con.cursor()    
    cur.execute("DROP TABLE IF EXISTS Friends")
    cur.execute("CREATE TABLE Friends(Id INTEGER PRIMARY KEY, Name TEXT)")
    cur.execute("INSERT INTO Friends(Name) VALUES ('Tom')")
    cur.execute("INSERT INTO Friends(Name) VALUES ('Rebecca')")
    cur.execute("INSERT INTO Friends(Name) VALUES ('Jim')")
    cur.execute("INSERT INTO Friends(Name) VALUES ('Robert')")

    
except lite.Error, e:    
    
    print "Error %s:" % e.args[0]
    sys.exit(1)
    
finally:
    
    if con:
        con.close() 
```
# Использование методов ярлыка
Используя нестандартные методы execute(), executemany() и executescript() объекта Connection ваш код будет более кратким, потому что не будет явно создан объект Cursor, вместо этого он будет создан неявно и эти методы ярлыка возвращают объект курсора. Таким образом, вы можете выполнить оператор SELECT и выполнить итерации по нему используя только один вызов к объекту Connection.
example4.py
```
import sqlite3 

persons = [ 
    ("Hugo", "Boss"), 
    ("Calvin", "Klein")] 

con = sqlite3.connect(":memory:") 
con.execute("create table person(firstname, lastname)") 
con.executemany("insert into person(firstname, lastname) values (?, ?)", persons) 
for row in con.execute("select firstname, lastname from person"): 
    print row 

print "I just deleted", con.execute("delete from person where 1=1").rowcount, "rows"
Результат:
(u'Hugo', u'Boss') 
(u'Calvin', u'Klein') 
I just deleted 2 rows
```
# Доступ к столбцам по имени вместо индекса
Одна из полезных возможностей модуля sqlite3 является класс sqlite3.Row разработанный чтобы быть использованным как фабрика рядов.

К рядам, обернутыми в этот класс, можно получить доступ как по индексам (подобно кортежам) так и, без влияния регистра, по имени.
example5.py
```
# -*- coding: utf-8 -*- 
import sqlite3 

con = sqlite3.connect(":memory:") 
con.row_factory = sqlite3.Row 

cur = con.cursor() 
cur.execute("CREATE TABLE people(name_last,age)") 
cur.execute("INSERT INTO people values (?,?)",[(u'Порощенко'),25]) 
cur.execute("select name_last, age from people") 
for row in cur: 
    assert row[0] == row["name_last"] 
    assert row["name_last"] == row["nAmE_lAsT"] 
    assert row[1] == row["age"] 
    assert row[1] == row["AgE"] 
print row[0],row[1]
Результатом будет отсутствие ошибок и результирующий вывод:
Порощенко 25
```
# Использование соединения как менеджера контекста.

Объекты соединения могут использоваться в качестве менеджеров по контексту, которые автоматически фиксируют или откатывают транзакции. В случае исключения откатывается транзакция; иначе, транзакция фиксируется:

example6.py
```
# -*- coding: utf-8 -*- 
import sqlite3 

con = sqlite3.connect(":memory:") 
con.execute("create table person (id integer primary key, firstname varchar unique)") 

# Будет выполненно успешно, con.commit() будет вызван автоматически 
with con: 
    con.execute("insert into person(firstname) values (?)", ("Joe",)) 

# con.rollback() будет вызван после блока with окончившегося исключением 
# которое должно быть перехвачено и корректно обработано 
try: 
    with con: 
        con.execute("insert into person(firstname) values (?)", ("Joe",)) 
except sqlite3.IntegrityError: 
    print "couldn't add Joe twice"
Результат:
couldn't add Joe twice
```
## Export and import of data
backup.py

```
#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

cars = (
    (1, 'Audi', 52643),
    (2, 'Mercedes', 57642),
    (3, 'Skoda', 9000),
    (4, 'Volvo', 29000),
    (5, 'Bentley', 350000),
    (6, 'Hummer', 41400),
    (7, 'Volkswagen', 21600)
)

def writeData(data):
    
    f = open('cars.sql', 'w')
    
    with f:
        f.write(data)


con = lite.connect(':memory:')

with con:
    
    cur = con.cursor()
    
    cur.execute("DROP TABLE IF EXISTS Cars")
    cur.execute("CREATE TABLE Cars(Id INT, Name TEXT, Price INT)")
    cur.executemany("INSERT INTO Cars VALUES(?, ?, ?)", cars)
    cur.execute("DELETE FROM Cars WHERE Price < 30000")
    
    data = '\n'.join(con.iterdump())
    
    writeData(data)
```
revers.py
```
#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys


def readData():
    
    f = open('cars.sql', 'r')
    
    with f:
        data = f.read()
        return data
        

con = lite.connect(':memory:')

with con:   

    cur = con.cursor()
    
    sql = readData()
    cur.executescript(sql)
    
    cur.execute("SELECT * FROM Cars")
    
    rows = cur.fetchall()
    
    for row in rows:
        print row    
```

# Мультипоточность.
У более старых версий SQLite были проблемы с совместным использованием соединений между потоками. Именно поэтому модуль Python отвергает совместное использование соединений и курсоров между потоками. Если Вы все еще попытаетесь сделать так, то вы получите исключение во время выполнения.
Единственное исключение это вызов метода interrupt() который имеет смысл вызвать только из другого потока.

# Использование SQLite в многопоточных приложениях

SQLite может быть собран в однопоточном варианте (параметр компиляции SQLITE_THREADSAFE = 0). 

В этом варианте его нельзя одновременно использовать из нескольких потоков, поскольку полностью отсутствует код синхронизации. Зачем? Для бешеной скорости. 

Проверить, есть ли многопоточность можно через вызов sqlite3_threadsafe(): если вернула 0, то это однопоточный SQLite.

По умолчанию, SQLite собран с поддержкой потоков.

Есть два способа использования многопоточного SQLite: serialized и multi-thread.

Serialized (надо указать флаг SQLITE_OPEN_FULLMUTEX при открытии соединения). В этом режиме потоки могут как угодно дергать вызовы SQLite, никаких ограничений. Но все вызовы блокируют друг друга и обрабатываются строго последовательно.

Multi-thread (SQLITE_OPEN_NOMUTEX). В этом режиме нельзя использовать одно и то же соединение одновременно из нескольких потоков (но допускается одновременное использование разных соединений разными потоками). Обычно используется именно этот режим.

# Всегда используйте UTF-8. 

# Поддержка UNICODE

По умолчанию — нету поддержки. Надо создать свой collation (способ сравнения) через sqlite3_create_collation .
И определить свои встроенные функции like(), upper(), lower() через www.sqlite.org/c3ref/create_function.html.

Значение внутри БД может принадлежать к одному из следующих типов хранения (storage class):
- NULL, 
- INTEGER (занимает 1,2,3,4,6 или 8 байт), 
- REAL (число с плавающей точкой, 8 байт в формате IEEE), 
- TEXT (строка в формате данных базы, обычно UTF-8), 
- BLOB (двоичные данные, хранятся «как есть»).

# Порядок сортировки значений разных типов:
- NULL меньше всего (включая другой NULL);
- INTEGER и REAL меньше любого TEXT и BLOB, между собой сравниваются арифметически;
- TEXT меньше любого BLOB, между собой сравниваются на базе своих collation;
- BLOB-ы сравниваются между собой через memcmp().

SQLite выполняет неявные преобразования типов «на лету» в нескольких местах:
- при занесении значения в столбец (тип столбца задает рекомендацию по преобразованию);
- при сравнении значений между собой.

Столбец может иметь следующие рекомендации приведения типа: TEXT, NUMERIC, INTEGER, REAL, NONE.

Значения BLOB и NULL всегда заносятся в любой столбец «как есть».

В столбец TEXT значения TEXT заносятся «как есть», значения INTEGER и REAL становятся строками.
В столбец NUMERIC, INTEGER числа записываются «как есть», а строки становятся числами, если _могут_ (то есть допустимо обратное преобразование «без потерь»).
Для столбца REAL правила похожи на INTEGER(NUMERIC); отличие в том, что все числа представлены в формате с плавающей запятой.
В столбец NONE значения заносятся «как есть» (этот тип используется по умолчанию, если не задан другой).

При сравнении значений разного типа между собой может выполняться дополнительное преобразование типов.

При сравнении числа со строкой, если строка может быть преобразована в число «без потерь», она становится числом.

в SQLite в уникальном индексе может быть сколько угодно NULL значений (с этим согласен Oracle и не согласен MS SQL).

# Присоединение одновременно к нескольким БД

Чтобы открыть соединение к БД используется вызов sqlite3_open().

В любой момент времени мы можем к открытому соединению присоединить еще до 10 баз данных через SQL команду ATTACH DATABASE.
```
sqlite3_open('foo.sqlite3', &db); // откроем соединение к БД в файле "foo.sqlite3"

sqlite3_exec(&db, "ATTACH 'bar.sqlite3' AS bar", ... ); // присоединим "bar.sqlite3"
```

Теперь все таблицы БД в файле db1.sqlite3 стали прозрачно доступны в нашем соединении.

Для разрешения конфликтов имен следует использовать имя присоединения (основная база называется «main»):
```
SELECT * FROM main.my_table UNION SELECT * FROM bar.my_table
```

Ничего не мешает присоединить к БД новую базу в памяти и использовать ее для кэширования и пр.
```
sqlite3_open('foo.sqlite3', &db); // откроем соединение к БД в файле "foo.sqlite3"

sqlite3_exec(&db, "ATTACH ':memory:' AS mem", ... ); // присоединим новую БД в памяти
```

Это очень полезная возможность. Присоединяемые БД должны иметь формат данных такой же, как и у основной БД, иначе — ошибка.

# Временная база данных

Передайте пустую строку вместо имени файла в sqlite3_open() и будет создана временная БД в файле на диске. Причем, после закрытия соединения к БД, она будет удалена с диска.

# Тонкие настройки БД через команду PRAGMA

SQL команда PRAGMA служит для задания всевозможных настроек у соединения или у самой БД:
```
  PRAGMA name; // запросить текущее значение параметра name

  PRAGMA name = value; // задать параметр name значением value
```
meta1.py
```
#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

con = lite.connect('test.db')

with con:
    
    cur = con.cursor()    
    
    cur.execute('PRAGMA table_info(Cars)')
    
    data = cur.fetchall()
    
    for d in data:
        print d[0], d[1], d[2]
```

meta2.py
```
#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

con = lite.connect('test.db')

with con:
    
    cur = con.cursor()    
    cur.execute('SELECT * FROM Cars')
    
    col_names = [cn[0] for cn in cur.description]
    
    rows = cur.fetchall()
    
    print "%s %-10s %s" % (col_names[0], col_names[1], col_names[2])

    for row in rows:    
        print "%2s %-10s %s" % row
```

meta3.py
```
#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

con = lite.connect('test.db')

with con:
    
    cur = con.cursor()    
    cur.execute("SELECT name FROM sqlite_master WHERE type='table'")

    rows = cur.fetchall()

    for row in rows:
        print row[0]
```
Настройку соединения следует проводить сразу после открытия и до его использования.

- PRAGMA page_size = bytes; // размер страницы БД; страница БД - это единица обмена между диском и кэшом, разумно сделать равным размеру кластера диска (у меня 4096)

- PRAGMA cache_size = -kibibytes; // задать размер кэша соединения в килобайтах, по умолчанию он равен 2000 страниц БД

- PRAGMA encoding = "UTF-8";  // тип данных БД, всегда используйте UTF-8

- PRAGMA foreign_keys = 1; // включить поддержку foreign keys, по умолчанию - ОТКЛЮЧЕНА

- PRAGMA journal_mode = DELETE | TRUNCATE | PERSIST | MEMORY | WAL | OFF;  // задать тип журнала

- PRAGMA synchronous = 0 | OFF | 1 | NORMAL | 2 | FULL; // тип синхронизации транзакции


# Журнал и фиксация транзакций

SQLite тщательно блюдет целостность данных в БД (ACID), реализуя механизм изменения данных через транзакции.

Кратко о транзакциях: транзакция либо полностью накатывается, либо полностью откатывается. Промежуточных состояний быть не может.

Если вы не используете транзакции явно (BEGIN; ...; COMMIT;), то всегда создается неявная транзакция. Она стартует перед выполнением команды и коммитится сразу после.

SQLite может вставлять и до 50 тыс записей в секунду, но фиксировать транзакций он не может больше, чем ~ 50 в секунду.

Именно поэтому, не получается вставлять записи быстро, используя неявную транзакцию.

При настройках по умолчанию SQLite гарантирует целостность БД даже при отключении питания в процессе работы.

Достигается подобное поведение ведением журнала (специального файла) и хитроумным механизмом синхронизации изменений на диске.

## Кратко обновление данных в БД работает так: 

-  до любой модификации БД SQLite сохраняет изменяемые страницы из БД в отдельном файле (журнале), то есть просто копирует их туда;
- убедившись, что копия страниц создана, SQLite начинает менять БД;
- убедившись, что все изменения в БД «дошли до диска» и БД стала целостной, SQLite стирает журнал.

Если SQLite открывает соединение к БД и видит, что журнал уже есть, он соображает, что БД находится в незавершенном состоянии и автоматически откатывает последнюю транзакцию.

То есть механизм восстановления БД после сбоев, фактически, встроен в SQLite и работает незаметно для пользователя.

По умолчанию журнал ведется в режиме DELETE .

PRAGMA journal_mode = DELETE

Это означает, что файл журнала удаляется после завершения транзакции. Сам факт наличия файла с журналом в этом режиме означает для SQLite, что транзакция не была завершена, база нуждается в восстановлении. Файл журнала имеет имя файла БД, к которому добавлено "-journal".

В режиме TRUNCATE файл журнала обрезается до нуля (на некоторых системах это работает быстрее, чем удаление файла). 

В режиме PERSIST начало файла журнала забивается нулями (при этом его размер не меняется и он может занимать кучу места).

В режиме MEMORY файл журнала ведется в памяти и это работает быстро, но не гарантирует восстановление базы при сбоях (копии данных нет на диске).

А можно и совсем отключить журнал (PRAGMA journal_mode = OFF). В этой ситуации перестает работать откат транзакций (команда ROLLBACK) и база, скорее всего, испортится, если программа будет завершена аварийно.

Для базы данных в памяти режим журнала может быть только либо MEMORY, либо OFF.

## Как же SQLite «убеждается», что база всегда будет целостной?

Мы знаем, что современные системы используют хитроумное кэширование для повышения производительности и могут откладывать запись на диск.

Допустим, SQLite завершил запись в БД и хочет стереть файл журнала, чтобы отметить факт фиксации транзакции. 

А вдруг файл сотрется раньше, чем обновится БД?

Если в этот промежуток времени отключится питание, то журнала уже не будет, а БД еще не будет целостной — потеря данных! 

Короче говоря, хитроумный механизм фиксации изменений должен полагаться на некоторые гарантии со стороны дисковой системы и ОС.

PRAGMA synchronous задает степень «паранойи» SQLite на это счет. 

Режим OFF (или 0) означает: SQLite считает, что данные фиксированы на диске сразу после того как он передал их ОС (то есть сразу после вызова соот-го API ОС).

Это означает, что целостность гарантирована при аварии приложения (поскольку ОС продолжает работать), но не при аварии ОС или отключении питания. 

Режим синхронизации NORMAL (или 1) гарантирует целостность при авариях ОС и почти при всех отключениях питания. Существует ненулевой шанс, что при потере питания в самый неподходящий момент база испортится. Это некий средний, компромисный режим по производительности и надежности.

Режим FULL гарантирует целостность всегда и везде и при любых авариях. Но работает, разумеется, медленнее, поскольку в определенных местах делаются паузы ожидания. И это режим по умолчанию.


# Режим журнала WAL

По умолчанию, режим журнала БД всегда «возвращается» в DELETE. Допустим, мы открыли соединение к БД и установили режим PERSIST. Изменили данные, закрыли соединение.

На диске остался файл журнала (начало которого забито нулями).

Открываем соединение к БД снова. Если не задать режим журнала в этом соединении, он опять будет работать в DELETE. Как только мы обновим данные, механизм фиксации транзакций сотрет файл журнала.

Режим журнала WAL работает иначе — он «постоянный». Как только мы перевели базу в режим WAL, она останется в этом режиме, пока ей явно не поменяют режим журнала на другой.

Изначально SQLite проектировалась как встроенная БД. Архитектура разделения одновременного доступа к данным была устроена примитивно: одновременно несколько соединений могут читать БД, а вот записывать в данный момент времени может только одно соединение. Это, как минимум, означает, что пишущее соединение ждет «освобождения» БД от читающих. При попытке записать в «занятую» БД приложение получает ошибку SQLITE_BUSY. Достигается этот механизм разделения доступа через API блокировки файлов (которые плохо работают на сетевых дисках, поэтому там не рекомендуется использовать SQLite; )

В режиме WAL (Write-Ahead Logging) «читатели» БД и «писатели» в БД уже не мешают друг другу, то есть допускается модификация данных при одновременном чтении. Короче говоря, это шаг в сторону больших и серьезных СУБД, в которых все так и есть. Утверждается также, что SQLite в WAL работает быстрее.

Но есть и недостатки:
- БД занимает несколько файлов (файлы «XXX-wal» и «XXX-shm»);
- плохо работает на больших транзакциях (условно, если транзакция больше 50 Мбайт);
- нельзя открыть такую БД в режиме «только чтение»;
- возникает дополнительная операция checkpoint.

Фактически, в режиме WAL данные БД разделяются между БД и файлом журнала. Операция checkpoint переносит данные в БД. По умолчанию, это делается автоматически, если журнал занял 1000 страниц БД.
То есть, идут быстрые COMMIT-ы и вдруг какой-то COMMIT задумался и начал делать checkpoint. Если такое поведение нежелательно, можно делать checkpoint вручную (когда все спокойно), можно это делать и в отдельном процессе.

# Пределы

Несмотря на миниатюрность, SQLite в реальности не накладывает серьезных ограничений на размеры полей, таблиц или БД.

- По умолчанию, BLOB или строкое значение могут занимать 1 Гбайт и это же ограничение размера одной записи (можно поднять до 2^31 — 1, параметр SQLITE_MAX_LENGTH).

- Количество столбцов: 2000 (можно поднять до 32767, SQLITE_MAX_COLUMN).

- Размер SQL оператора: 1 МБайт (1073741824 байт, SQLITE_MAX_SQL_LENGTH).

- Одновременный join: 64 таблицы.

- Присоединить баз к соединению: 10 (до 62, SQLITE_MAX_ATTACHED)

- Максимальное количество страниц в БД: 1073741823 (до 2147483646, SQLITE_MAX_PAGE_COUNT).

- Если задать размер страницы 65636 байт, то максимальный размер БД будет примерно 14 Терабайт.

- Максимальное число записей в таблице: 2^64 — 1, но на практике, конечно, ограничение размера вступит раньше.

