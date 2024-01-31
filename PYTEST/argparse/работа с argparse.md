1. **Импорт библиотек**:
   ```python
   import argparse
   import pytest
   ```

2. **Создание парсера аргументов**:
   ```python
   parser = argparse.ArgumentParser(description="Описание вашего тестового скрипта")
   parser.add_argument("--myoption", type=str, default="default_value", help="Описание вашей опции")
   ```

3. **Получение значений аргументов**:
   ```python
   args = parser.parse_args()
   my_option_value = args.myoption
   ```

4. **Использование значений аргументов в тестах**:
   ```python
   import pytest

   @pytest.mark.parametrize("param", [my_option_value])
   def test_example(param):
       assert param == "expected_value"
   ```

5. **Запуск тестов с аргументами**:
   ```bash
   pytest --myoption=expected_value
   ```