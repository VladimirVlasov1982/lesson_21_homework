from entity.abstract_storage import AbstractStorage
from exeptions import DepartureNotKnown, DestinationNotKnown, BaseError
from entity.request import Request


class Curier:
    def __init__(self, storages: dict[str, AbstractStorage], request: Request):
        self._request = request

        if self._request.departure not in storages:
            raise DepartureNotKnown

        if self._request.destination not in storages:
            raise DestinationNotKnown

        self._from = storages[self._request.departure]
        self._to = storages[self._request.destination]

    def move(self) -> None:
        """
        Перемещение товаров из места доставки в место назначения
        """
        self._from.remove(self._request.product, self._request.amount)
        print(f"Курьер забрал {self._request.amount} {self._request.product} из {self._request.departure}")
        try:
            self._to.add(self._request.product, self._request.amount)
            print(f"Курьер доставил {self._request.amount} {self._request.product} в {self._request.destination}")
        except BaseError as error:
            print(error.message)
            self.cancel()

    def cancel(self):
        """
        Возрат товара в место доставки, если не получилось отгрузить товар в месте назначения
        """
        self._from.add(self._request.product, self._request.amount)
        print(f"Курьер вернул {self._request.amount} {self._request.product} в {self._request.departure}")
