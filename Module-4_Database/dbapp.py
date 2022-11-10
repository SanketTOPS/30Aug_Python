import sqlite3

try:
    dbcon=sqlite3.connect("mydb.db")
    print("Database connected!")
except Exception as e:
    print(e)

# Create Table
tbl_create="create table studinfo(id int primary key, name text, sub text)"
try:
    dbcon.execute(tbl_create)
    print("Table created!")
except Exception as e:
    print(e)

# Insert data
insert_data="insert into studinfo values (1,'mitesh','python'),(2,'hitesh','java'),(3,'ashok','php'),(4,'nirav','react')"
try:
    dbcon.execute(insert_data)
    dbcon.commit()
    print("Record inserted!")
except Exception as e:
    print(e)