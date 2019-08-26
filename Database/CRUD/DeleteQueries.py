# from sys import path as p

from Database.DB_Utilities import dic_tables
from Database.ConnectionDB import Queries

class DeleteQ(Queries):
    def __init__(self):
        super().__init__()

    #Delete all data defined in all tables
    #It restart all tables
    def delete_all(self):
        for k, v in dic_tables.items():
            query = "DELETE FROM {0}".format(v)
            self.ExecuteDeleteQuery(query)