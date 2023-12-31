from os import get_terminal_size
from json import loads, dumps


host = '127.0.0.1'
port = 8000
close = '<close-connection>'
recv = 1024
msgColor = '\33[100m'
recvColor = '\33[34m'

def jsonExt(data):
    return loads(data)

def jsonBuilder(**data):
    return dumps(data)

def sender(sock, data, encode=True):
    if encode: data = data.encode()
    sock.send(data)
    return data

def receiver(client, recv=2048):
    return client.recv(recv).decode()

def center(string, color=''):
    width = get_terminal_size().columns

    space = width // 2 - len(string) // 2
    return f"{space * ' '}{color}{string}\33[m"
