# TCP Socket where server issue a command which will be executed at the client slide
# Server Side
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1',8080) #sock.bind(('127.0.0.1', 8080)) for windows
sock.listen(1)
conn, addr = sock.accept()
print('Connected by', addr)
while True:
    data = input('> ')
    if not data:
        break
    print('Sending data to client...')
    conn.sendall(data.encode('utf-8'))
conn.close()
