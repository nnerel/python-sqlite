import sqlite3
from sqlite3 import connect 


class Database:

    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def __str__(self):
        return self.db_name

    def close(self):
        self.connection.close()

    def create_table(self, data):
        self.cursor.execute(data)
        self.connection.commit() 
        
    def insert_data(self, table_name, *values):
        self.cursor.execute(f"""INSERT INTO {table_name} VALUES({','.join(['?' for _ in values])})""", values)
        self.connection.commit()

    def delete_single_record(self, sql_update_query):
        self.cursor.execute(sql_update_query)
        self.connection.commit()

    def delete_multiple_record(self, sql_update_query, ids):
        self.cursor.executemany(sql_update_query, ids)
        self.connection.commit()

    def delete_all_record(self, sql_update_query):
        self.cursor.execute(sql_update_query)
        self.connection.commit()