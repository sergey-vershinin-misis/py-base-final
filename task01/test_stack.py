from unittest import TestCase

from task01.stack import Stack


class TestStack(TestCase):

    def test_init_empty_stack(self):
        stack = Stack()
        self.assertEqual(stack.length(), 0, "Длина пустого стека не равна 0")

    def test_init_stack_with_list(self):
        stack = Stack([10, 20, 30])
        self.assertEqual(stack.length(), 3, "Количество элементов не совпадает с ожидаемым")

    def __get_initial_stack(self):
        return Stack([10, 20, 30])

    def test_push(self):
        stack = self.__get_initial_stack()
        stack.push(40)

        self.assertEqual(stack.length(), 4, 'Количество элементов в стеке не совпадает с ожидаемым')
        self.assertEqual(stack.peek(), 40, 'Элемент в вершине стека не совпадает с ожидаемым')

    def test_pop(self):
        stack = self.__get_initial_stack()

        self.assertEqual(stack.pop(), 30, 'Элемент, полученный вызовом метода pop, не совпадает с ожидаемым')
        self.assertEqual(stack.length(), 2, 'Количество элементов в стеке после вызова pop не совпадает с '
                                            'ожидаемым')

    def test_peek(self):
        stack = self.__get_initial_stack()

        self.assertEqual(stack.peek(), 30, 'Элемент, полученный вызовом peek, не совпадает с ожидаемым')
        self.assertEqual(stack.length(), 3, 'Количество элементов стека после вызова peek не совпадает с '
                                            'ожидаемым')

    def test_length(self):
        stack = self.__get_initial_stack()

        self.assertEqual(stack.length(), 3, 'Количество элементов в стеке не совпадает с ожидаемым')

    def test_pop_with_empty_stack(self):
        stack = Stack()

        with self.assertRaises(IndexError, ):
            stack.pop()

    def test_stack_as_iterable(self):
        expected_result_list = [10, 20, 30]
        stack = Stack(expected_result_list)
        for i, element in enumerate(stack):
            self.assertEqual(element, expected_result_list[i], f'Элемент стека с индексом {i} отличается от ожидаемого')
