def cache(verbose: bool = False):
    """Декоратор для кэширования результата вычисления произвольной функции.

    Если установить аргумент verbose в True, декоратор будет выводить подробную информацию о вызовах декорируемой
    функции и результатах поиска ее значений в кеше.

    В качестве ключа для кэширования значения функции используется кортеж, вычисленный как (args, tuple(kwargs.items()).
    Поэтому для корректной работы обязательным условием является то, чтобы значение хэш-функции для этого кортежа
    было одинаковым для одинаковых наборов входных аргументов (в том смысле, в каком в вашей задаче понимается
    "одинаковость").
    """
    cached_values = {}

    def actual_decorator(func):

        if func.__name__ not in cached_values:
            cached_values[func.__name__] = {}
        func_cached_values = cached_values[func.__name__]

        def cached_wrapper(*args, **kwargs):
            key = (args, tuple(kwargs.items()))
            if verbose:
                print(f'   Вызов функции {func.__name__} c аргументами args {args} и kwargs {kwargs}')

            if key not in func_cached_values:
                if verbose:
                    print('   Результат не найден в кэше - вызов функции')
                func_cached_values[key] = func(*args)
            else:
                if verbose:
                    print('   Результат найден в кеше: ', func_cached_values[key])

            return func_cached_values[key]

        return cached_wrapper

    return actual_decorator


@cache(verbose=True)
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


@cache(verbose=True)
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
