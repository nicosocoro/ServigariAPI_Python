import sqlite3

conn = sqlite3.connect('Registers.db')
c = conn.cursor()

# c.executescript("DELETE FROM Client; DELETE FROM Telephone;")

c.execute("SELECT * FROM Client")
print(c.fetchall())

c.execute("SELECT * FROM Telephone")
print(c.fetchall())



conn.commit()
conn.close()