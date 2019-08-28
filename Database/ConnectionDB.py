# Generals
import sqlite3

#  Specifics
from sys import path
from Database.DB_Utilities import db_connection_string
from Exceptions import DatabaseException as DE
from Logs import LogHandler as LH
from Logs.Constants import database_folder as log_folder

class Queries:
    def __init__(self):
        self.connection_string = db_connection_string
        self.cursor = None
        self.conn = None

    def __OpenConnection(self):
        try:
            self.conn = sqlite3.connect(self.connection_string)
            self.cursor = self.conn.cursor()

        except Exception as e:
            LH.Handler(log_folder, 'ConnectionDB', 'Queries', '__OpenConnection', e)   
            raise DE.ConnectionDB_Exception

    def __ExecuteQueryCommon(self, pQuery):
        self.__OpenConnection()
        self.cursor.execute(pQuery)

    def ExecuteSelectQuery(self, pQuery):
        try:
            self.__ExecuteQueryCommon(pQuery)
            result = self.cursor.fetchall()        
            return result

        except Exception as e:
            LH.Handler(log_folder, 'ConnectionDB', 'Queries', 'ExecuteSelectQuery', e)            
            raise DE.ConnectionDB_Exception()

        finally:
            self.conn.close()

    def ExecuteDeleteQuery(self, pQuery):
        try:
            self.__ExecuteQueryCommon(pQuery)
            self.conn.commit()

        except Exception as e:
            self.conn.rollback()
            LH.Handler(log_folder, 'ConnectionDB', 'Queries', 'ExecuteDeleteQuery', e)     
            raise DE.ConnectionDB_Exception()

        finally:
            self.cursor.close()
            self.conn.close()