import os
import paramiko

from config import HOST, USERNAME

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(HOST, key_filename=os.path.expanduser("~/.ssh/otus"))

sftp = ssh.open_sftp()
sftp.get(f"/home/{USERNAME}/file.py", "downloaded.py")

# stin, stout, ster = ssh.exec_command("touch file.py")
# stin, stout, ster = ssh.exec_command("ls -la")
# print(stout.read().decode("utf-8"))

ssh.close()
