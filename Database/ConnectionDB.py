import sqlite3
from sys import path
from Database.DB_Utilities import db_connection_string

class Queries:
    def __init__(self):
        self.connection_string = db_connection_string
        self.cursor = None
        self.conn = None

    def __OpenConnection(self):
        self.conn = sqlite3.connect(self.connection_string)
        self.cursor = self.conn.cursor()

    def __ExecuteQueryCommon(self, pQuery):
        self.__OpenConnection()
        self.cursor.execute(pQuery)

    def ExecuteSelectQuery(self, pQuery):
        self.__ExecuteQueryCommon(pQuery)
        # self.conn.close()
        return self.cursor.fetchall()

    def ExecuteDeleteQuery(self, pQuery):
        try:
            self.__ExecuteQueryCommon(pQuery)
            self.conn.commit()
        except:
            print("Error")            
            self.conn.rollback()
        finally:
            self.cursor.close()
            self.conn.close()


    