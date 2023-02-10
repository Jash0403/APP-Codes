import socket
import os
from _thread import *

ServerSideSocket = socket.socket()
host = ''
port = 2004
ThreadCount = 0
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', 8080))
except socket.error as e:
    print(str(e))
print('Socket is listening..')
ServerSideSocket.listen(5)


def multi_threaded_client(connection):
    connection.send(str.encode('Server is online'))
    while True:
        data = connection.recv(1024)
        response = 'Server message: ' + data.decode('utf-8')
        if not data:
            break
        connection.sendall(str.encode(response))
    connection.close()
# might not work
