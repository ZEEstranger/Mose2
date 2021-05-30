import sys
from PyQt5.QtWidgets import QApplication, QProgressBar, QWidget, QPushButton, QLineEdit, QRadioButton, QStackedWidget, \
                            QVBoxLayout, QGridLayout, QDialog, QLabel
from PyQt5.QtCore import Qt   
from hero import Hero     


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

class NewGamePage(QWidget): # Window New Game with choice of difficulty
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.newGameEasyButton = QPushButton("Easy")
        self.newGameMediumButton = QPushButton("Medium (soon)")
        self.newGameHardButton = QPushButton("Hard (soon)")
        self.newGameBackButton = QPushButton("Back")

        self.newGameMediumButton.setEnabled(True)
        self.newGameHardButton.setEnabled(False)

        layout.addWidget(self.newGameEasyButton)
        layout.addWidget(self.newGameMediumButton)
        layout.addWidget(self.newGameHardButton)
        layout.addWidget(self.newGameBackButton)

        self.setLayout(layout)

class FightingWin(QWidget):
    def __init__(self, hero, enemy):
        super().__init__()

        self.hero = hero
        self.enemy = enemy

        layout = QGridLayout()
        layout.rowStretch(10)

        self.heroHPLabel = QLabel(self)
        self.enemyHPLabel = QLabel(self)
        self.heroHPLabel.setText("Hero HP = " + str(self.hero.geta()))
        self.enemyHPLabel.setText("Enemy HP =" + str(self.enemy.getHP()))

        self.heroHPPbar = QProgressBar(self)
        self.enemyHPPbar = QProgressBar(self)
        self.heroHPPbar.setValue(self.hero.geta())
        self.enemyHPPbar.setValue((self.enemy.getHP()/self.enemy.getMaxHP())*100)

        self.heroDamageButton = QPushButton()
        self.heroDamageButton.clicked.connect(self.heroDamageToEnemy)

        layout.addWidget(self.heroHPLabel, 1, 0, 1, 3)
        layout.addWidget(self.enemyHPLabel, 1, 3, 1, 3)
        layout.addWidget(self.heroHPPbar, 2, 0, 1, 3)
        layout.addWidget(self.enemyHPPbar, 2, 3, 1, 3)
        layout.addWidget(self.heroDamageButton, 3, 0)


        self.newGameBackButton = QPushButton("Back")
        layout.addWidget(self.newGameBackButton, 4, 0)

        self.setLayout(layout)

    def heroDamageToEnemy(self):
        self.enemy.setInputDamage(self.hero.getDamage())
        self.enemyHPLabel.setText("Enemy HP =" + str(self.enemy.getHP()))
        self.enemyHPPbar.setValue((self.enemy.getHP()/self.enemy.getMaxHP())*100)
