import sqlite3
import Database.CRUD.DeleteQueries as DQ
import Database.CRUD.SelectQueries as SQ
from Database.DB_Utilities import db_connection_string

#MAIN
def Main():
    try:
        conn = sqlite3.connect(db_connection_string)
        cur = conn.cursor()
        
        S = SQ.SelectQ(cur)
        D = DQ.DeleteQ(cur)
        
        #D.delete_all()
        S.select_all()

        conn.commit()

    except Exception as e:
        print("Error message: ", e)
        conn.rollback()

    finally:
        conn.close()