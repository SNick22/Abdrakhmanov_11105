import socket

address = 'localhost'
port = 2000

socket = socket.socket()
socket.connect((address, port))
print('please enter the shift')
shift = int(input())
socket.send(shift.to_bytes(2, byteorder='little'))
while True:
    print('please enter the word')
    socket.send(input().encode('utf-8'))
    data = socket.recv(1024)
    print(data.decode('utf-8'))
