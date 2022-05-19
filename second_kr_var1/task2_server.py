import socket as Socket


address = 'localhost'
port = 2000


def start_server():
    socket = Socket.socket()
    socket.bind((address, port))
    socket.listen(1)
    conn, addr = socket.accept()
    print(f'{addr} has been connected')
    symbols = []
    while True:
        data = conn.recv(1024).decode('utf-8')
        if data == '=':
            break
        symbols.append(data)
    stack = []
    for i in symbols:
        if i.isdigit():
            stack.append(i)
        elif i in ['+', '-', '*', '/']:
            stack.append(str(eval(stack.pop(-1) + i + stack.pop(-1))))
    conn.sendall(stack[0].encode('utf-8'))


if __name__ == '__main__':
    start_server()
