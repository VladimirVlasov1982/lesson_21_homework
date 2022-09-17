from entity.base_storage import BaseStorage
from exceptions import ToManyDiferentProduct


class Shop(BaseStorage):
    _capacity: int = 20

    def __init__(self, items: dict):
        super().__init__(items)

    def add(self, title: str, quantity: int) -> None:
        """
        Добавление товара в магазин с проверкой на количество уникальных товаров.
        """
        if title not in self.get_items():
            if self.get_unique_items_count() >= 5:
                raise ToManyDiferentProduct

        super().add(title, quantity)

    def __repr__(self):
        return f"{self.get_items()}"
