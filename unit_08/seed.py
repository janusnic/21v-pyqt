
from database_functions import query

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
    products = [("Signature",4.0,4),("Delight",3.5,4)]
    insert_product_data(products)
    