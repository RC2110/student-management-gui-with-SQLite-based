from PyQt6.QtWidgets import QApplication, QVBoxLayout, QGridLayout, QLineEdit, QPushButton, QWidget, QLabel
import sys
from datetime import datetime

class AgeCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Äge Calculator")
        grid=QGridLayout()

        name=QLabel("Enter your name:")
        self.name_ip=QLineEdit()
        dob=QLabel("Enter your date of birth DD/MM/YYYY:")
        self.dob_ip=QLineEdit()
        calculate = QPushButton("Calculate")
        calculate.clicked.connect(self.calculate)
        self.outlabel = QLabel("")

        grid.addWidget(name, 0, 0)
        grid.addWidget(self.name_ip, 0, 1)
        grid.addWidget(dob, 1, 0)
        grid.addWidget(self.dob_ip, 1, 1)
        grid.addWidget(calculate, 2, 0, 1, 2)
        grid.addWidget(self.outlabel, 3, 0, 1, 2)

        self.setLayout(grid)


    def calculate(self):
        current_year =  datetime.now().year
        yearofbirth = datetime.strptime(self.dob_ip.text(), "%d/%m/%Y").date().year
        age = current_year - yearofbirth
        self.outlabel.setText(f"{self.name_ip.text()} is {age} years old")


app = QApplication(sys.argv)
age= AgeCalculator()
age.show()
sys.exit(app.exec())

