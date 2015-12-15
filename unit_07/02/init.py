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
