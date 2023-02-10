import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('', 8888)) #sock.connect(('127.0.0.1', 8080)) for windows
print('Connected to server')
while True:
    data = input('> ')
    if not data:
        break
    print('Sending data to server...')
    sock.sendall(data.encode('utf-8'))
    data = sock.recv(1024)
    print('Received data from server:', data.decode('utf-8'))
sock.close()
print('Connection closed')
