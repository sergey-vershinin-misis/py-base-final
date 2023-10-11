from dataclasses import dataclass


@dataclass
class _StorageEntry:
    """Используется для хранения объекта в кэше и содержит ссылку на сам объект (value) и значение счетчика в
    момент добавления объекта или в момент последнего получения объекта (last_used)"""
    value: object
    last_used: int


class LRUCache:
    """LRUCache реализует Last recently used cache фиксированной емкости, позволяющий кэшировать объекты, после чего
     получать их их кэша по ключу. В случае увеличения количества элементов кэша выше заданной емкости, из кэша удаляется
     элемент, к которому не обращались дольше всего.

     Для фиксации времени обращения за объектом используется внутренний счетчик обращений к кэшу,
     который увеличивается на единицу каждый раз, когда происходит получение объекта из кэша или размещение в кэше
     нового объекта. Значение счетчика, соответствующее размещению объекта в кэше или его последнему получению из
     кэша, хранится рядом с объектом (внутри объекта _StorageEntry). Используя это значение можно упорядочить все
     объекты в кэше от last recently used (наименьшее значение счетчика) до most recently used (наибольшее значение
     счетчика), и, соответственно, удалять last recently used элементы при переполнении кэша.

     Для хранения кэшировуемых объектов используется словарь, обеспечивающий наиболее быстрый доступ к объекту по ключу.
     """

    def __init__(self, capacity: int):
        """Создает LRUCache с емкостью capacity"""
        if capacity < 1:
            raise ValueError('Размерность кэша не может быть меньше 1')

        self.__storage = dict()
        self.__capacity = capacity

    def __get_ticks(self):
        """Инкрементирует и возвращает значение внутреннего счетчика обращений к кэшу"""
        if self.__ticker is None:
            self.__ticker = 0
        self.__ticker += 1
        return self.__ticker

    @property
    def cache(self):
        """Возвращает элемент кэша, который в последний раз использовался раньше всех остальных"""

        if len(self.__storage) == 0:
            return None

        storage_as_tuple = tuple(self.__storage.items())
        last_used_element = storage_as_tuple[0]

        for storage_element in storage_as_tuple[1:]:
            if storage_element[1].last_used < last_used_element[1].last_used:
                last_used_element = storage_element

        return last_used_element[0], last_used_element[1].value

    @cache.setter
    def cache(self, new_elem: tuple):
        """Добавляет в кэш новый элемент, представленный в виде кортежа: (ключ, значение)"""
        self.__remove_old_element_if_full()
        self.__storage[new_elem[0]] = _StorageEntry(new_elem[1], self.__get_ticks())

    def __remove_old_element_if_full(self):
        if len(self.__storage) < self.__capacity:
            return
        self.__storage.pop(self.cache[0])

    def __repr__(self):
        storage_entry: _StorageEntry
        return "LRU Cache:\n" + '\n'.join(
            [f'{key} : {storage_entry.value}' for key, storage_entry in self.__storage.items()])

    def print_cache(self):
        """Выводит текстовое представление кэша на экран"""
        print(self)

    def get(self, key):
        """Возвращает объект, хранящийся в кэшн по ключу key. Либо None, если объекта в кэше нет"""
        storage_entry: _StorageEntry = self.__storage.get(key)
        if storage_entry is not None:
            storage_entry.last_used = self.__get_ticks()
        return storage_entry.value
