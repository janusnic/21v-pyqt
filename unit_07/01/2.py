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
