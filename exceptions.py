class BaseError(Exception):
    message = "Ошибка"


class InvalidRequest(BaseError):
    message = "Неверный запрос"


class NotEnoughSpace(BaseError):
    message = "Недостаточно места"


class ProductNotFound(BaseError):
    message = "Продукт не найден"


class NotEnoughProduct(BaseError):
    message = "Не достаточное количество имеющегося товара"


class ToManyDiferentProduct(BaseError):
    message = "Уже есть пять разных товаров"


class DepartureNotKnown(BaseError):
    message = "Пункт отправления не известен"


class DestinationNotKnown(BaseError):
    message = "Пункт назначения не известен"
