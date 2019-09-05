# Generals
import sqlite3

#  Specifics
from sys import path
from Exceptions import DatabaseException as DE
from Logs import LogHandler as LH
from Logs.Constants import database_folder as log_folder

#Database Tools
from Database.DB_ContextManager import DB_ContextManager as DB_CM
from Database.DB_Utilities import db_connection_string

class Queries:
    def __init__(self):
        pass

    def ExecuteSelectQuery(self, pQuery):
        with DB_CM(db_connection_string, pQuery) as cur:
            result = cur.fetchall()
            return result

    def ExecuteSelectNonQuery(self, pQuery):
        with DB_CM(db_connection_string, pQuery): 
            pass