from os import getenv 
from sys import argv
import sqlite3
from dotenv import load_dotenv 
from db import Database 
load_dotenv() 


# CREATE DATABASE
if argv[1] == "create" and argv[2] == "database":
    db = Database(getenv("DB_FILE")) 
    print("database created")  


# CREATE TABLE  
if argv[1] == "create" and argv[2] == "table" and argv[3]:
    table_name = argv[3]
    try:
        db = Database(getenv("DB_FILE")) 
        db.create_table(f"CREATE TABLE {table_name}(id INTEGER PRIMARY KEY AUTOINCREMENT, field1 TEXT, field2 INTEGER)")
        print(f"table {table_name!r} created")
    except sqlite3.Error as error:
        print(f"failed to create table {table_name!r}", error)


# INSERT DATA TO EXISTING TABLE
if argv[1] == "insert" and argv[2] == "data" and len(argv) > 4:
    table_name = argv[3] 
    field1 = argv[4] 
    field2 = argv[5]
    try:
        db = Database(getenv("DB_FILE"))
        db.insert_data(table_name, None, field1, field2)
        print(f"data has beed inserted from {table_name!r} table")
    except sqlite.Error as error:
        print(f"failed to insert data to {table_name!r}", error)


# DELETE SINGLE/MULTIPLE RECORD/S FROM EXISTING TABLE  |   delete data 'table_name' 'field_id1' 'field_id2' 'field_idn'
if argv[1] == 'delete' and argv[2] == 'data':
    table_name = argv[3] 
    if len(argv) < 5:
        field_id = argv[4]
        try:
            sql_update_query = f"DELETE FROM {table_name} WHERE ID={field_id}"
            db = Database(getenv("DB_FILE")) 
            db.delete_single_record(sql_update_query)
        except sqlite3.Error as error:
            print(f"failed to delete record from {table_name!r}", error)
    else:
        ids = []
        for i in range(4, len(argv)):
            ids.append(argv[i])
        try:
            sql_update_query = f"DELETE FROM {table_name} WHERE ID=?"
            db = Database(getenv("DB_FILE"))
            db.delete_multiple_record(sql_update_query, ids)
        except sqlite3.Error as error:
            print(f"failed to delete multiple records from {table_name!r}", error)


# DELETE ALL ROWS FROM TABLE
if argv[1] == 'delete' and argv[2] == 'all' and argv[3] == 'rows':
    table_name = argv[4]
    try:
        sql_update_query = f"DELETE FROM {table_name};"
        db = Database(getenv("DB_FILE"))
        db.delete_all_record(sql_update_query)
    except sqlite3.Error as error:
        print(f"failed to delete all records from {table_name!r}", error)


if argv[1] == "close" and argv[2] == "database":
    db = Database(getenv("DB_FILE"))
    db.close()