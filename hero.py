


class Hero(object):
    def __init__(self) -> None:
        super().__init__()

        self.__hp = 20
        self.__maxHP = 100 
        self.__damage = 10
        self.__killedMonsters = 0
        self.__money = 1000
        self.__healPotion = 0
        self.__healPotionPower = 30

    def reload (self):

        self.__hp = 20
        self.__maxHP = 100 
        self.__damage = 10
        self.__killedMonsters = 0
        self.__money = 1000
        self.__healPotion = 0
        self.__healPotionPower = 30
        
    def getHP(self):
        return self.__hp
        
    def getMaxHP(self):
        return self.__maxHP

    def getHPPercent(self):
        return self.__hp/self.__maxHP*100
    
    def getDamage(self):
        return self.__damage

    def getKilledMonster(self):
        return self.__killedMonsters

    def getMoney(self):
        return self.__money

    def getHealPotion(self):
        return self.__healPotion

    def getDeath(self):
        if self.__hp <= 0:
            return True
        else:
            return False
            
###############################################

    def takeDamage(self, damage):
        self.__hp -= damage

    def killMonster(self):
        self.__killedMonsters += 1

    def changeMoney(self, count):
        self.__money += count

    def changeHealPotionCount(self, count):
        self.__healPotion += count
        print("hehe boiiiii")

    def healWithHealPotion(self):
        if self.__healPotion > 0:
            self.__hp += self.__healPotionPower
            if self.__hp > self.__maxHP:
                self.__hp = self.__maxHP
            self.__healPotion -= 1