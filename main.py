from game import Game
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QWidget, QPushButton, QLineEdit, QRadioButton, QStackedWidget, \
                            QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import QCoreApplication, Qt                         
from windows import FightingWin, MenuWindow, NewGamePage
from hero import Hero
from enemy import Enemy

class MainWindow(QWidget):
    
    def __init__(self, game, hero, enemy): # Input data
        super().__init__() 
        
        self.game = game
        self.hero = hero
        self.enemy = enemy

        self.setGeometry(500, 500, 500, 200)

        self.setupMainWindow()
        
    def setupMainWindow(self): # Main window
        
        mainLayout = QVBoxLayout()


        self.mainPage1 = MenuWindow() # Main page with main menu 
        self.newGamePage1 = NewGamePage()
        self.fightingPage1 = FightingWin(self.hero, self.enemy)
        
        self.stackedWidget = QStackedWidget()
        self.stackedWidget.addWidget(self.mainPage1) # Index 0
        self.stackedWidget.addWidget(self.newGamePage1) # Index 1
        self.stackedWidget.addWidget(self.fightingPage1)

        


        #mainLayout.addWidget(self.headLabel)
        mainLayout.addWidget(self.stackedWidget)

        self.setLayout(mainLayout)
        self.mainPage1.newGameButton.clicked.connect(self.changeToNewGameWindow)
        self.mainPage1.exitButton.clicked.connect(self.exit)
        
        self.newGamePage1.newGameEasyButton.clicked.connect(self.selectDifficult)   
        self.newGamePage1.newGameMediumButton.clicked.connect(self.selectDifficult)
        self.newGamePage1.newGameHardButton.clicked.connect(self.selectDifficult)    
        self.newGamePage1.newGameBackButton.clicked.connect(self.backButton)
        self.fightingPage1.newGameBackButton.clicked.connect(self.backButton)

    def selectDifficult(self):
        sender = self.sender()
        if sender == self.newGamePage1.newGameEasyButton:
            
            self.game.setDifficulty(0)
            print("Difficulty was changed to ", self.game.getDifficulty())
                    
        elif sender == self.newGamePage1.newGameMediumButton:
            self.game.setDifficulty(1)
            print("Difficulty was changed to ", self.game.getDifficulty())
            print(self.enemy.getHP())

        else:
            self.game.setDifficulty(2)
            print("Difficulty was changed to ", self.game.getDifficulty())

        self.stackedWidget.setCurrentIndex(2)


    def changeToNewGameWindow(self): # Jump to select dif win
        
        self.stackedWidget.setCurrentIndex(1)

    def backButton(self):
        self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex() - 1)
    
    def exit(self): #Exit function. Close the app

        QCoreApplication.instance().quit()


class Manager(): # Manager of launch
    def __init__(self):

        self.game = Game(difficulty=0)
        self.hero = Hero()
        self.enemy = Enemy()
        self.mainWindow = MainWindow(self.game, self.hero, self.enemy)

        self.mainWindow.show()
        

app = QApplication(sys.argv)
manager = Manager()
sys.exit(app.exec_())
