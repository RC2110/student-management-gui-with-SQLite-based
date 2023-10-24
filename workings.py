from PyQt6.QtWidgets import QApplication, QLabel, QGridLayout, QLineEdit, QWidget, QPushButton
import sys
from datetime import datetime

class AgeCalculator(QWidget): #inheriting from QWidget parent. We can also inherit from QVboxlayout
    def __init__(self):
        super().__init__() # we need to init the parent class as well.
        grid = QGridLayout()
        self.setWindowTitle("Age Calculator")
        name_label= QLabel("Name:")
        self.name_line = QLineEdit()
        date_label= QLabel("Enter your date of birth dd/mm/yyyy:")
        self.date_line = QLineEdit()
        calculate = QPushButton("Calculate")
        calculate.clicked.connect(self.calculate_age)
        self.name_label2= QLabel("")

        grid.addWidget(name_label,0,0)
        grid.addWidget(self.name_line,0,1)
        grid.addWidget(date_label,1,0)
        grid.addWidget(self.date_line,1,1)
        grid.addWidget(calculate,2,0,1,2)
        grid.addWidget(self.name_label2,3,0,1,2)

        self.setLayout(grid) #using parent class intance variable setlayout to align the grids.

    def calculate_age(self):
        year = datetime.now().year
        date_of_birth = self.date_line.text()
        year_of_birth= datetime.strptime(date_of_birth, "%d/%m/%Y").date().year
        age = year - year_of_birth
        self.name_label2.setText(f"{self.name_line.text()} is {age} year's old")


app = QApplication(sys.argv)
age = AgeCalculator()
age.show()
sys.exit(app.exec())  # code to keep the application running