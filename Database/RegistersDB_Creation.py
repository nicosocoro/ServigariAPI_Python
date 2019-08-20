import sqlite3

conn = sqlite3.connect('Registers.db')

c = conn.cursor()

c.executescript("""CREATE TABLE Client (
                ID INTEGER PRIMARY KEY,
                Name TEXT,
                LastName TEXT NOT NULL,
                Adress TEXT NOT NULL,
                Location TEXT NOT NULL,
                Birthdate INTEGER,
                UserRegistry TEXT NOT NULL,
                DateRegistry INTEGER NOT NULL
            );
            
            CREATE TABLE Client_Telephone (
                ID INTEGER PRIMARY KEY,
                ID_Client INTEGER,
                FOREIGN KEY (ID_Client) REFERENCES Client(ID)
            );

            CREATE TABLE Telephone (
                ID INTEGER PRIMARY KEY,
                Number INTEGER NOT NULL,
                Description TEXT,
                UserRegistry TEXT NOT NULL,
                DateRegistry INTEGER NOT NULL
            );

            CREATE TABLE Trademark (
                ID INTEGER PRIMARY KEY,
                Description TEXT NOT NULL,
                UserRegistry TEXT NOT NULL,
                DateRegistry INTEGER NOT NULL                
            );

            CREATE TABLE Product (
                ID INTEGER PRIMARY KEY,
                Comments TEXT NOT NULL,
                UserRegistry TEXT NOT NULL,
                DateRegistry INTEGER NOT NULL,
                ID_Product_Type INTEGER,
                ID_Trademark INTEGER,
                FOREIGN KEY (ID_Product_Type) REFERENCES Product_Type(ID)
                FOREIGN KEY (ID_Trademark) REFERENCES Trademark(ID)
            );

            CREATE TABLE Product_Type (
                ID INTEGER PRIMARY KEY,
                Description TEXT NOT NULL,
                UserRegistry TEXT NOT NULL,
                DateRegistry INTEGER NOT NULL
            );

            CREATE TABLE Registry (
                ID INTEGER PRIMARY KEY,
                Description TEXT,
                Amount REAL NOT NULL,
                UserRegistry TEXT NOT NULL,
                DateRegistry INTEGER NOT NULL,
                ID_Client INTEGER,
                ID_Product INTEGER,
                FOREIGN KEY (ID_Client) REFERENCES Client(ID),
                FOREIGN KEY (ID_Product) REFERENCES Product(ID)
            );
         """)

conn.commit()

conn.close()