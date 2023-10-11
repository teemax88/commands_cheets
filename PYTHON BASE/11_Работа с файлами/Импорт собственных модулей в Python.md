```python
# импорт из imp_st_library.py
# Для импортирования модулей применяются инструкции import и import from.
# Собственные модули импортируются как и стандартные модули python.
# Всего то надо написать инструкцию import и указать название модуля(программы)

# import imp_st_library  # импорт всего модуля(программы) если они находятся в 1-й папке
# # после импорта Python сделает всё что было в модуле (вывод End programm)
# # ,но только один раз (даже если импорт будет несколько раз)
# import importlib  # запомнит первоначальное значение модуля и если мы его меняем ,то в 14.15 строке вызовем старые знач.
#
# print(imp_st_library.my_num1)
# imp_st_library.my_num1 = 7  # изменили значение переменной внутри модуля
# print(imp_st_library.my_num1)  # вывод End programm  2  7
# importlib.reload(import_st_library)
# print(imp_st_library.my_num1)  # вывод End programm  2  7 End programm  2

# print(imp_st_library.factor(5)) # импорт определённой функции из модуля
# print(imp_st_library.pi) # 3.141592653589793

# # или так
# from imp_st_library import summa, factor, my_num1 # импорт конкретных переменных
# print(factor(5)) # 120
# print(summa(12, 4, 56)) # 72

# если модуль который нужно импортировать находится в другой папке то нужно её указать
# import Задачи.FizzBuzz # импорт из дугой папки (название должно быть без точек и цифр)

print(__name__)  # End programm  __main__ (вывод всего модуля и __main__). Если поставить
# if __name__ == '__main__':  в import_st_library
# то программа будет запускаться только если мы её запускаем а не с импортом
print(__name__)  # __main__

```