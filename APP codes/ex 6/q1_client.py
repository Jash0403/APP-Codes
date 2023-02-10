# TCP Socket where server issue a command which will be executed at the client slide
# Client Side
import socket


def print_command(msg):
    print('Executing command print_func...')
    print(msg)


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((''127.0.0.1', 8080', 8080))  # sock.connect(('127.0.0.1', 8080)) for windows
print('Connected to server')
while True:
    data = sock.recv(1024)
    if not data:
        break
    print_command(data.decode('utf-8'))
sock.close()
print('Connection closed')
