import socket as Socket

address = 'localhost'
port = 2000


class Player:
    def __init__(self, connection):
        self.connection = connection
        self.lives = 3

    def take_lives(self):
        self.lives -= 1

    def isDead(self):
        if self.lives == 0:
            return True
        else:
            return False


def start_game():
    socket = Socket.socket()
    socket.bind((address, port))
    socket.listen(2)
    conn1, addr1 = socket.accept()
    print(f'{addr1} has been connected')
    conn2, addr2 = socket.accept()
    print(f'{addr2} has been connected')
    last_words = []
    game_status = True
    player = Player(conn1)
    another_player = Player(conn2)

    while game_status:
        data_output = player.connection.recv(1024).decode('utf-8')
        if not data_output.isalpha():
            player.connection.sendall(b'please enter a WORD')
            continue
        data = data_output.upper()
        if data in last_words:
            player.connection.sendall(b'this word has already been used, please try again')
            continue
        else:
            if len(last_words) != 0 and last_words[-1][-1] != data[0]:
                player.lives -= 1
                if player.isDead():
                    another_player.connection.sendall(b'you are won!')
                    player.connection.sendall(b'you lost!')
                    game_status = False
                else:
                    message = f'word with the wrong letter. lives left: {player.lives}'
                    player.connection.sendall(message.encode('utf-8'))
                    continue
            else:
                last_words.append(data)
                another_player.connection.sendall(data_output.encode('utf-8'))
                player, another_player = another_player, player


if __name__ == '__main__':
    start_game()
