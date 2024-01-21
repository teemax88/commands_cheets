with open("mynewtextfile.txt", "w+") as f:
    f.write("Otus we are learning python\nOtus we are learning python\nOtus we are learning python")
    f.seek(0)
    print(f.read())
    # Вывод:
    # Otus we are learning python
    # Otus we are learning python
    # Otus we are learning python

    print("Is readable:", f.readable())  # Is readable: True
    print("Is writeable:", f.writable())  # Is writeable: True
    print("File no:", f.fileno())  # File no: 3
    print("Is connected to tty-like device:", f.isatty())  # Is connected to tty-like device: False
    f.truncate(5)
    f.flush()
    f.seek(0)
    print(f.read())  # Otus
f.close()
