
*Оператор EXIST Sявляется логическим оператором, который возвращает либо true, либо false. Оператор EXISTSчасто используется для проверки существования строк, возвращаемых подзапросом*
``` sql
Поиск клиента, у которого есть хотя бы один заказ
SELECT 
    customerNumber, 
    customerName
FROM
    customers
WHERE
    EXISTS(
	SELECT 
            1
        FROM
            orders
        WHERE
            orders.customernumber 
		= customers.customernumber);
```

``` sql
Поиск клиентов, у которых нет заказов
SELECT 
    customerNumber, 
    customerName
FROM
    customers
WHERE
    NOT EXISTS( 
	SELECT 
            1
        FROM
            orders
        WHERE
            orders.customernumber = customers.customernumber
	);
```