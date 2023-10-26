Чтобы обновить данные в таблице MySQL в Python, выполните следующие действия:

+ Подключитесь к базе данных , создав новый MySQLConnectionобъект.
+ Создайте новый MySQLCursorобъект из MySQLConnectionобъекта и вызовите execute()метод объекта MySQLCursor. Чтобы принять изменения, вы вызываете commit()метод объекта MySQLConnectionпосле вызова execute()метода. В противном случае в базу данных не будет внесено никаких изменений.
+ Закройте курсор и соединение с базой данных.

*В следующем примере обновляется название книги, указанное идентификатором книги:*

```python
from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config


def update_book(book_id, title):
    # read database configuration
    db_config = read_db_config()

    # prepare query and data
    query = """ UPDATE books
                SET title = %s
                WHERE id = %s """

    data = (title, book_id)

    try:
        conn = MySQLConnection(**db_config)

        # update book title
        cursor = conn.cursor()
        cursor.execute(query, data)

        # accept the changes
        conn.commit()

    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()


if __name__ == '__main__':
    update_book(37, 'The Giant on the Hill *** TEST ***')
```
*Важно понимать, что мы всегда должны использовать заполнители ( %s) внутри любых операторов SQL, которые содержат вводимые пользователем данные. Это помогает нам предотвратить SQL-инъекцию.*


