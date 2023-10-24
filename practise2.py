from PyQt6.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QLabel,\
    QPushButton, QApplication, QDialog, QVBoxLayout, QLineEdit, QComboBox

from PyQt6.QtGui import QAction
import sys
import sqlite3
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Database Management")
        self.setFixedWidth(400)
        self.setFixedHeight(300)


        window= QMainWindow()
        file_menu= window.menuBar().addMenu("&File")
        help_menu= window.menuBar().addMenu("&About")
        edit_menu= window.menuBar().addMenu("&Edit")

        file_action = QAction("Add Student", self)
        file_menu.addAction(file_action)
        file_menu.triggered.connect(self.add_newrec)
        help_action = QAction("Help", self)
        help_menu.addAction(help_action)
        edit_action= QAction("Search", self)
        edit_menu.addAction(edit_action)
        edit_menu.triggered.connect(self.searchwindow)

        self.setMenuWidget(window)

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(("ID", "Name", "Course", "Mobile"))
        self.table.verticalHeader().setVisible(False)
        self.setCentralWidget(self.table)

    def load_date(self):
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        data = cursor.execute("SELECT * FROM records")
        self.table.setRowCount(0)
        for i, item in enumerate(data):
            self.table.insertRow(i)
            for n, content in enumerate(item):
                self.table.setItem(i, n, QTableWidgetItem(str(content)))

        cursor.close()
        connection.close()

    def add_newrec(self):
        new = AddStudent()
        new.exec()

    def searchwindow(self):
        searchwin = SearchWindow()
        searchwin.exec()


class AddStudent(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Insert Student")
        self.setFixedHeight(300)
        self.setFixedWidth(300)
        box = QVBoxLayout()

        self.name= QLineEdit()
        self.name.setPlaceholderText("Type Name")

        self.course = QComboBox()
        lis= ["Nuclear Chemistry", "Computer Science", "Physics", "Mathematics", "Botony"]
        self.course.addItems(lis)


        self.mobile = QLineEdit()
        self.mobile.setPlaceholderText("Enter mobile number")

        insert = QPushButton("Insert")
        insert.clicked.connect(self.add_stu)


        box.addWidget(self.name)
        box.addWidget(self.course)
        box.addWidget(self.mobile)
        box.addWidget(insert)

        self.setLayout(box)

    def add_stu(self):
        name = self.name.text()
        course= self.course.itemText(self.course.currentIndex())
        mobile= self.mobile.text()
        connection = sqlite3.connect("database.db")
        cursor=  connection.cursor()
        cursor.execute("INSERT INTO records (Name, Course, Mobile) VALUES(?, ?, ?)", (name, course, mobile)) # first () represents the name of the columns as per database
        connection.commit()
        cursor.close()
        connection.close()

        app1.load_date()

class SearchWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Search")

        inp=QVBoxLayout()
        self.inp_label= QLineEdit()
        self.inp_label.setPlaceholderText("Search Bar")

        button= QPushButton("Submit")
        button.clicked.connect(self.search)

        inp.addWidget(self.inp_label)
        inp.addWidget(button)

        self.setLayout(inp)

    def search(self):
        key = self.inp_label.text()
        connection= sqlite3.connect("database.db")
        cursor = connection.cursor()
        data = cursor.execute("SELECT * FROM records")
        content = list(data)
        print(content)
        items = app1.table.findItems(key, Qt.MatchFlag.MatchFixedString)
        for i in items:
            app1.table.item(i.row(),1).setSelected(True)

        cursor.close()
        connection.close()

app= QApplication(sys.argv)
app1 = MainWindow()
app1.show()
app1.load_date()
sys.exit(app.exec())