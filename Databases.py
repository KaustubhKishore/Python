#  import sqlite3
#  db=sqlite3.connect(":memory:")
#  splite3.show(db)
#
# Traceback (most recent call last):
#   File "<pyshell#2>", line 1, in <module>
#     splite3.show(db)
# NameError: name 'splite3' is not defined
#  sqlite3.show(db)
#
# Traceback (most recent call last):
#   File "<pyshell#3>", line 1, in <module>
#     sqlite3.show(db)
# AttributeError: 'module' object has no attribute 'show'
#  cursor=db.cursor()
#  cursor.execute('create table employee(empid integer Primary Key,name varchar)')
# <sqlite3.Cursor object at 0x000000000404F500>
#  cursor.execute('show tables')
#
# Traceback (most recent call last):
#   File "<pyshell#6>", line 1, in <module>
#     cursor.execute('show tables')
# OperationalError: near "show": syntax error
#  cursor.execute('show * from empid')
#
# Traceback (most recent call last):
#   File "<pyshell#7>", line 1, in <module>
#     cursor.execute('show * from empid')
# OperationalError: near "show": syntax error
#  db.commit()
#  cursor.execute('select * from employee')
# <sqlite3.Cursor object at 0x000000000404F500>

# cursor.execute('insert into employee (empid,name) values (:empid,:name)',{'empid':2,'name':'ram'})

