import socket as Socket

address = 'localhost'
port = 2000


def start_server():
    socket = Socket.socket()
    socket.bind((address, port))
    socket.listen(1)
    conn, addr = socket.accept()
    print(f'{addr} has been connected')
    shift = int.from_bytes(conn.recv(1024), byteorder='little')
    while True:
        word = conn.recv(1024).decode('utf-8')
        encoded_word = ''
        for letter in word:
            ascii_letter = ord(letter)
            if 97 <= ascii_letter <= 122:
                ascii_letter += shift
                if ascii_letter > 122:
                    while ascii_letter > 122:
                        ascii_letter -= 26
            elif 65 <= ascii_letter <= 90:
                ascii_letter += shift
                if ascii_letter > 90:
                    while ascii_letter > 90:
                        ascii_letter -= 26
            encoded_word += chr(ascii_letter)
        conn.sendall(encoded_word.encode('utf-8'))


if __name__ == '__main__':
    start_server()
