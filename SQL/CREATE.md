## CREATE DATABASE
*Cоздать новую базу данных*

В этом синтаксисе:
+ Укажите имя базы данных после ключевых слов CREATE DATABASE. Имя базы данных должно быть уникальным в пределах экземпляра сервера MySQL. Если вы попытаетесь создать базу данных с именем, которое уже существует, MySQL выдаст ошибку.
+ Используйте IF NOT EXISTS опцию условного создания базы данных, если она не существует.
+ Укажите набор символов и параметры сортировки  для новой базы данных. Если вы пропустите предложения CHARACTER SET и COLLATE, MySQL будет использовать набор символов и параметры сортировки по умолчанию для новой базы данных.
```sql
CREATE DATABASE [IF NOT EXISTS] database_name
[CHARACTER SET charset_name]
[COLLATE collation_name]
```

## CREATE TABLE
*Создать новую таблицу в базе данных*

```sql
CREATE TABLE [IF NOT EXISTS] table_name(
   column_1_definition,
   column_2_definition,
   ...,
   table_constraints
) ENGINE=storage_engine;
```

```sql
Следующий оператор создает новую таблицу с именем tasks

CREATE TABLE IF NOT EXISTS tasks (
    task_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    start_date DATE,
    due_date DATE,
    status TINYINT NOT NULL,
    priority TINYINT NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)  ENGINE=INNODB;

created_at столбец TIMESTAMP, который принимает текущее время в качестве значения по умолчанию.
```

## FOREIGN KEY
```sql
Предположим, у каждой задачи есть контрольный список или список дел. Для хранения контрольных списков задач вы можете создать новую таблицу с именем checklists следующим образом

CREATE TABLE IF NOT EXISTS checklists (
    todo_id INT AUTO_INCREMENT,
    task_id INT,
    todo VARCHAR(255) NOT NULL,
    is_completed BOOLEAN NOT NULL DEFAULT FALSE,
    PRIMARY KEY (todo_id , task_id),
    FOREIGN KEY (task_id)
        REFERENCES tasks (task_id)
        ON UPDATE RESTRICT ON DELETE CASCADE
);

task_id столбец внешнего ключа, который ссылается на task_id столбец таблицы tasks. Мы использовали ограничение внешнего ключа, чтобы установить эту связь
```

## AUTO_INCREMENT
``` sql
CREATE TABLE contacts(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(320) NOT NULL
);

В этом примере мы присваиваем атрибут AUTO_INCREMENT столбцу id, чтобы установить его в качестве первичного ключа с автоматическим приращением
```

*AUTO_INCREMENT в существующую таблицу*
```sql
Чтобы добавить AUTO_INCREMENT к существующей таблице, вы используете ALTER TABLE оператор

ALTER TABLE subscribers
ADD id INT AUTO_INCREMENT PRIMARY KEY;
```

## Создание таблицы с выборкой полей из другой таблицы
``` sql
Создание новой таблицы с именем sales, в которой хранятся значения заказов, суммированные по линиям продуктов и годам. Данные поступают из таблиц products, orders и orderDetails
CREATE TABLE sales
SELECT
    productLine,
    YEAR(orderDate) orderYear,
    SUM(quantityOrdered * priceEach) orderValue
FROM
    orderDetails
        INNER JOIN
    orders USING (orderNumber)
        INNER JOIN
    products USING (productCode)
GROUP BY
    productLine ,
    YEAR(orderDate);
```