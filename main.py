from entity.curier import Curier
from exeptions import InvalidRequest, DepartureNotKnown, DestinationNotKnown, BaseError
from entity.request import Request
from entity.shop import Shop
from entity.store import Store

store = Store(items={
    "печеньки": 3,
    "собачки": 2,
    "коробки": 5,
})

shop = Shop(items={
    "собачки": 2,
    "коробки": 5,
})

storages = {
    "склад": store,
    "магазин": shop
}


def main():
    print("Добрый день!\n")

    while True:

        for storage in storages:
            print(f"Сейчас в {storage}:")
            for item in storages[storage].get_items().items():
                print(f"{item[1]} {item[0]}")
            print("")
        user_input = input(
            "Пример запроса: Доставить 3 печеньки из склад в магазин\n"
            "Введите запрос ('стоп' - выход): "
        )
        if user_input.lower() in ['стоп']:
            break

        try:
            request = Request(user_input)
        except InvalidRequest as error:
            print(error.message)
            continue
        try:
            curier = Curier(storages, request)
        except (DepartureNotKnown, DestinationNotKnown) as error:
            print(error.message)
            continue
        try:
            curier.move()
        except BaseError as error:
            print(error.message)
            continue


if __name__ == "__main__":
    main()
