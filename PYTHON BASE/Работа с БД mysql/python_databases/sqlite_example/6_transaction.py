from sqlite_example.connect import connection
from sqlite_example.config import config

sql_1 = f"INSERT INTO {config.DB_NAME} (name, email, phone) VALUES (?, ?, ?)"
sql_2 = f"UPDATE {config.DB_NAME} SET name = ? WHERE email = ?"
sql_3 = f"DELETE FROM {config.DB_NAME} WHERE name = ?"

name = 'SuperUser'
new_name = 'NEW_USER'
email = 'superemail@email.ru'
address = 'California'

connection.execute(sql_1, (name, email, "989898"))
connection.execute(sql_2, (new_name, email))
connection.commit()
connection.rollback()
connection.execute(sql_3, (name,))
connection.rollback()
connection.commit()
connection.close()
