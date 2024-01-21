import socket
import sys

from config import LOCALHOST

# Define this target port
my_socket = socket.socket()
address_and_port = (LOCALHOST, int(sys.argv[1]))

my_socket.connect(address_and_port)

# https://docs.python.org/3/library/socket.html#socket.socket.send
data_amount = my_socket.send(b"Hello, socket!")
print("Send", data_amount, "bytes")

my_socket.close()
