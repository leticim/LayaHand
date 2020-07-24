class HomeController:
    def __init__(self):
        self.message = "this message is important "

    def get(self):
        self.message += "/n and this message is also important"
        return self.message