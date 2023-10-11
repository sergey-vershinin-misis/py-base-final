from task01.stack import Stack


class TaskManager:
    """Класс TaskManager - реализация простейшего менеджера задач, который позволяет добавить новую задачу и ее
     приоритет, проверить, содержится ли задача в списке задач, удалить задачу из списка задач, а также вывести
     список задач на экран"""

    def __init__(self):
        """Создает новый менеджер с пустым списком задач"""
        self.__task_storage = Stack()

    def contains_task(self, name: str) -> bool:
        """Возвращает True, если задача с именем name содержится в списке задач, и False в противном случае"""
        return name in map(lambda task_item: task_item[0], self.__task_storage)

    def add_task(self, name: str, priority: int) -> None:
        """Добавляет в список задач задачу с именем name и приоритетом priority. Генерирует исключение
        ValueError, если задача с таким именем уже содержится в списке задач"""
        if self.contains_task(name):
            raise ValueError('Менеджер задач уже содержит задачу с таким именем')

        self.__task_storage.push((name, priority))

    def remove_task(self, name: str) -> None:
        """Удаляет задачу с именем name из списка задач. Не генерирует ошибку, если задача с таким именем отсутствует"""
        # Удаление задачи реализовано путем пересоздания стека, но без удаляемого элемента. Не самый эффективный способ,
        # но он позволяет не усложнять интерфейс класса Stack, оставляя его обычным стеком.
        self.__task_storage = Stack([task_item for task_item in self.__task_storage if task_item[0] != name])

    def task_count(self):
        """Возвращает количество задача в списке задач менеджера"""
        return self.__task_storage.length()

    def __repr__(self):
        results = dict()
        for name, priority in sorted(self.__task_storage, key=lambda task_info: task_info[1]):
            results[priority] = results.get(priority, [])
            results[priority].append(name)

        return '\n'.join([f'{priority} {", ".join(task_names)}' for priority, task_names in results.items()])
