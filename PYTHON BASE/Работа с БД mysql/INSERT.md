Чтобы вставить новые строки в таблицу MySQL, выполните следующие действия:

+ Подключитесь к серверу базы данных MySQL , создав новый MySQLConnectionобъект.
+ Инициировать MySQLCursorобъект из MySQLConnectionобъекта.
+ Выполните INSERTоператор, чтобы вставить данные в таблицу.
+ Закройте соединение с базой данных.

*Следующий метод вставляет в  booksтаблицу новую книгу*
```python
from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config

def insert_book(title, isbn):
    query = "INSERT INTO books(title,isbn) " \
            "VALUES(%s,%s)"
    args = (title, isbn)

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        if cursor.lastrowid:
            print('last insert id', cursor.lastrowid)
        else:
            print('last insert id not found')

        conn.commit()
    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()

def main():
   insert_book('A Sudden Light','9781439187036')

if __name__ == '__main__':
    main()
```

В приведенном выше коде:

+ Сначала импортируйте MySQLConnectionобъекты Errorиз пакета MySQL Connector/Python и read_db_config()функции из модуля python_mysql_dbconfig .
+ Затем определите новую функцию с именем insert_book(), которая принимает два аргумента: заголовок и ISBN. Внутри insert_book()функции создайте INSERTоператор ( query) и данные ( args) для вставки в booksтаблицу. Обратите внимание, что данные, передаваемые в функцию, представляют собой кортеж.
+ Затем создайте новое соединение, выполните оператор и зафиксируйте изменение в блоке try except. Обратите внимание, что вам необходимо явно вызвать  commit()метод, чтобы внести изменения в базу данных. В случае успешной вставки новой строки вы можете получить идентификатор последней вставки столбца AUTO_INCREMENT , используя  lastrowidсвойство объекта MySQLCursor.
+ После этого закройте курсор и соединение с базой данных в конце функции  insert_book().
+ Наконец, вызовите  insert_book()функцию, чтобы вставить новую строку в  booksтаблицу  main()функции.


*Следующий INSERT оператор позволяет вставить в таблицу несколько строкbooks*
```python
INSERT INTO books(title,isbn)
VALUES('Harry Potter And The Order Of The Phoenix', '9780439358071'),
       ('Gone with the Wind', '9780446675536'),
       ('Pride and Prejudice (Modern Library Classics)', '9780679783268');
```

*Чтобы вставить несколько строк в таблицу в Python, вы используете  executemany()метод объекта MySQLCursor*
```python
from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config

def insert_books(books):
    query = "INSERT INTO books(title,isbn) " \
            "VALUES(%s,%s)"

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.executemany(query, books)

        conn.commit()
    except Error as e:
        print('Error:', e)

    finally:
        cursor.close()
        conn.close()

def main():
    books = [('Harry Potter And The Order Of The Phoenix', '9780439358071'),
             ('Gone with the Wind', '9780446675536'),
             ('Pride and Prejudice (Modern Library Classics)', '9780679783268')]
    insert_books(books)

if __name__ == '__main__':
    main()
```