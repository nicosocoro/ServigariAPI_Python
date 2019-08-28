import sqlite3
from Database.DB_Utilities import db_connection_string
from Utilities.DateHandler import today_YYYYMMDD

# *** IMPORTANT ***
# Descriptions are typed in Spanish
#
#
# *****************

try:
    # Define data to set into Audit Information in Query
    dic_query = {
        'user': 'Admin',
        'today': today_YYYYMMDD
        }
    conn = sqlite3.connect(db_connection_string)
    c = conn.cursor()

    # Client
    c.execute("""INSERT INTO Client
                VALUES
                (1, 'Name1', 'LastName2', 'Address1', 'Location1', 19620608, :user, :today),
                (2, 'Name2', 'LastName2', 'Address2', 'Location2', 19860216, :user, :today)
    """, dic_query)

    #Telephone
    c.execute("""INSERT INTO Telephone
                VALUES
                (1, 123456, 'Celular', :user, :today),
                (2, 564812, 'Fijo', :user, :today),
                (3, 624881, 'Celular', :user, :today)
    """, dic_query)

    #Client_Telephone
    c.execute("""INSERT INTO Client_Telephone
                VALUES
                (1, 1, 1),
                (2, 1, 2),
                (3, 2, 3)
    """, dic_query)

    #Product_Type
    c.execute("""INSERT INTO Product_Type
                VALUES
                (1, 'Microondas', :user, :today),
                (2, 'Tostadora', :user, :today),
                (3, 'Secador de Pelo', :user, :today),
                (4, 'Lavarropas', :user, :today)
    """, dic_query)

    #Trademark
    c.execute("""INSERT INTO Trademark
                VALUES
                (1, 'Samsung', :user, :today),
                (2, 'LG', :user, :today),
                (3, 'Phillips', :user, :today)
    """, dic_query)

    #Product
    c.execute("""INSERT INTO Product
                VALUES
                (1, 'Producto 1', :user, :today, 1, 2),
                (2, 'Producto 2', :user, :today, 1, 1),
                (3, 'Producto 3', :user, :today, 4, 2)
    """, dic_query)

    #Registry
    c.execute("""INSERT INTO Registry
                VALUES
                (1, 'Registry1', 2366.12, :user, :today, 1, 1),
                (2, 'Registry2', 1200.00, :user, :today, 1, 2),
                (3, 'Registry3', 6200.50, :user, :today, 2, 2),
                (4, 'Registry4', 2000.00, :user, :today, 1, 3)
    """, dic_query)

    conn.commit()
    print("Commit")

except Exception as e:
    print("Message Error: {0}".format(e))
    conn.rollback()

finally:
    conn.close()