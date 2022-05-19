import socket

address = 'localhost'
port = 2000

socket = socket.socket()
socket.connect((address, port))

data = socket.recv(1024).decode('utf-8')
while data != 'you are won!' or data != 'you lost!':
    print(data)
    socket.send(input().encode('utf-8'))
    data = socket.recv(1024).decode('utf-8')
    if data == 'you are won!' or data == 'you lost!':
        print(data)
        break
