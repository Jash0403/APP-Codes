import socket


def convert_to_uppercase(msg):
    return msg.upper()


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 1234)) #sock.bind(('127.0.0.1', 8080)) for windows
sock.listen(1)
conn, addr = sock.accept()
print('Connected by', addr)
while True:
    data = conn.recv(1024)
    if not data:
        break
    upper = convert_to_uppercase(data.decode('utf-8'))
    print('Received data from client:', data.decode('utf-8'))
    conn.sendall(upper.encode('utf-8'))
conn.close()
