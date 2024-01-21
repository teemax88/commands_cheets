import os
import paramiko

from config import HOST, PASSWORD

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(HOST, key_filename=os.path.expanduser("~/.ssh/otus"))

sftp = client.open_sftp()
sftp.put("config.yml", "config_with_empty_line.yml")


def put_file_to(local_file_path, remote_file_path, client):
    """Функция позволяет загрузить файл в любое место УМ.

    https://www.dmosk.ru/miniinstruktions.php?mini=ubuntu-ssh-root
    """
    sftp = client.open_sftp()
    sftp.put(local_file_path, "tmp")
    _stdin, _stdout, _stderr = client.exec_command(f"sudo -S mv tmp {remote_file_path}")
    _stdin.write(f'{PASSWORD}\n')
    _stdin.flush()

# put_file_to(local_file_path="config.yml", remote_file_path="/test_config.yml", client=client)

client.close()
