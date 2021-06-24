import sys
from PyQt5.QtWidgets import QApplication, QProgressBar, QWidget, QPushButton, QLineEdit, QRadioButton, QStackedWidget, \
                            QVBoxLayout, QGridLayout, QDialog, QLabel
from PyQt5.QtCore import Qt   
from hero import Hero  
from enemy import Enemy  
import time 
import random


class MenuWindow(QWidget): # First window with main menu
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.headLabel = QLabel("Welcome to Mose2")

        self.newGameButton = QPushButton("New Game")
        self.loadGameButton = QPushButton("Load Game (soon)")
        self.exitButton = QPushButton("Exit")

        self.loadGameButton.setEnabled(False)

        layout.addWidget(self.headLabel)
        layout.addWidget(self.newGameButton)
        layout.addWidget(self.loadGameButton)
        layout.addWidget(self.exitButton)

        self.setLayout(layout)

class ChangeDifficultyPage(QWidget): # Window New Game with choice of difficulty
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.changeDifficultyEasyButton = QPushButton("Easy")
        self.changeDifficultyMediumButton = QPushButton("Medium (soon)")
        self.changeDifficultyHardButton = QPushButton("Hard (soon)")
        self.changeDifficultyBackButton = QPushButton("Back")

        self.changeDifficultyMediumButton.setEnabled(False)
        self.changeDifficultyHardButton.setEnabled(False)

        layout.addWidget(self.changeDifficultyEasyButton)
        layout.addWidget(self.changeDifficultyMediumButton)
        layout.addWidget(self.changeDifficultyHardButton)
        layout.addWidget(self.changeDifficultyBackButton)

        self.setLayout(layout)

class GameMenu(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()

        self.fightButton = QPushButton("Fight")
        self.shopButton = QPushButton("Shop")
        self.backButton = QPushButton("Back")

        self.backButton.setEnabled(False)

        self.layout.addWidget(self.fightButton)
        self.layout.addWidget(self.shopButton)
        self.layout.addWidget(self.backButton)

        self.setLayout(self.layout)

class FightingWin(QWidget):
    def __init__(self, hero):
        super().__init__()

        self.hero = hero
        self.enemy = Enemy()
        
        self.deathFlag = False

        self.layout = QGridLayout()
        self.layout.rowStretch(10)

        self.monsterKilled = QLabel(self)
        self.heroHealPotion = QLabel(self)
        self.heroHPLabel = QLabel(self)
        self.enemyHPLabel = QLabel(self)
        
        self.monsterKilled.setText("Monsters were killed: " + str(self.hero.getKilledMonster()))
        self.heroHPLabel.setText("Hero HP = " + str(self.hero.getHP()))
        self.enemyHPLabel.setText("Enemy HP =" + str(self.enemy.getHP()))

        self.heroHPPbar = QProgressBar(self)
        self.enemyHPPbar = QProgressBar(self)
        self.heroHPPbar.setValue(self.hero.getHPPercent())
        self.enemyHPPbar.setValue((self.enemy.getHP()/self.enemy.getMaxHP())*100)

        self.heroDamageButton = QPushButton("take damage to enemy")
        self.heroHealButton = QPushButton("heal with heal potion")

        self.heroDamageButton.clicked.connect(self.heroDamageToEnemy)
        self.heroHealButton.clicked.connect(self.heroHealWithHealPotion)

        self.layout.addWidget(self.monsterKilled, 0, 1, 1, 3)
        self.layout.addWidget(self.heroHealPotion, 1, 1, 1, 3)
        self.layout.addWidget(self.heroHPLabel, 2, 0, 1, 3)
        self.layout.addWidget(self.enemyHPLabel, 2, 3, 1, 3)
        self.layout.addWidget(self.heroHPPbar, 3, 0, 1, 3)
        self.layout.addWidget(self.enemyHPPbar, 3, 3, 1, 3)
        self.layout.addWidget(self.heroDamageButton, 4, 0)
        self.layout.addWidget(self.heroHealButton, 5, 0)


        self.fightBackButton = QPushButton("Back")
        self.layout.addWidget(self.fightBackButton, 6, 0)

        self.setLayout(self.layout)

    def heroDamageToEnemy(self):
        self.heroDamageButton.setEnabled(False)
        self.setLayout(self.layout)

        # Hero deal damage
        self.enemy.takeDamage(self.hero.getDamage())
        self.enemyHPLabel.setText("Enemy HP =" + str(self.enemy.getHP()))
        self.enemyHPPbar.setValue(self.enemy.getHPPercent())

        if self.enemy.checkDeath() == True:
            del self.enemy
            self.deathFlag = True
    
        time.sleep(0.4)
        self.heroDamageButton.setEnabled(True)
        self.setLayout(self.layout)

        # Hero take damage
        if self.deathFlag == True:
            self.enemy = Enemy()
            self.deathFlag = False
            self.enemyHPLabel.setText("Enemy HP =" + str(self.enemy.getHP()))
            self.enemyHPPbar.setValue(self.enemy.getHPPercent())
            self.hero.killMonster()
            self.monsterKilled.setText("Monsters were killed: " + str(self.hero.getKilledMonster()))
            self.hero.changeMoney(self.enemy.getMoneyCoef() * random.randint(0, 100))

        else:
            self.hero.takeDamage(self.enemy.getDamage())
            self.heroHPLabel.setText("Hero HP = " + str(self.hero.getHP()))
            self.heroHPPbar.setValue(self.hero.getHPPercent())
            if self.hero.getDeath():
                self.hero.reload()
                self.heroHPLabel.setText("Hero HP = " + str(self.hero.getHP()))
                self.heroHPPbar.setValue(self.hero.getHPPercent())
                self.monsterKilled.setText("Monsters were killed: " + str(self.hero.getKilledMonster()))
                self.heroHealPotion.setText("You have - " + str(self.hero.getHealPotion()) + " heal potion(s)")

    def heroHealWithHealPotion(self):
        self.hero.healWithHealPotion()
        self.heroHPLabel.setText("Hero HP = " + str(self.hero.getHP()))
        self.heroHPPbar.setValue(self.hero.getHPPercent())
        self.heroHealPotion.setText("You have - " + str(self.hero.getHealPotion()) + " heal potion(s)")
        

class ShopWindow(QWidget):
    def __init__(self, hero) :
        super().__init__()

        self.hero = hero

        self.layout = QVBoxLayout()

        self.moneyLabel = QLabel(self)
        self.healPotionButton = QPushButton("Buy Heal Potion")
        self.backButton = QPushButton("Back")

        self.healPotionButton.clicked.connect(self.buyHealPotion)

        self.layout.addWidget(self.moneyLabel)
        self.layout.addWidget(self.healPotionButton)
        self.layout.addWidget(self.backButton)
        
        self.setLayout(self.layout)

    def buyHealPotion(self, hero):
        self.hero.changeHealPotionCount(1)
        self.hero.changeMoney(-100)
        self.moneyLabel.setText("Your money: " + str(self.hero.getMoney()))

class DeathWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()

        self.deathLabel = QLabel(self)
        self.deathLabel.setText("You are dead! Please restart game! I'm sorry...")

        self.layout.addWidget(self.deathLabel)

        self.setLayout(self.layout)