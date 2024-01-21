from sqlite_example.config import config
from sqlite_example.connect import connection

cursor = connection.cursor()

sql = f"SELECT * FROM {config.TABLE} WHERE name LIKE ?"

request_result = cursor.execute(sql, ('Vasiliy%',))

# Fetch results as list
# print(request_result.fetchall())
# print(request_result.fetchall())

# # Wont work if data was fetched
# for row in request_result:
#     print(row)

connection.close()
