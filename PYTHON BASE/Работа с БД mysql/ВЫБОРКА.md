Чтобы запросить данные в базе данных MySQL из Python, вам необходимо выполнить следующие шаги:

+ Подключитесь к базе данных MySQL , вы получите MySQLConnectionобъект.
+ Создайте экземпляр  MySQLCursorобъекта из MySQLConnectionобъекта.
+ Используйте курсор для выполнения запроса, вызвав его  execute()метод.
+ Используйте метод или  fetchone()для  получения данных из набора результатов.fetchmany()fetchall()
+ Закройте курсор, а также соединение с базой данных, вызвав  close()метод соответствующего объекта.

## fetchone()
*Метод  fetchone()возвращает следующую строку набора результатов запроса или, Noneесли строк не осталось.*

```python
from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config


def query_with_fetchone():
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books")

        row = cursor.fetchone()

        while row is not None:
            print(row)
            row = cursor.fetchone()

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


if __name__ == '__main__':
    query_with_fetchone()
```

Давайте рассмотрим код подробно:

+ Сначала подключитесь к базе данных, создав новый  MySQLConnectionобъект.
+ Затем создайте экземпляр нового  MySQLCursorобъекта из  MySQLConnectionобъекта
+ Затем выполните запрос, который выбирает все строки из booksтаблицы.
+ После этого извлеките следующую строку в наборе результатов, вызвав метод fetchone(). В  while loopблоке отобразите содержимое строки и перейдите к следующей строке, пока не будут выбраны все строки.
+ Наконец, закройте объекты курсора и соединения, вызвав  close()метод соответствующего объекта.

## fetchall()
*Если количество строк в таблице небольшое, вы можете использовать этот  fetchall()метод для извлечения всех строк из таблицы базы данных.*

```python
from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config


def query_with_fetchall():
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books")
        rows = cursor.fetchall()

        print('Total Row(s):', cursor.rowcount)
        for row in rows:
            print(row)

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


if __name__ == '__main__':
    query_with_fetchall()
```

## fetchmany()
*fetchmany()метод, который возвращает следующее количество строк (n) набора результатов, что позволяет вам сбалансировать время поиска и объем памяти.*

*Сначала разработайте генератор, который разбивает вызовы базы данных на серию  fetchmany()вызовов:*
```python
def iter_row(cursor, size=10):
    while True:
        rows = cursor.fetchmany(size)
        if not rows:
            break
        for row in rows:
            yield row
```
*Во-вторых, используйте  iter_row()генератор для получения 10 строк за раз:*

```python
def query_with_fetchmany():
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM books")

        for row in iter_row(cursor, 10):
            print(row)

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()
```
