*Следующий метод вставляет в books таблицу новую книгу*
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

*Следующий INSERT оператор позволяет вставить в таблицу несколько строк books*
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