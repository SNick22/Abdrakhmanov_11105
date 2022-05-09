import socket

socket = socket.socket()
address = 'localhost'
port = 2000
socket.connect((address, port))
while True:
    data = socket.recv(1024)
    print(data.decode('utf-8'))
    if 'you are won!' in data.decode('utf-8') or 'you lost!' in data.decode('utf-8'):
        break
    print('please enter the letter')
    socket.send(input().encode('utf-8'))
