from PyQt6.QtWidgets import QApplication, QLabel, QGridLayout, QLineEdit, QVBoxLayout, QWidget, \
    QPushButton
import sys
from datetime import  datetime

class AgeCalculator(QWidget):
    def __init__(self):

        super().__init__()
        grid = QGridLayout()

        name_label = QLabel("Enter your name:")
        self.name_inp = QLineEdit()
        dob_label = QLabel("Enter your Date of Birth:")
        self.dob_inp = QLineEdit()
        calc_label = QPushButton("Calculate")
        calc_label.clicked.connect(self.calculate)
        self.opt_show = QLabel("")

        grid.addWidget(name_label, 0, 0)
        grid.addWidget(self.name_inp, 0, 1)
        grid.addWidget(dob_label, 1, 0)
        grid.addWidget(self.dob_inp, 1, 1)
        grid.addWidget(calc_label, 2, 0, 1, 2)
        grid.addWidget(self.opt_show, 3, 0, 1, 2)

        self.setLayout(grid)


    def calculate(self):
        current_year = datetime.now().year
        yob = self.dob_inp.text()
        year= datetime.strptime(yob, "%d/%m/%Y").date().year
        age= current_year - year
        print(age)
        self.opt_show.setText(f"{self.name_inp.text()} is {age} year's old")


parent = QApplication(sys.argv)
calc = AgeCalculator()
calc.show()
sys.exit(parent.exec())