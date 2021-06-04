class UserNotFoundError(Exception):
    def __init__(self, message):
        super().__init__(message)


class QueryMissingError(Exception):
    def __init__(self, message):
        super().__init__(message)


class EventTypeNotFound(Exception):
    def __init__(self, message):
        super().__init__(message)
