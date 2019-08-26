# ***** Summary *****
# Define all common values to be used in queries
#

#String used to reference DB
db_connection_string = "Registers.db"

#Dictionary with all the tables defined
#If a table is added to the ERD, it must be written here
dic_tables = {
    'trademark': "Trademark", 
    'client': "Client", 
    'product_type': "Product_Type", 
    'product': "Product", 
    'telephone': "Telephone", 
    'client_telephone': "Client_Telephone", 
    'registry': "Registry"
    }