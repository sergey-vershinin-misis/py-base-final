"""
Задание 3. Кэширование результатов вызова рекурсивной функции
"""
from task03.cached_fibonacci import fibonacci, factorial


def demo_task03():
    """Демонстрирует работу рекурсивных функций с кэшированием значений в рамках третьего задания ДЗ """

    print('\n-------------Демонстрация работы декоратора для кэширования значения функции ------------------')
    while True:
        print('\n\nВведите номер, соответствующий функции, значение которой вы хотите вычислить')
        print('1 - число Фибоначчи, 2 - факториал, q - выход')
        func_code = input("")
        if func_code.lower() == 'q':
            return
        elif func_code == '1' or func_code == '2':
            try:
                n = int(input("Введите натуральный аргумент функции:"))
            except:
                print('Не удалось преобразовать введенное значение к целому числу')
                continue
            if n < 0:
                print('Введенное число отрицательно')
                continue
            if func_code == '1':
                calc_fibonacci_number(n)
            if func_code == '2':
                calc_factorial(n)


def calc_fibonacci_number(n: int):
    print(f'\nВычисляем число Фибоначчи под номером {n} ...')
    print(f'Число Фибоначчи под номером {n}:', fibonacci(n))


def calc_factorial(n: int):
    print(f'\nВычисляем {n}! ...')
    print(f'{n}! =', factorial(n))