from PyQt6.QtWidgets import QApplication, QLabel, QGridLayout, QLineEdit, QWidget, QPushButton
import sys
from datetime import datetime
class AgeCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Age Calculator")
        grid = QGridLayout()


        name_label = QLabel("Name:")
        self.name_linedit1 = QLineEdit()
        date_label = QLabel("Enter your date of birth DD/MM/YYYY:")
        self.name_linedit2 = QLineEdit()
        calculator= QPushButton("Calculate")
        calculator.clicked.connect(self.calculate)
        self.calc_label = QLabel("")

        grid.addWidget(name_label, 0, 0)
        grid.addWidget(self.name_linedit1, 0, 1)
        grid.addWidget(date_label, 1, 0)
        grid.addWidget(self.name_linedit2, 1, 1)
        grid.addWidget(calculator, 2, 0, 1,2)
        grid.addWidget(self.calc_label, 3, 0, 1, 2)

        self.setLayout(grid)

    def calculate(self):
        currentyear = datetime.now().year
        dateofbirth= self.name_linedit2.text()
        yearofbirth = datetime.strptime(dateofbirth, "%d/%m/%Y" ).date().year
        age = currentyear - yearofbirth
        self.calc_label.setText(f"{self.name_linedit1.text()} is {age} years old.")

##code for running application
parent = QApplication(sys.argv)
agec = AgeCalculator()
agec.show()
sys.exit(parent.exec())

