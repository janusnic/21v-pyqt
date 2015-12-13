#!/usr/bin/env python
# encoding: utf-8

"""Control access to columns using an authorizer function.
"""
#end_pymotw_header

import sqlite3

db_filename = 'todo.db'
 
con = sqlite3.connect(db_filename) # Warning: This file is created in the current directory
con.execute("DROP TABLE IF EXISTS todo")
con.execute("CREATE TABLE todo (id INTEGER PRIMARY KEY, priority INTEGER, details char(100) NOT NULL, project char(100) NOT NULL, status bool NOT NULL)")
con.execute("INSERT INTO todo (id,priority,details,project,status) VALUES (0, 1,'Read Google News','pymotw',0)")
con.execute("INSERT INTO todo (id,priority,details,project,status) VALUES (1, 2,'Visit the Python website','pymotw',1)")
con.execute("INSERT INTO todo (id,priority,details,project,status) VALUES (2, 3,'See how flask differs from bottle','pymotw',1)")
con.execute("INSERT INTO todo (id,priority,details,project,status) VALUES (3, 1,'Watch the latest from the Slingshot Channel','pymotw',0)")
con.commit()
con.close()

def authorizer_func(action, table, column, sql_location, ignore):
    print '\nauthorizer_func(%s, %s, %s, %s, %s)' % \
        (action, table, column, sql_location, ignore)

    response = sqlite3.SQLITE_OK # be permissive by default

    if action == sqlite3.SQLITE_SELECT:
        print 'requesting permission to run a select statement'
        response = sqlite3.SQLITE_OK
    
    elif action == sqlite3.SQLITE_READ:
        print 'requesting access to column %s.%s from %s' % \
            (table, column, sql_location)
        if column == 'details':
            print '  ignoring details column'
            response = sqlite3.SQLITE_IGNORE
        elif column == 'priority':
            print '  preventing access to priority column'
            response = sqlite3.SQLITE_DENY

    return response

with sqlite3.connect(db_filename) as conn:
    conn.row_factory = sqlite3.Row
    conn.set_authorizer(authorizer_func)

    print 'Using SQLITE_IGNORE to mask a column value:'
    cursor = conn.cursor()
    cursor.execute("""
    select id, details from todo where project = 'pymotw'
    """)
    for row in cursor.fetchall():
        print row['id'], row['details']

    print '\nUsing SQLITE_DENY to deny access to a column:'
    cursor.execute("""
    select id, priority from todo where project = 'pymotw'
    """)
    for row in cursor.fetchall():
        print row['id'], row['details']
