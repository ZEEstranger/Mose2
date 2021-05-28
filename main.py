import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QRadioButton, QStackedWidget, \
                            QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt                         
from widgets import WidgetButtons, WidgetLineEdits, WidgetRadioButtons
from hero import Hero

class AppDemo(QWidget):
    def __init__(self, hero):
        super().__init__()

        self.heroUnit = hero

        mainLayout = QVBoxLayout()

        self.stackedWidget = QStackedWidget()
        self.stackedWidget.addWidget(WidgetButtons(self.heroUnit)) # index 0
        self.stackedWidget.addWidget(WidgetLineEdits()) # index 1
        self.stackedWidget.addWidget(WidgetRadioButtons()) # index 2

        buttonPrevious = QPushButton('Previous')
        buttonPrevious.clicked.connect(self.previousWidget)

        buttonNext = QPushButton('Next')
        buttonNext.clicked.connect(self.nextWidget)

        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(buttonPrevious)
        buttonLayout.addWidget(buttonNext)

        mainLayout.addWidget(self.stackedWidget)
        mainLayout.addLayout(buttonLayout)
        self.setLayout(mainLayout)

        

    def nextWidget(self):
        self.stackedWidget.setCurrentIndex((self.stackedWidget.currentIndex() + 1) % 3)

    def previousWidget(self):
        self.stackedWidget.setCurrentIndex((self.stackedWidget.currentIndex() - 1) % 3)     

app = QApplication(sys.argv)
pep = Hero()
demo = AppDemo(pep)
demo.show()
sys.exit(app.exec_())