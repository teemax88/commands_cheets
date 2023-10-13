
*Оператор INSERT позволяет вставить в таблицу одну или несколько строк*
``` sql
INSERT INTO table(c1,c2,...)
VALUES (v1,v2,...);
```

``` sql
Для вставки нескольких строк в таблицу

INSERT INTO table(c1,c2,...)
VALUES 
   (v11,v12,...),
   (v21,v22,...),
    ...
   (vnn,vn2,...);
```

``` sql
Оператор вставляет в tasksтаблицу новую строку

INSERT INTO tasks(title,priority)
VALUES('Learn MySQL INSERT Statement',1);
```

*Если вы хотите вставить в столбец значение по умолчанию, у вас есть два способа:*
+ Игнорируйте имя и значение столбца в INSERTинструкции.
+ Укажите имя столбца в INSERT INTOпредложении и используйте DEFAULTключевое слово в VALUESпредложении.

``` sql
В этом примере мы указали priority столбец и DEFAULT ключевое слово. Поскольку значение по умолчанию для столбца priority равно 3, то MySQL использует номер 3 для вставки в priority столбец

INSERT INTO tasks(title,priority)
VALUES('Understanding DEFAULT keyword in INSERT statement',DEFAULT);
```

## INSERT INTO SELECT
``` sql
INSERT INTO table_name(column_list)
SELECT 
   select_list 
FROM 
   another_table
WHERE
   condition;
```

``` sql
Используйте оператор, чтобы вставить в таблицу INSERT INTO SELECT клиентов, которые находятся в таблице:California USA customers suppliers
INSERT INTO suppliers (
    supplierName, 
    phone, 
    addressLine1,
    addressLine2,
    city,
    state,
    postalCode,
    country,
    customerNumber
)
SELECT 
    customerName,
    phone,
    addressLine1,
    addressLine2,
    city,
    state ,
    postalCode,
    country,
    customerNumber
FROM 
    customers
WHERE 
    country = 'USA' AND 
    state = 'CA';
```

``` sql
Используйте INSERTоператор для вставки значений, полученных из SELECTоператоров
INSERT INTO stats(totalProduct, totalCustomer, totalOrder)
VALUES(
	(SELECT COUNT(*) FROM products),
	(SELECT COUNT(*) FROM customers),
	(SELECT COUNT(*) FROM orders)
);
```
