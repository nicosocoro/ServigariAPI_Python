import sqlite3
from sys import path
from Database.DB_Utilities import db_connection_string

class Queries:
    def __init__(self, pCursor):
        self.connection_string = db_connection_string
        self.cursor = pCursor
        self.conn = None

    def __OpenConnection__(self):
        self.conn = sqlite3.connect(self.connection_string)

    