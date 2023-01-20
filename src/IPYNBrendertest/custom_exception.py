class InvalidURLException(Exception):
    def __init__(self, message: str = "url is not valid"):
        self.message = message
        super().__init__(self.message)
