import os
import paramiko

from config import HOST


def key_based_connect(host, file_key):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, key_filename=file_key)
    return client


client = key_based_connect(
    host=HOST,
    file_key=os.path.expanduser("~/.ssh/otus")
)

_stdin, _stdout, _stderr = client.exec_command("df -h")
print(_stdout.read().decode())
client.close()
