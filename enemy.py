

class Enemy():
    def __init__(self) -> None:
        

        self.__hp = 50
        self.__maxHP = 50
        self.__damage = 10
        self.__moneyCoefficient = 1

    def getHP(self):
        return self.__hp

    def getDamage(self):
        return self.__damage

    def getMaxHP(self):
        return self.__maxHP

    def getHPPercent(self):
        return self.__hp/self.__maxHP*100
    
    def getMoneyCoef(self):
        return self.__moneyCoefficient

    ################################################

    def takeDamage(self, damage):
        self.__hp -= damage

    def setDamage(self, damage):
        self.__damage = damage

    def setHP(self, max_hp):
        self.__maxHp = max_hp

    def checkDeath(self):
        
        if self.__hp <= 0:
            return True
        else:
            return False
