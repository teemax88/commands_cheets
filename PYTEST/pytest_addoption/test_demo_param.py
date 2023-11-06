def test_answer(url_param):
    """ При запуске теста в url по умолчанию стоит значение https://ya.ru
     Чтобы поменять URL, нужно в терминале при запуске явно задать этот параметр
     т.е pytest pytest_addoption -s --url="google.com"
     Важно! Кавычки имеют значение (одинарные или двойные)"""
    if url_param == "ya.ru":
        print("YAAAAANDEX")
    elif url_param == "google.com":
        print("GOOOGLE!")
    else:
        print("DuckDuckGOOOOO")
