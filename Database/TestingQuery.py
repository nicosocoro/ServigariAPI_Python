import sqlite3
import Database.CRUD.DeleteQueries as DQ
import Database.CRUD.SelectQueries as SQ
from Database.DB_Utilities import db_connection_string

#MAIN
def Main():
    try:        
        S = SQ.SelectQ()
        # D = DQ.DeleteQ()
        
        #D.delete_all()
        results = S.select_all()
        print(results)


    except Exception as e:
        print("Error message: ", e)