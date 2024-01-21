from sqlite_example.config import config
from sqlite_example.connect import connection

cursor = connection.cursor()

# Delete table
# cursor.execute("DROP TABLE contacts2")
# cursor.execute(f"DROP TABLE IF EXISTS contacts2")

sql = f"DELETE FROM {config.TABLE} WHERE name = ?"
cursor.executemany(sql, ([
    ("Vasiliy1",),
    ("Vasiliy3",),
]))

connection.commit()

connection.close()
