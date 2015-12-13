import sqlite3

db = sqlite3.connect("myshop.db")
cursor = db.cursor()

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

cursor.execute('''insert into Customer values(1, "Adam","McNicol","1 Python Street","Cambridge","CB3 2YU","01223 467893")''') 

db.commit()

cursor.close()
