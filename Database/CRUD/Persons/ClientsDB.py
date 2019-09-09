# ** Specifics **

# Database
from Database.DB_Utilities import client, dic_tables
from Database.CRUD.SelectQueries import SelectQ

# Entities
from Entities.Persons.Client import Client as Cli

# Fields
from Database.CRUD.Persons.ClientUtilities import client_fields as cf
from Database.CRUD.Persons import ClientUtilities as CU


# Tables
t_client = dic_tables[client]

# Client's Fields
c_id = cf[CU.ID]
c_name = cf[CU.Name]
c_lastname = cf[CU.Lastname]
c_adress = cf[CU.Adress]
c_location = cf[CU.Location]
c_email = cf[CU.Email]
c_birthdate = cf[CU.Birthdate]
c_user_registry = cf[CU.UserRegistry]
c_date_registry = cf[CU.DateRegistry]

def GetAllClients():    
    Q = SelectQ() 
    clients = Q.select_table(t_client)
    
    lst_clients = []

    for r in clients:
        ID = r[c_id]
        name = r[c_name]
        lastname = r[c_lastname]
        location = r[c_location]
        adress = r[c_adress]
        # email = r[c_email] # forget to add email to database, have to fix that
        email = 'Email_testing@test.com'
        birthdate = r[c_birthdate]
        user_registry = r[c_user_registry]
        date_registry = r[c_date_registry]

        cli = Cli(ID, name, lastname, location, adress, email, birthdate, user_registry, date_registry)

        lst_clients.append(cli)

    return lst_clients