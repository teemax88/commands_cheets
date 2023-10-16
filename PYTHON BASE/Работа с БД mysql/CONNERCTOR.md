*Команда pip позволяет установить соединитель MySQL Python в любой операционной системе*
```python
pip install mysql-connector-python
```

*После установки соединителя MySQL Python вам необходимо протестировать его, чтобы убедиться, что он работает правильно и что вы можете без проблем подключиться к серверу базы данных MySQL*
```python
>>> import mysql.connector
>>> mysql.connector.connect(host='localhost',database='mysql',user='root',password='your pass')

Если вы видите следующий вывод, это означает, что вы успешно установили MySQL Connector/Python в своей системе.

<mysql.connector.connection.MySQLConnection object at 0x0187AE50>
```


*Сначала загрузите следующую базу данных, распакуйте файл и скопируйте его в папку, например C:\mysql\python_mysql.sql*

*Затем войдите на сервер MySQL с помощью mysqlинструмента*
```python
mysql -u root -p
```

Затем создайте овую БД, выберите ее и загрузите данные:
```python
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
Давайте рассмотрим этот модуль подробно:

+ Сначала импортируйте  объекты mysql.connectorи Errorиз пакета MySQL Connector/Python.
+ Используйте connect()функцию для подключения к серверу MySQL. Функция connect()принимает четыре параметра: хост, базу данных, пользователя и пароль. Функция  connect()устанавливает соединение с  python_mysqlбазой данных и возвращает MySQLConnectionобъект.
+ Проверьте, успешно ли установлено соединение с базой данных MySQL, используя  is_connected()метод. В случае возникновения исключения, например, когда сервер MySQL недоступен, база данных не существует или неверное имя пользователя или пароль, Python вызовет исключение. Блок  try exceptобрабатывает исключение и отображает ошибку.
+ Закройте соединение с базой данных, используя  close()метод объекта  MySQLConnection.

*Чтобы протестировать  connect.pyмодуль, вы используете следующую команду:*
```python
>python connect.py
Connected to MySQL database
```
## Подключение с помощью config файла
*Сначала создайте файл конфигурации базы данных с именем  config.iniи определите раздел с четырьмя параметрами следующим образом:*
```python
[mysql]
host = localhost
database = python_mysql
user = root
password =SecurePass1!
```

*создайте новый модуль с именем  python_mysql_dbconfig.py, который считывает конфигурацию базы данных из  config.iniфайла и возвращает объект словаря:*
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

*создайте новый модуль connect2.py  , который использует MySQLConnectionобъект для подключения к python_mysqlбазе данных.*
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

Рассмотрим модуль более подробно:

+ Сначала импортируйте необходимые объекты, включая MySQLConnection, Errorиз пакета MySQL Connector/Python и  read_db_configиз  python_mysql_dbconfigмодуля.
+ Прочитайте конфигурацию базы данных и передайте ее, чтобы создать новый экземпляр MySQLConnectionобъекта в connect()функции. Остальная часть кода работает аналогично первому примеру.