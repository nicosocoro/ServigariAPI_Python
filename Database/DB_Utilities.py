# ***** Summary *****
# Define all common values to be used in queries
#

#String used to reference DB
db_connection_string = "Registers.db"

# Constants table
trademark = 'trademark'
client = 'client'
product_type = 'product_type'
product = 'product'
telephone = 'telephone'
client_telephone = 'client_telephone'
registry = 'registry'

#Dictionary with all the tables defined
#If a table is added to the ERD, it must be written here
dic_tables = {
    trademark: "Trademark", 
    client: "Client", 
    product_type: "Product_Type", 
    product: "Product", 
    telephone: "Telephone", 
    client_telephone: "Client_Telephone", 
    registry: "Registry"
    }

# *** General Constats ***
# Audit information

# Keys used to access value information
UserRegistry = 'UserRegistryFieldName'
DateRegistry = 'DateRegistryFieldName'

audit_fields = {
    UserRegistry: 'UserRegistry',
    DateRegistry: 'DateRegistry'
}