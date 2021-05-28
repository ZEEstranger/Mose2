


class Hero(object):
    def __init__(self) -> None:
        super().__init__()

        self.a = 10

    def geta(self):
        return self.a

    def seta(self, a):
        self.a = a