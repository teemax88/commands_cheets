
```python
pip install mysql-connector-python
```

```python
import mysql.connector
mysql.connector.connect(host='localhost',database='mysql',user='root',password='your pass')

# Сообщение об успешной установке
<mysql.connector.connection.MySQLConnection object at 0x0187AE50>
```

*Сначала загрузите следующую базу данных, распакуйте файл и скопируйте его в папку, например C:\mysql\python_mysql.sql*

```python
# Затем войдите на сервер MySQL
mysql -u root -p
```

```python
# Затем создайте новую БД, выберите ее и загрузите данные:
mysql>create database python_mysql;

mysql>use python_mysql;

mysql> source c:\mysql\python_mysql.sql

mysql> SHOW TABLES;
```


## Подключение к БД
```python
import mysql.connector
from mysql.connector import Error


def connect():
    """ Connect to MySQL database """
    conn = None
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='python_mysql',
                                       user='root',
                                       password='SecurePass1!')
        if conn.is_connected():
            print('Connected to MySQL database')

    except Error as e:
        print(e)

    finally:
        if conn is not None and conn.is_connected():
            conn.close()


if __name__ == '__main__':
    connect()
```

```python
# Чтобы протестировать  connect.py модуль используете команду:
python connect.py

Connected to MySQL database
```

## Подключение с помощью config файла
*Создайте файл конфигурации базы данных config.ini и определите раздел с четырьмя параметрами:*
```python
[mysql]
host = localhost
database = python_mysql
user = root
password = SecurePass1!
```

*создайте новый модуль python_mysql_dbconfig.py, который считывает конфигурацию базы данных из  config.ini файла и возвращает объект словаря:*
```python
from configparser import ConfigParser


def read_db_config(filename='config.ini', section='mysql'):
    """ Read database configuration file and return a dictionary object
    :param filename: name of the configuration file
    :param section: section of database configuration
    :return: a dictionary of database parameters
    """
    # create parser and read ini configuration file
    parser = ConfigParser()
    parser.read(filename)

    # get section, default to mysql
    db = {}
    if parser.has_section(section):
        items = parser.items(section)
        for item in items:
            db[item[0]] = item[1]
    else:
        raise Exception('{0} not found in the {1} file'.format(section, filename))

    return db
```

*Создайте connect2.py, который использует MySQLConnection объект для подключения к python_mysql базе данных.*
```python
from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config

def connect():
    """ Connect to MySQL database """

    db_config = read_db_config()
    conn = None
    try:
        print('Connecting to MySQL database...')
        conn = MySQLConnection(**db_config)

        if conn.is_connected():
            print('Connection established.')
        else:
            print('Connection failed.')

    except Error as error:
        print(error)

    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print('Connection closed.')

if __name__ == '__main__':
    connect()
```