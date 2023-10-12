from task04.board import Board
from task04.player import BotPlayer, ConsolePlayer


class Game:
    """Класс игры в крестики-нолики. Обеспечивает создание поля, двух игроков и возможность запуска игры"""
    def __init__(self, x_player_is_bot: bool = False, o_player_is_bot: bool = True):
        """Создает игру с двумя игроками-ботами или реальными игроками, в зависимости от переданных параметров"""
        self.__board = Board()

        self.__x_player = BotPlayer(self.__board, self.__board.put_x) if x_player_is_bot \
            else ConsolePlayer(self.__board, self.__board.put_x)

        self.__o_player = BotPlayer(self.__board, self.__board.put_o) if o_player_is_bot \
            else ConsolePlayer(self.__board, self.__board.put_o)

    def play(self):
        """Запускает игру"""
        x_plays = True
        print('---------Добро пожаловать в игру крестики-нолики----------------')

        while not self.__board.game_over():
            print('Текущее состояние поля: ')
            print(self.__board)
            print(f'Играет игрок {"X" if x_plays else "O"}')

            if x_plays:
                self.__x_player.make_move()
            else:
                self.__o_player.make_move()
            x_plays = not x_plays
            print(" ")
        if self.__board.has_winner():
            print(f'Игра окончена, победил игрок {self.__board.winner().upper()} ')
        else:
            print('Игра окончена, т.к. на поле не осталось пустых клеток. Победила дружба')
        print(self.__board)