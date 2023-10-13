### NOT IN

``` sql
Запрос использует подзапрос для возврата сотрудников, работающих в офисах, расположенных в США
SELECT 
    lastName, firstName
FROM
    employees
WHERE
    officeCode IN (SELECT 
            officeCode
        FROM
            offices
        WHERE
            country = 'USA');

- Подзапрос возвращает все коды офисов , расположенных в США
- Внешний запрос выбирает фамилию и имя сотрудников, работающих в офисах, коды офисов которых находятся в наборе результатов, возвращаемом подзапросом
```

``` sql
Запрос возвращает клиента с самым высоким платежом
SELECT 
    customerNumber, 
    checkNumber, 
    amount
FROM
    payments
WHERE
    amount = (SELECT MAX(amount) FROM payments);
```

``` sql
Найти клиентов, чьи платежи превышают средний платеж, можно с помощью подзапроса
SELECT 
    customerNumber, 
    checkNumber, 
    amount
FROM
    payments
WHERE
    amount > (SELECT 
            AVG(amount)
        FROM
            payments);
```

*Если подзапрос возвращает более одного значения, вы можете использовать в предложении другие операторы, например оператор IN или .NOT IN WHERE*
``` sql
Найти клиентов, которые не разместили заказов
SELECT 
    customerName
FROM
    customers
WHERE
    customerNumber NOT IN (SELECT DISTINCT
            customerNumber
        FROM
            orders);
```

*Когда вы используете подзапрос в FROMпредложении, набор результатов, возвращаемый из подзапроса, используется как временная таблица. Эта таблица называется производной таблицей или материализованным подзапросом.*
``` sql
Подзапрос находит максимальное , минимальное и среднее количество позиций в заказах на продажу
SELECT 
    MAX(items), 
    MIN(items), 
    FLOOR(AVG(items))
FROM
    (SELECT 
        orderNumber, COUNT(orderNumber) AS items
    FROM
        orderdetails
    GROUP BY orderNumber) AS lineitems;
```