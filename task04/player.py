import random
from typing import Callable

from task04.board import Board


class Player:
    """Абстрактный класс игрока, реализующий его базовую функцию play(), а также предоставляющий классам-наследникам
    точку расширения в виде виртуального метода _get_cell_to_put_a_mark(), в котором можно реализовать различные
    методы определения очередной клетки для хода"""
    def __init__(self, board: Board, put_mark_func: Callable[[int, int], bool]):
        """Создает экземпляр игрока для игры на доске board. Также принимает функцию, которая обеспечивает
        установку соответствующего знака (крестик или нолик) в заданную клетку игрового поля"""
        self._board = board
        self.__put_mark_func = put_mark_func

    def make_move(self):
        """Инициирует выполнения хода игроком"""
        self.__put_mark_func(*self._get_cell_to_put_a_mark())

    def _get_cell_to_put_a_mark(self) -> tuple[int, int]:
        """Позволяет класса наследникам реализовать различные способы получения координат клетки для очередного хода"""
        raise NotImplementedError


class ConsolePlayer(Player):
    """Класс игрока, обеспечивающий ввод координат клетки для очередного хода из консоли"""
    def _get_cell_to_put_a_mark(self) -> tuple[int, int]:
        while True:
            move = input('Введите координаты клетки для хода в формате "строка, столбец" '
                         '(строки и столбцы нумеруются с 0):')

            try:
                line, column = map(int, move.split(","))
            except:
                print('Не удалось распознать координаты клетки')
                continue

            if not ((0 <= line <= 2) and (0 <= column <= 2)):
                print('Номера строки и столбца не могут быть меньше 0 и больше 2')
                continue

            if not self._board.cell_is_empty(line, column):
                print(f'Клетка {line},{column} уже занята')
                continue

            return line, column


class BotPlayer(Player):
    """Класс игрока-бота, выбирающего клетку для очередного хода случайным образом"""
    def _get_cell_to_put_a_mark(self) -> tuple[int, int]:
        while True:
            line = random.randint(0, 2)
            column = random.randint(0, 2)
            if self._board.cell_is_empty(line, column):
                print(f'Выбрана клетка: {line},{column}')
                return line, column
