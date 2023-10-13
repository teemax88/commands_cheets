### NOT IN
*Оператор UPDATE обновляет данные в таблице*
``` sql
UPDATE [LOW_PRIORITY] [IGNORE] table_name 
SET 
    column_name1 = expr1,
    column_name2 = expr2,
    ...
[WHERE
    condition];
    
Модификатор LOW_PRIORITY указывает UPDATE оператору задержать обновление до тех пор, пока не будет установлено соединение для чтения данных из таблицы. Это LOW_PRIORITY вступает в силу для механизмов хранения , которые используют блокировку только на уровне таблицы, таких как MyISAM, MERGE и MEMORY.
Модификатор IGNORE позволяет UPDATE оператору продолжать обновление строк даже в случае возникновения ошибок. Строки, вызывающие ошибки, например конфликты дубликатов ключей, не обновляются.
```

```sql
Обновите адрес электронной почты Mary на новый адрес

UPDATE employees 
SET 
    email = 'mary.patterson@classicmodelcars.com'
WHERE
    employeeNumber = 1056;
```

```sql
Обновляет столбцы фамилии и электронной почты сотрудника с номером 1056

UPDATE employees 
SET 
    lastname = 'Hill',
    email = 'mary.hill@classicmodelcars.com'
WHERE
    employeeNumber = 1056;
```

```sql
В следующем примере обновляются доменные части всех электронных писем Sales Reps с кодом Office 6

UPDATE employees
SET email = REPLACE(email,'@classicmodelcars.com','@mysqltutorial.org')
WHERE
   jobTitle = 'Sales Rep' AND
   officeCode = 6;
```