from entity.base_storage import BaseStorage


class Store(BaseStorage):
    _capacity: int = 100

    def __init__(self, items: dict):
        super().__init__(items)

    def __repr__(self):
        return f"{self.get_items()}"
