


class Hero(object):
    def __init__(self) -> None:
        super().__init__()

        self.hp = 100
        self.damage = 10

    def geta(self):
        return self.hp

    #def seta(self, a):
    #    self.a += a
    
    def getDamage(self):
        return self.damage