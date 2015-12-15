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
db.commit()

cur.execute("select * from Product")

data=cur.fetchall()
print data

cur.close()
db.close()
