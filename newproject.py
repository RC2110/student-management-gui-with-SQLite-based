import sys
from PyQt6.QtWidgets import QApplication, QLabel, QGridLayout, QVBoxLayout, QPushButton, QMainWindow, QTableWidget
from PyQt6.QtGui import QAction
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        file_menu = self.menuBar().addMenu("&File")
        help_menu = self.menuBar().addMenu("&About")

        file_action = QAction("Add Table", self)
        file_menu.addAction(file_action)

        help_action = QAction("About", self)
        help_menu.addAction(help_action)
        help_action.setMenuRole(QAction.MenuRole.NoRole)

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(("Name", "ID", "Course", "Mobile"))
        self.setCentralWidget(self.table)

    # def load_tabledata(self):

app= QApplication(sys.argv)
app1= MainWindow()
app1.show()
sys.exit(app.exec())/
