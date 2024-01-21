from sqlite_example.connect import connection

cursor = connection.cursor()

with open("table.sql", "r") as script:
    cursor.execute(script.read())

sql = f"INSERT INTO contacts4 (name, email, phone, address) VALUES (?, ?, ?, ?)"
data = ("One", "Two", "Three", "Four")

# https://docs.python.org/3.7/library/sqlite3.html
with connection:
    cursor.execute(sql, data)

connection.close()
