from exeptions import InvalidRequest


class Request:
    def __init__(self, user_input: str):
        parsed_request = user_input.lower().split(' ')
        if len(parsed_request) != 7:
            raise InvalidRequest
        self.departure = parsed_request[4]
        self.destination = parsed_request[6]
        self.amount = int(parsed_request[1])
        self.product = parsed_request[2]

    def __repr__(self):
        return f"Из {self.departure} в {self.destination} доставить {self.amount} {self.product}"
