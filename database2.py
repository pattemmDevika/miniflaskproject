import sqlite3
connection=sqlite3.connect('database2.db')
print("database connected")
connection.execute("CREATE TABLE details(name text,email text,password text)")
print("table created")
connection.close()