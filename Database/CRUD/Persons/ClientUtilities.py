from Database.DB_Utilities import UserRegistry, DateRegistry, audit_fields

# Audit information
__user_registry = audit_fields[UserRegistry]
__date_registry = audit_fields[DateRegistry]

# Client table's fields
# Constants fields
ID = 'f_id'
Name = 'f_name'
Lastname = 'f_lastname'
Adress = 'f_adress'
Location = 'f_location'
Email = 'f_email'
Birthdate = 'f_birthdate'

# Table's fields as defined in Database.InitialQueries.RegistersDB_Creation.py
client_fields = {
    ID: 'ID',
    Name: 'Name',
    Lastname: 'Lastname',
    Adress: 'Adress',
    Location: 'Location',
    Email: 'Email',
    Birthdate: 'Birthdate',
    UserRegistry: __user_registry,
    DateRegistry: __date_registry
}