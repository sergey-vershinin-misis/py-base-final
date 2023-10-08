class Stack:

    def __init__(self, seq=()):
        self.__storage = list(seq)

    def push(self, element):
        self.__storage.append(element)

    def pop(self):
        return self.__storage.pop()

    def peek(self):
        return self.__storage[-1]

    def length(self):
        return len(self.__storage)

    def __repr__(self):
        return self.__storage.__repr__()

    def __iter__(self):
        return self.__storage.__iter__()
