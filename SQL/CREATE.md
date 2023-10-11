### HAVING COUNT
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