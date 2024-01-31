1. **Создание**:
   ```python
   import pytest

   def pytest_addoption(parser):
       parser.addoption("--myoption", action="store", default="default_value", help="Описание вашей опции")
   ```

2. **Использование опции**:
   ```python
   import pytest

   def test_example(request):
       my_option_value = request.config.getoption("--myoption")
       assert my_option_value == "expected_value"
   ```

3. **Запуск тестов**:
   ```bash
   pytest --myoption=expected_value
   ```