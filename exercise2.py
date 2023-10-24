from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QGridLayout, QComboBox, QPushButton
import sys
class SpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()
        grid= QGridLayout()

        distance= QLabel("Distance:")
        self.dist_ip= QLineEdit()

        self.select = QComboBox()
        self.select.addItems(["km", "miles"])
        # select.

        timelabel=QLabel("Time(in hours):")
        self.time_ip=QLineEdit()

        calculate = QPushButton("Calculate")
        calculate.clicked.connect(self.calculate)
        self.outp = QLabel("")

        grid.addWidget(distance, 0, 0)
        grid.addWidget(self.dist_ip, 0, 1)
        grid.addWidget(self.select, 0, 2) # adding to first row and third column
        grid.addWidget(timelabel, 1, 0)
        grid.addWidget(self.time_ip, 1, 1)
        grid.addWidget(calculate, 2, 0, 1, 2)
        grid.addWidget(self.outp, 3, 0, 1, 2)

        self.setLayout(grid)

    def calculate(self):
        distance=float(self.dist_ip.text())
        time=float(self.time_ip.text())
        speed = distance / time

        if self.select.currentText()== "km":
            speed = round(speed, 2)
            unit = "km/hr"

        elif self.select.currentText()== "miles":
            speed = round(speed * 0.621371, 2)
            unit = "miles/hr"

        self.outp.setText(f"The Speed is {speed} {unit}")


app = QApplication(sys.argv)
speed= SpeedCalculator()
speed.show()
sys.exit(app.exec())
