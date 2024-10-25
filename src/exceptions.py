class InvalidData (Exception):
    def __init__(self, message="Invalid data provided"):
        self.message = message
        super().__init__(self.message)
