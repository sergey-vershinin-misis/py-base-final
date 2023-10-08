"""
Задание 1. Стек и менеджер задач
"""
from task01.stack import Stack
from task01.task_manager import TaskManager


def demo_task01():
    # st = Stack()
    # st.push(2)
    # st.push(3)
    # st.push(4)
    # print('peek:', st.peek())
    # print(st.length())
    # print(st)
    # st.push(5)
    # print(st)
    # st.pop()
    # print(st)

    manager = TaskManager()
    manager.add_task('Составить список задач', 2)
    manager.add_task('Вывести список задач', 3)
    manager.add_task('Проверить вывод списка', 2)
    manager.add_task('Проанализировать список задач', 1)
    try:
        manager.add_task('Проанализировать список задач', 1)
    except ValueError as err:
        print(err)

    print(manager)

    print(manager.contains_task('Составить список задач'))

    manager.remove_task('Составить список задач')
    print(manager)

    print(manager.contains_task('Составить список задач'))