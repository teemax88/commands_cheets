import socket

from config import LOCALHOST, random_port

my_socket = socket.socket()
address_and_port = (LOCALHOST, random_port())
my_socket.bind(address_and_port)

# https://docs.python.org/3/library/socket.html#socket.socket.listen
# Без дополнительной работы мы можем обрабатывать только одно соединение
# backlog - это размер очереди таких соединений

BACKLOG = 10
my_socket.listen(BACKLOG)

print(my_socket)
