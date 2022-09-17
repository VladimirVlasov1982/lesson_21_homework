from entity.abstract_storage import AbstractStorage
from exceptions import NotEnoughSpace, ProductNotFound, NotEnoughProduct


class BaseStorage(AbstractStorage):
    _capacity: int

    def __init__(self, items: dict):
        self._items = items

    def add(self, title: str, quantity: int) -> None:
        """
        Увеличивает запас items с учетом лимита capacity
        """
        if self.get_free_space() < quantity:
            raise NotEnoughSpace
        if title in self._items:
            self._items[title] += quantity
        else:
            self._items[title] = quantity

    def remove(self, title: str, quantity: int) -> None:
        """
        Уменьшает запас items но не ниже 0
        """
        if title not in self._items:
            raise ProductNotFound
        if quantity > self._items[title]:
            raise NotEnoughProduct

        self._items[title] -= quantity
        print("Нужное количество товара есть")

        if self._items[title] == 0:
            self._items.pop(title)

    def get_free_space(self) -> int:
        """
        Вернуть количество свободных мест
        """
        current_space = 0
        for value in self._items.values():
            current_space += value
        return self.get_capacity() - current_space

    def get_items(self) -> dict:
        """
        Возвращает содержание склада в словаре
        """
        return self._items

    def get_unique_items_count(self) -> int:
        """
        Возвращает количество уникальных товаров.
        """
        return len(self._items.keys())

    def get_capacity(self) -> int:
        """
        Получить вместимость помещения
        """
        return self._capacity

    def set_capacity(self, value) -> None:
        """
        Установить вместимость помещения
        """
        self._capacity = value
