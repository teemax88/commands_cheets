Файл `pytest.ini` - это конфигурационный файл для библиотеки `pytest`.
Используется для настройки параметров запуска тестов и управления поведением `pytest`

1. **Настройка параметров командной строки по умолчанию**:

   ```ini
   [pytest]
   console_output_style = progress
   ```

   При запуске `pytest` без указания параметра `--console_output_style`, будет использоваться значение `progress`.

2. **Исключение файлов из выполнения тестов**:

   ```ini
   [pytest]
   addopts = --ignore=tests/slow_tests.py
   ```

  `pytest` будет игнорировать файл `slow_tests.py` при запуске тестов.

3. **Установка пользовательских маркеров**:

   ```ini
   [pytest]
   markers =
       smoke: Маркер для тестов, выполняющих быструю проверку
       regression: Маркер для регрессионных тестов
   ```

   Можно использовать маркеры `@pytest.mark.smoke` и `@pytest.mark.regression` в тестах.


4. **Изменение уровня логгирования**:

   ```ini
   [pytest]
   log_cli_level = INFO
   ```

   Это устанавливает уровень логгирования для вывода в консоль при запуске тестов.


5. **Использование фикстур и параметров**:
   НО это чаще делается непосредственно в тестовом коде или в файлах конфигурации `conftest.py`.


## Как брать и использовать данные из pytest.ini

1. **Импортируйте библиотеку `configparser`**:
   ```python
   import configparser
   ```

2. **Создайте объект `configparser` и прочитайте `pytest.ini`**:
   ```python
   config = configparser.ConfigParser()
   config.read('pytest.ini')
   ```

3. **Извлеките значение из `pytest.ini`**:
   ```python
   my_option_value = config.get('pytest', 'myoption')
   ```

4. **Используйте извлеченное значение в тестах**:
   ```python
   import pytest

   @pytest.mark.parametrize("param", [my_option_value])
   def test_example(param):
       assert param == "expected_value"
   ```