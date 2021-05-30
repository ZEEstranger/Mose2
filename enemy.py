


class Enemy():
    def __init__(self) -> None:
        

        self.hp = 50
        self.maxHp = 100
        self.damage = 10

    def getHP(self):
        return self.hp

    def getDamage(self):
        return self.damage

    def getMaxHP(self):
        return self.maxHp

    def setHP(self, damage):
        self.hp -= damage

    def setDamage(self, damage):
        self.damage = damage

    def setHP(self, max_hp):
        self.maxHp = max_hp

    def setInputDamage(self, damage):
        self.hp -= damage