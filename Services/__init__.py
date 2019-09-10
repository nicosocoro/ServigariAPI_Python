# *** Generals *** 
import os
import markdown # Used to convert to HTML the content of README.md

# API message
from Services.Utilities import GenericUtilities

# *** Specifics *** 
# Manage API requests
from flask import Flask
app = Flask(__name__)

# Log register
from Logs import LogHandler as LH
from Logs.Constants import API_folder as log_API_folder

@app.route('/')
def main():
    # Guided by https://www.youtube.com/watch?v=4T5Gnrmzjak&list=PLznhi6Wjqv_s9ObOVrTDWr23Zw_Qzvtm4&index=3&t=0s
    # highly recommended channel

    try:
        return "Hello, worlds"
        # path = os.path.dirname(app.root_path) + '/README.md'
        # with open(path, 'r') as markdown_file:

        #     # Open README.md as readonly file
        #     content = markdown_file.read()

        #     # Convert the content to HTML
        #     return markdown.markdown(content)
    except Exception as e:
        LH.Handler(log_API_folder, '__init__', '', 'main', e)

# Clients
@app.route('/Clients')
def get():
    from Database.CRUD.Persons.ClientsDB import GetAllClients
    from Services.Utilities.Persons.PersonsUtilities import c_fields
    from Services.Utilities.Persons import PersonsUtilities as PU
    from Entities.Persons.Client import Client

    # Get a list of Clients' instances
    clients = GetAllClients()

    lst_clients_json = []

    # Loop over each Client instance and create a JSON
    for cli in clients:
        cli_json = {
            c_fields[PU.c_id]: cli.ID,
            c_fields[PU.c_name]: cli.Name,
            c_fields[PU.c_lastname]: cli.Lastname,
            c_fields[PU.c_location]: cli.Location,
            c_fields[PU.c_adress]: cli.Adress,
            c_fields[PU.c_email]: cli.Email,
            c_fields[PU.c_birthdate]: cli.Birthdate,
            c_fields[PU.c_user_registry]: cli.UserRegistry,
            c_fields[PU.c_date_registry]: cli.DateRegistry
        }

        # Add the JSON to the final list
        lst_clients_json.append(cli_json)
    
    return {
        'message': GenericUtilities.success_msg,
        'data': lst_clients_json
    }
