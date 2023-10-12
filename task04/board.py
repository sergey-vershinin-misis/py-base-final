import numpy as np


class Board:
    """Класс игрового поля в игре крестики-нолики. Обеспечивает возможность устанавливать в клетках крестики и нолики,
    а также определяет наличие свободных ячеек, победителя и факта окончания игры

    Для реализации игрового поля используется 2d-массив из библиотеки NumPy. Это позволяет компактно находить строки,
    столбцы и диагонали игрового поля и по ним определять факт победы того или иного игрока.

    В качестве отметок X и O на игровом поле используются числа 1 и -1. Это позволяет определять наличие трех крестиков
    или ноликов в строке, столбце или диагонали простым суммированием: сумма будет равна 3 только в случае, если есть
    три 1, а -3 - если есть три -1. Во всех остальных случаях сумма трех клеток не будет ровна ни 3, ни -3"""
    def __init__(self):
        """Создает новое игровое поле """
        self.__space = np.zeros((3, 3))

    def __get_space_sums(self):
        """Считает суммы элементов игрового поля по всем строкам, столбцам и диагоналям матрицы 3х3"""
        return ([sum(self.__space[i, :]) for i in range(3)]
                + [sum(self.__space[:, i]) for i in range(3)]
                + [sum(self.__space.diagonal())]
                + [sum(np.fliplr(self.__space).diagonal())])

    def __put_sign(self, line, column, sign):
        if self.__space[line, column] == 0:
            self.__space[line, column] = sign
            return True
        else:
            return False

    def __repr__(self):
        def represent_cell_state(cell_value):
            if cell_value == 1:
                return 'x'
            elif cell_value == -1:
                return 'o'
            else:
                return '_'

        result = []
        for line in range(3):
            result.append(" ".join([represent_cell_state(cell_value) for cell_value in self.__space[line, :]]))

        return "\n".join(result)

    def put_x(self, line: int, column: int) -> bool:
        """Устанавливает в клетку [line, column] крестик, если она пуста, и возвращает True.
        Если клетка не пустая, то ничего возвращает False"""
        return self.__put_sign(line, column, 1)

    def put_o(self, line: int, column: int) -> bool:
        """Устанавливает в клетку [line, column] нолик, если она пуста, и возвращает True.
        Если клетка не пустая, то ничего возвращает False"""
        return self.__put_sign(line, column, -1)

    def winner(self) -> str:
        """Возвращает 'х' или 'o', если кто-то из игроков победил, или None, если победителя нет"""
        space_sums = self.__get_space_sums()
        if 3 in space_sums:
            return 'x'
        elif -3 in space_sums:
            return 'o'
        else:
            return None

    def has_winner(self):
        """Возвращает True, если в игре есть победитель, и False - в противном случае"""
        return self.winner() is not None

    def cell_is_empty(self, line, column):
        """Возвращает True, если клетка (line, column) пуста, и False - в противном случае"""
        return self.__space[line, column] == 0

    def has_empty_cells(self):
        """Возвращает True, если на поле есть пустые клетки, и False - в противном случае"""
        return 0 in self.__space

    def game_over(self) -> bool:
        """Возвращает True, если игра окончена (есть победитель или закончились пустые клетки), и False - в противном
        случае"""
        return (not self.has_empty_cells()) or self.has_winner()
