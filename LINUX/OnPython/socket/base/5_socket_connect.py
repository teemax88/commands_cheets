import socket
import sys

from config import LOCALHOST

my_socket = socket.socket()

address_and_port = (LOCALHOST, int(sys.argv[1]))

# https://docs.python.org/3/library/socket.html#socket.socket.connect
my_socket.connect(address_and_port)
my_socket.close()
