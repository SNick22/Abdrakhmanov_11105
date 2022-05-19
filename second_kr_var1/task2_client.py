import socket


address = 'localhost'
port = 2000

socket = socket.socket()
socket.connect((address, port))

while True:
    a = input()
    socket.send(a.encode('utf-8'))
    if a == '=':
        break
data = socket.recv(1024).decode('utf-8')
print(data)
