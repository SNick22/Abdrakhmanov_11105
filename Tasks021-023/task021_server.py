import socket as Socket

address = 'localhost'
port = 2000


def start_game():
    socket = Socket.socket()
    socket.bind((address, port))
    socket.listen(1)
    conn, addr = socket.accept()
    print(f'{addr} has been connected')
    print('please enter the word')
    while True:
        word = input()
        if word.isalpha():
            break
        else:
            print('the word must contain only letters')
    errors = 0
    output = '_' * len(word)
    conn.sendall(output.encode('utf-8'))
    while True:
        data = conn.recv(1024)
        if not data:
            break
        if not (data.decode('utf-8').isalpha() and len(data.decode('utf-8')) == 1):
            conn.sendall(b'the entered character is not a letter')
            continue
        if data.decode('utf-8') in output:
            conn.sendall(b'this letter has already been entered')
            continue
        if data.decode('utf-8') in word:
            for i, v in enumerate(word):
                if v == data.decode('utf-8'):
                    output = output[:i] + v + output[i+1:]
            if '_' not in output:
                conn.sendall(output.encode('utf-8') + b'\nyou are won!')
                break
            else:
                conn.sendall(output.encode('utf-8'))
        else:
            errors += 1
            if errors == 1:
                conn.sendall(b'|------\n|     |\n|     o\n|\n|\n|')
            if errors == 2:
                conn.sendall(b'|------\n|     |\n|     o\n|     0\n|\n|')
            if errors == 3:
                conn.sendall(b'|------\n|     |\n|     o\n|    /0\n|\n|')
            if errors == 4:
                conn.sendall(b'|------\n|     |\n|     o\n|    /0\\\n|\n|')
            if errors == 5:
                conn.sendall(b'|------\n|     |\n|     o\n|    /0\\\n|    /\n|')
            if errors == 6:
                conn.sendall(b'|------\n|     |\n|     o\n|    /0\\\n|    / \\\n|\nyou lost!')
                break
    conn.close()


if __name__ == '__main__':
    start_game()
