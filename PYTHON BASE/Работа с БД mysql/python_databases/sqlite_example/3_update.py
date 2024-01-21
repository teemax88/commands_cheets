from sqlite_example.config import config
from sqlite_example.connect import connection

cursor = connection.cursor()

# Bad example because hardcoded data!!!
sql = f"UPDATE {config.TABLE} SET email = '????' WHERE name = ? LIMIT 2"

cursor.execute(sql, ("Vasiliy2",))
connection.commit()

sql = f"UPDATE {config.TABLE} SET name = ? WHERE name = ?"
data = ("HELLOTEST", "Vasiliy")

cursor.execute(sql, data)
connection.commit()

connection.close()
