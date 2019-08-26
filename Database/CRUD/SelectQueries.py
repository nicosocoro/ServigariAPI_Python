from Database.DB_Utilities import dic_tables
from Database.ConnectionDB import Queries

class SelectQ(Queries):
    def __init__(self):
        super().__init__()

    #Loop over each table and returns its data
    def select_all(self):
        for k, v in dic_tables.items():
            query = "SELECT * FROM {0}".format(v)
            return self.ExecuteSelectQuery(query)

    #Returns an specific table data
    def select_table(self, pTable):
        query = "SELECT * FROM {0}".format(pTable)
        return self.ExecuteSelectQuery(query)