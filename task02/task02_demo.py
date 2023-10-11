"""
Задание 2. LRU-кэш
"""
from task02.lru_cache import LRUCache


def demo_task02():
    """Демонстрирует простой сценарий работы LRU - кэша в рамках второго задания ДЗ """

    print('\n-------------Демонстрация работы LRUCache ------------------')

    cache = LRUCache(3)
    print('1. Создаём экземпляр класса LRU Cache с capacity = 3 и печатаем его содержимое:')
    cache.print_cache()

    cache.cache = ("key1", "value1")
    cache.cache = ("key2", "value2")
    cache.cache = ("key3", "value3")
    print('2. Добавляем в кэш три элемента и снова выводим на экран:')
    cache.print_cache()

    print('3. Получаем значение по ключу "key1" и выводим его: ', cache.get("key1"))

    cache.cache = ("key4", "value4")
    print('4. Добавляем в кэш еще один объект и выводим кэш на экран, чтобы убедиться, что из него был удален '
          'LRU-элемент')
    cache.print_cache()
