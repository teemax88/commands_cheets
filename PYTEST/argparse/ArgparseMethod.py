import argparse
import subprocess

# Создание парсера
parser = argparse.ArgumentParser()

"""
    Все параметры для add_argument
    
    name or flags - Either a name or a list of option strings, e.g. foo or -f, --foo.
    action - The basic type of action to be taken when this argument is encountered at the command line.
    nargs - The number of command-line arguments that should be consumed.
    const - A constant value required by some action and nargs selections.
    default - The value produced if the argument is absent from the command line.
    type - The type to which the command-line argument should be converted.
    choices - A container of the allowable values for the argument.
    required - Whether or not the command-line option may be omitted (optionals only).
    help - A brief description of what the argument does.
    metavar - A name for the argument in usage messages.
    dest - The name of the attribute to be added to the object returned by parse_args().

"""

# Добавление аргументов
parser.add_argument('--method', '-m',
                    action='store',
                    help='Method to make request',
                    default='GET')

parser.add_argument('--url', '-u',
                    action='store',
                    help='Url to make request to',
                    required=True)

# Если параметр передан то Ture, иначе False
parser.add_argument('--true', '-t',
                    action='store_true',
                    help='True or false param',
                    required=False)

# Добавляение значений в список по параметру
# python3 ArgparseMethod.py --url=ya.ru -s
parser.add_argument('--save', '-s',
                    action='append_const',
                    const='const_to_save',
                    dest='const_collection',
                    default=[],
                    help='Store params in list',
                    required=False)

# Добавляение значений в список по параметру
# python3 ArgparseMethod.py --url=ya.ru -s -s2
parser.add_argument('--save2', '-s2',
                    action='append_const',
                    const='const_to_save2',
                    dest='const_collection',
                    default=[],
                    help='Store params in list',
                    required=False)

# Парсим всё что положили
args = parser.parse_args()

# Это словарь из которого аргументы можно доставать
print(args)

"""////////////////////////////////////////////////////////////////////////////////////////////////////////////////"""


def ping_ip(ip_address, count):
    # благодаря argparse, доступен help
    """
    Ping IP address and return tuple:
    On success: (return code = 0, command output)
    On failure: (return code, error output (stderr))
    """
    reply = subprocess.run(
        f"ping -c {count} -n {ip_address}",
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding="utf-8",
    )
    if reply.returncode == 0:
        return True, reply.stdout
    else:
        return False, reply.stdout + reply.stderr


parser = argparse.ArgumentParser(description="Ping script")

# аргумент, который передается после опции -a, сохранится в переменную ip
# можно указать, что аргумент является обязательным. Для этого надо изменить опцию -a: добавить в конце required=True
parser.add_argument("-a", dest="ip", required=True)

# аргумент, который передается после опции -c, будет сохранен в переменную count, но прежде будет конвертирован в число.
# Если аргумент не был указан, по умолчанию будет значение 2
parser.add_argument("-c", dest="count", default=2, type=int)

args = parser.parse_args()
print(args)

rc, message = ping_ip(args.ip, args.count)
print(message)

# Вызов
# python ping_function.py -a 8.8.8.8 -c 5
