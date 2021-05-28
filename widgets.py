import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QRadioButton, QStackedWidget, \
                            QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt   
from hero import Hero       

class WidgetButtons(QWidget):
    def __init__(self, hero):
        super().__init__()

        self.heroUnit = hero

        layout = QVBoxLayout()

        for i in range(3):
            layout.addWidget(QPushButton(f'Button #{i}'))

        self.but1 = QPushButton("printa")
        self.but1.clicked.connect(self.printa)

        layout.addWidget(self.but1)

        self.setLayout(layout)

    def printa(self):
        print(self.heroUnit.geta())

class WidgetLineEdits(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        for i in range(3):
            layout.addWidget(QLineEdit(f'LineEdit #{i}'))

        

        self.setLayout(layout)


class WidgetRadioButtons(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        for i in range(4):
            layout.addWidget(QRadioButton(f'RaidoButton #{i}'))

        self.setLayout(layout)
