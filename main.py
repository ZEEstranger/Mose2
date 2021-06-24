from game import Game
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QWidget, QPushButton, QLineEdit, QRadioButton, QStackedWidget, \
                            QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import QCoreApplication, Qt                         
from windows import FightingWin, GameMenu, MenuWindow, ChangeDifficultyPage, ShopWindow, DeathWindow
from hero import Hero
from enemy import Enemy

class MainWindow(QWidget):
    
    def __init__(self, game, hero): # Input data
        super().__init__() 
        
        self.game = game
        self.hero = hero

        self.setGeometry(500, 500, 500, 200)

        self.setupMainWindow()
        
    def setupMainWindow(self): # Main window
        
        mainLayout = QVBoxLayout()


        self.mainPage1 = MenuWindow() # Main page with main menu 
        self.changeDifficultyPage = ChangeDifficultyPage()
        self.gameMenu = GameMenu()
        self.fightingPage1 = FightingWin(self.hero)
        self.shopWindow = ShopWindow(self.hero)
        self.deathWindow = DeathWindow()
        
        self.stackedWidget = QStackedWidget()
        self.stackedWidget.addWidget(self.mainPage1)                # Index 0 | Main Page
        self.stackedWidget.addWidget(self.changeDifficultyPage)     # Index 1 | Change Difficulty
        self.stackedWidget.addWidget(self.fightingPage1)            # Index 2 | Fighting Page
        self.stackedWidget.addWidget(self.gameMenu)                 # Index 3 | Game Menu
        self.stackedWidget.addWidget(self.shopWindow)               # Index 4 | Shop
        self.stackedWidget.addWidget(self.deathWindow)              # Index 5 | Death


        mainLayout.addWidget(self.stackedWidget)

        self.setLayout(mainLayout)
        self.mainPage1.newGameButton.clicked.connect(self.toChangeDifficultyWindow)
        self.mainPage1.exitButton.clicked.connect(self.exit)

        self.gameMenu.fightButton.clicked.connect(self.toFightWindow)

        self.gameMenu.shopButton.clicked.connect(self.toShopWindow)
        
        self.changeDifficultyPage.changeDifficultyEasyButton.clicked.connect(self.selectDifficult)
        self.changeDifficultyPage.changeDifficultyMediumButton.clicked.connect(self.selectDifficult)
        self.changeDifficultyPage.changeDifficultyHardButton.clicked.connect(self.selectDifficult)

        self.changeDifficultyPage.changeDifficultyBackButton.clicked.connect(self.toGameMenuWindow)
        self.fightingPage1.fightBackButton.clicked.connect(self.toGameMenuWindow)
        self.gameMenu.backButton.clicked.connect(self.toMainWindow)
        self.shopWindow.backButton.clicked.connect(self.toGameMenuWindow)


    def toMainWindow(self):

        self.stackedWidget.setCurrentIndex(0)

    def toChangeDifficultyWindow(self): # Jump to select dif window
        
        self.stackedWidget.setCurrentIndex(1)

    def toGameMenuWindow(self):

        self.stackedWidget.setCurrentIndex(3)

    def toFightWindow(self):

        self.stackedWidget.setCurrentIndex(2)
        self.fightingPage1.heroHealPotion.setText("You have - " + str(self.hero.getHealPotion()) + " heal potion(s)")

    def toShopWindow(self):

        self.stackedWidget.setCurrentIndex(4)
        self.shopWindow.hero = self.hero
        self.shopWindow.moneyLabel.setText("Your money: " + str(self.hero.getMoney()))

    def selectDifficult(self):
        sender = self.sender()
        if sender == self.changeDifficultyPage.changeDifficultyEasyButton:
            
            self.game.setDifficulty(0)
            print("Difficulty was changed to ", self.game.getDifficulty())
                    
        elif sender == self.changeDifficultyPage.changeDifficultyMediumButton:
            self.game.setDifficulty(1)
            print("Difficulty was changed to ", self.game.getDifficulty())
            print(self.enemy.getHP())

        else:
            self.game.setDifficulty(2)
            print("Difficulty was changed to ", self.game.getDifficulty())

        self.stackedWidget.setCurrentIndex(3)

    def exit(self): #Exit function. Close the app

        QCoreApplication.instance().quit()


class Manager(): # Manager of launch
    def __init__(self):

        self.game = Game(difficulty=0)
        self.hero = Hero()
        self.mainWindow = MainWindow(self.game, self.hero)

        self.mainWindow.show()
        

app = QApplication(sys.argv)
manager = Manager()
sys.exit(app.exec_())
