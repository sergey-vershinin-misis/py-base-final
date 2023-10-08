from task01.stack import Stack


class TaskManager:
    def __init__(self):
        self.__task_storage = Stack()

    def contains_task(self, name: str) -> bool:
        return name in map(lambda task_item: task_item[0], self.__task_storage)

    def add_task(self, name: str, priority: int) -> None:
        if self.contains_task(name):
            raise ValueError('Менеджер задач уже содержит задачу с таким именем')

        self.__task_storage.push((name, priority))

    def remove_task(self, name: str) -> None:
        self.__task_storage = Stack([task_item for task_item in self.__task_storage if task_item[0] != name])

    def task_count(self):
        return self.__task_storage.length()

    def __repr__(self):
        results = dict()
        for name, priority in sorted(self.__task_storage, key=lambda task_info: task_info[1]):
            results[priority] = results.get(priority, [])
            results[priority].append(name)

        return '\n'.join([f'{priority} {", ".join(task_names)}' for priority, task_names in results.items()])
