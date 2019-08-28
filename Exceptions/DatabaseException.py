import Exceptions.Constants as cons

class ConnectionDB_Exception(Exception):
        def __init__(self):
            msg = cons.err_database_connection
            super().__init__(msg)