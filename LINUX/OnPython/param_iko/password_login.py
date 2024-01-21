import paramiko
# Update the next three lines with your
from config import HOST, USERNAME, PASSWORD


client = paramiko.client.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(HOST, username=USERNAME, password=PASSWORD)
_, _stdout, _ = client.exec_command("df -h")
print(_stdout.read().decode())

# Create authorized_keys file
# with open(os.path.expanduser("~/.ssh/otus.pub")) as f:
#     _, _stdout, _ = client.exec_command(f"echo '{f.read()}' > ~/.ssh/authorized_keys")

# Stop ssh
# _stdin, _stdout, _stderr = client.exec_command("sudo -S systemctl stop ssh")
# _stdin.write(f'{PASSWORD}\n')
# _stdin.flush()
# print(_stdout.read().decode())
# print(_stderr.read().decode())

client.close()
