from task03.cache import cache


@cache(verbose=True)
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
