class Stack:
    """Класс Stack реализует функциональность структуры данных 'стек', предоставляя разработчику базовый
     набор методов для работы со стеком: добавление элемента в стек, удаление элемента из вершины стека,
     просмотр элемента в вершине стека

     Кроме того, объекты класса Stack являются итерируемым, что позволяет обходить элементы стека в циклах, а также
     применять другие средства языка python для работы с итерируемыми объектами  """
    def __init__(self, seq=()):
        """Создает пустой стек или стек, содержащий элементы в seq"""
        self.__storage = list(seq)

    def push(self, element):
        """Добавляет элемент в вершину стека"""
        self.__storage.append(element)

    def pop(self):
        """Удаляет элемент из вершины стека и возвращает его"""
        return self.__storage.pop()

    def peek(self):
        """Возвращает элемент из вершины стека, не удаляя его"""
        return self.__storage[-1]

    def length(self):
        """Возвращает количество элементов в стеке"""
        return len(self.__storage)

    def __repr__(self):
        return self.__storage.__repr__()

    def __iter__(self):
        return self.__storage.__iter__()
