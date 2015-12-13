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