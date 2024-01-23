with open("mynewtextfile.txt", "w+") as f:
    f.write(
        "Otus we are learning python\nOtus we are learning python\nOtus we are learning python")  # записывает в файл строку str
    f.seek(12)  # устанавливает текущую позицию в байтах offset для указателя чтения/записи в файле
    print(f.read())  # learning python
    # Вывод:
    # tus we are learning python
    # Otus we are learning python
    # Otus we are learning python

    print("Is readable:", f.readable())  # возвращает значение True, если файл доступен для чтения, Falseесли нет.
    print("Is writeable:", f.writable())  # возвращает значение True, если файл доступен для записи, False если не
    print("File no:", f.fileno())  # File no: 3 --- возвращает целочисленный файловый дескриптор
    print("Is connected to tty-like device:",
          f.isatty())  # возвращает True, если файл подключен/связан с терминальным устройством tty или с tty-подобным устройством, иначе возвратит False
    f.truncate(10)  # усекает размер файла
    f.flush()  # очищает внутренний буфер
    f.seek(0)
    print(f.read())  # Otus we ar

with open("mynewtextfile.txt", mode="r") as file:
    print("Default encoding:", file.encoding)  # Default encoding: cp1251
    file.close()

# change encoding to utf-8
with open("mynewtextfile.txt", mode="r", encoding="utf-8") as file:
    print("New encoding:", file.encoding)  # New encoding: utf-8
    file.close()



# Временные файлы
# from tempfile import TemporaryFile
# f = TemporaryFile("w+t")
# f.write("hello")
# f.seek(0)
# f.read()
# 'hello'
# f.close()  # файл уничтожается
# # либо в контекстном менеджере
# f.write('text2')


# Именованные временные файлы
# from tempfile import NamedTemporaryFile
# f = NamedTemporaryFile("w+t", prefix="myfile", suffix=".txt")
# f.name
# '/tmp/myfile7mxae0fi.txt'

# Временные папки
# from tempfile import TemporaryDirectory
# d = TemporaryDirectory()
# d.name
# '/tmp/tmp5eadqzz5'