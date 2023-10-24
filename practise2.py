from PyQt6.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QLabel,\
    QPushButton, QApplication, QDialog, QVBoxLayout, QLineEdit, QComboBox, QToolBar, QStatusBar, QGridLayout, QMessageBox

from PyQt6.QtGui import QAction, QIcon
import sys
import sqlite3
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Database Management")
        self.setMinimumWidth(400)
        self.setMinimumHeight(300)


        window= QMainWindow()
        file_menu= window.menuBar().addMenu("&File")
        help_menu= window.menuBar().addMenu("&About")
        edit_menu= window.menuBar().addMenu("&Edit")

        self.setMenuWidget(window)

        file_action = QAction(QIcon("icons/add.png"), "Add Student", self)
        file_menu.addAction(file_action)
        file_menu.triggered.connect(self.add_newrec)
        help_action = QAction("Help", self)
        help_menu.addAction(help_action)
        edit_action= QAction(QIcon("icons/search.png"), "Search", self)
        edit_menu.addAction(edit_action)
        edit_menu.triggered.connect(self.searchwindow)

        tool = QToolBar()
        tool.setMovable(True)
        tool.addAction(file_action)
        tool.addAction(edit_action)
        self.addToolBar(tool)

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(("ID", "Name", "Course", "Mobile"))
        self.table.verticalHeader().setVisible(False)
        self.setCentralWidget(self.table)

        self.status = QStatusBar()
        self.setStatusBar(self.status)
        self.table.cellClicked.connect(self.cell_clicked)

    def cell_clicked(self):
        edit = QPushButton("Edit Record")
        edit.clicked.connect(self.edit)
        delete = QPushButton("Delete Record")
        delete.clicked.connect(self.delete)
        children = self.findChildren(QPushButton)
        if children:
            for n in children:
                self.status.removeWidget(n)
        print(children)
        self.status.addWidget(edit)
        self.status.addWidget(delete)

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

    def edit(self):
        edit = EditDialog()
        edit.exec()

    def delete(self):
        delete = DeleteDialog()
        delete.exec()

class EditDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Update Student")
        self.setFixedHeight(300)
        self.setFixedWidth(300)
        box = QVBoxLayout()

        id = app1.table.currentRow()
        self.id= app1.table.item(id, 0).text()

        index = app1.table.currentRow()
        print(index)
        name = app1.table.item(index,1).text()
        self.name = QLineEdit(name)

        self.course = QComboBox()
        lis = ["Nuclear Chemistry", "Computer Science", "Physics",
               "Mathematics", "Botony"]
        course = app1.table.item(index, 2).text()
        self.course.addItems(lis)
        self.course.setCurrentText(course)

        mobile = app1.table.item(index, 3).text()
        self.mobile = QLineEdit(mobile)


        update = QPushButton("Update")
        update.clicked.connect(self.update_stu)

        box.addWidget(self.name)
        box.addWidget(self.course)
        box.addWidget(self.mobile)
        box.addWidget(update)

        self.setLayout(box)

    def update_stu(self):
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        cursor.execute("UPDATE records SET Name=?, Course = ?, Mobile =? WHERE ID = ?", (self.name.text(),
                                                                          self.course.itemText(self.course.currentIndex()),
                                                                          self.mobile.text(),
                                                                          self.id))
        connection.commit()
        cursor.close()
        connection.close()
        app1.load_date()

class DeleteDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Delete Record")

        grid =  QGridLayout()
        label = QLabel("Are you sure you want to delete?")
        yes = QPushButton("Yes")
        no = QPushButton("No")
        yes.clicked.connect(self.delet)

        grid.addWidget(label, 0, 0, 1, 2)
        grid.addWidget(yes, 1, 0)
        grid.addWidget(no, 1, 1)

        self.setLayout(grid)

    def delet(self):
        index= app1.table.currentRow()
        id= app1.table.item(index, 0).text()
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        cursor.execute("DELETE FROM records WHERE ID=?", (id,))
        connection.commit()
        cursor.close()
        connection.close()
        app1.load_date()
        self.close()

        message = QMessageBox()
        message.setWindowTitle("Success!")
        message.setText("The message was successfully deleted")
        message.exec()




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