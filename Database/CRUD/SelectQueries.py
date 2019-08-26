from Database.DB_Utilities import dic_tables
from Database.CRUD.Queries import Queries

class SelectQ(Queries):
    def __init__(self, pCursor):
        super().__init__(pCursor)

    #Execute the query wrote in other methods
    def __SelectDefault(self, pQuery):
        self.cursor.execute(pQuery)
        print(self.cursor.fetchall())

    #Loop over each table and returns its data
    def select_all(self):
        for k, v in dic_tables.items():
            query = "SELECT * FROM {0}".format(v)
            self.__SelectDefault(query)

    #Returns an specific table data
    def select_table(self, pTable):
        query = "SELECT * FROM {0}".format(pTable)
        self.__SelectDefault(query)