class HttpRequestError(Exception):
    """
        Exception raised when the request is not valid.
    """
    def __init__(self, message: str, status_code: int) -> None:
        super().__init__(message)
        self.message = message
        self.status_code = status_code

    def __str__(self):
        return self.message
