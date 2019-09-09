from Database.CRUD.Persons.ClientsDB import GetAllClients
print(GetAllClients())


from Database.CRUD.Persons.ClientsDB import GetAllClients
from Services.Utilities.Persons.PersonsUtilities import c_fields
from Services.Utilities.Persons import PersonsUtilities as PU
from Entities.Persons.Client import Client
clients = GetAllClients()

lst_clients_json = []
for Client(cli) in clients:
    print(cli.na)