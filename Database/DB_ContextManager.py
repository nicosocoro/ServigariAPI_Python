"""
Here goes all decorators functions that handles the connection to the DB and
the queries execution

My original idea was defining these funcitons inside each class but had some issues
when trying to use a class method as a decorator.
"""

# Generals
import sqlite3

#  Specifics
from Logs import LogHandler as LH
from Logs.Constants import database_folder as log_folder
from Exceptions import DatabaseException as DE

class DB_ContextManager():
    def __init__(self, db_connection, pQuery):
        self.db_connection = db_connection
        self.query = pQuery

    def __enter__(self):
        try:
            self.conn = sqlite3.connect(self.db_connection)
            cur = self.conn.cursor()
            cur.execute(self.query)
            self.conn.commit()
            return cur            

        except Exception as e:
            LH.Handler(log_folder, 'DB_ContextManager', 'DB_ContextManager', '__enter__', e)
            self.conn.rollback()
            raise DE.ConnectionDB_Exception()

    def __exit__(self, exc_type, exc_val, exc_tb): # obligatory params
        self.conn.close()
