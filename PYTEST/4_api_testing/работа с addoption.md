Опции командной строки `--addoption` позволяет добавить собственные параметры командной строки для тестов

1. **Создание**:
   Для использования `--addoption` создайте файл, например, `myplugin.py`

   ```python
   import pytest

   def pytest_addoption(parser):
       parser.addoption("--myoption", action="store", default="default_value", help="Описание вашей опции")
   ```

   Параметр `default` устанавливает значение по умолчанию для этой опции, а `help` предоставляет описание опции.


2. **Использование опции**:
   В тестах опцию можно получить с помощью объекта `config`

   ```python
   import pytest

   def test_example(request):
       my_option_value = request.config.getoption("--myoption")
       assert my_option_value == "expected_value"
   ```

   Получаем значение опции `--myoption` с помощью `request.config.getoption("--myoption")` и затем
   выполняем проверку на ожидаемое значение.


3. **Запуск тестов**:
   Используйте команду `pytest` и передайте ей опцию, указывая ее имя и значение.

   ```bash
   pytest --myoption=expected_value
   ```

   Запускаем тесты с опцией `--myoption` и устанавливаем ее значение равным `expected_value`.