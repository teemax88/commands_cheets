import socket

from config import LOCALHOST, random_port

default_socket = socket.socket()
address_and_port = (LOCALHOST, random_port())

# Можем биндить на порты выше 1023
default_socket.bind(address_and_port)

print("Socket 1 binded on", address_and_port)

default_socket.close()
