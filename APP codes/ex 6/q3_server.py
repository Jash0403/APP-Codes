import socket


def ping_pong(sock):
    while True:
        data = sock.recv(1024)
        if not data:
            break
        if data.decode('utf-8') == 'ping':
            print('Received data from client:', data.decode('utf-8'))
            sock.sendall(b'pong')
        else:
            print('Received data from client:', data.decode('utf-8'))
            sock.sendall(b' ')


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 8888))  # sock.bind(('127.0.0.1', 8080)) for windows
sock.listen(1)
conn, addr = sock.accept()
print('Connected by', addr)
ping_pong(conn)
conn.close()
print('Connection closed')
