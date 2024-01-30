## DELETE
``` sql
DELETE FROM table_name
WHERE condition;
```

```sql
удалить сотрудников, у которых значение officeNumberравно 4

DELETE FROM employees 
WHERE officeCode = 4;
```

```sql
следующий оператор сортирует клиентов по именам в алфавитном порядке и удаляет первые 10 клиентов
DELETE FROM customers
ORDER BY customerName
LIMIT 10;

Обратите внимание, что порядок строк в таблице не указан, поэтому при использовании этого LIMIT предложения вы всегда должны использовать это ORDER BY предложение.
```