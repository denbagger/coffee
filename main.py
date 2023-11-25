import sys
import sqlite3

from PyQt6.QtWidgets import *
from PyQt6 import uic


class ADD(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.okButton.clicked.connect(self.ok)


    def ok(self):
        if self.a.text() != '' and self.b.text() != '' and self.c.text() != '' and self.d.text() != '' and self.e.text() != '' and self.f.text() != '':
            connection = sqlite3.connect('coffee.db')
            cursor = connection.cursor()
            cursor.execute(
                f"INSERT INTO coffee(ID, sort_name, roasting_degree, ground_ingrains, taste_decription, price, packing_volume)"
                f" VALUES('{row_count + 1}','{self.a.text()}', '{self.b.text()}', '{self.c.text()}', '{self.d.text()}', '{self.e.text()}', '{self.f.text()}')")
            connection.commit()
            connection.close()
        self.close()
        self.w = MAIN()
        self.w.show()

class EDIT(QMainWindow):
    def __init__(self, index):
        print(index)
        self.index = index
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)
        connection = sqlite3.connect('coffee.db')
        cursor = connection.cursor()
        data = cursor.execute(f"SELECT sort_name, roasting_degree, ground_ingrains, taste_decription, price, packing_volume "
                       f"FROM coffee WHERE ID = ?",
                       (f'{self.index}',)).fetchall()
        self.a.setText(data[0][0])
        self.b.setText(data[0][1])
        self.c.setText(data[0][2])
        self.d.setText(data[0][3])
        self.e.setText(data[0][4])
        self.f.setText(data[0][5])
        self.okButton.clicked.connect(self.ok)

    def ok(self):
        connection = sqlite3.connect('coffee.db')
        cursor = connection.cursor()
        cursor.execute(f"UPDATE coffee SET sort_name = ?, roasting_degree = ?, ground_ingrains = ?, taste_decription = ?, price = ?, packing_volume = ? "
                       f"WHERE ID = ?",
                       (self.a.text(), self.b.text(), self.c.text(), self.d.text(), self.e.text(), self.f.text(), self.index)).fetchall()
        connection.commit()
        connection.close()
        self.close()
        self.w = MAIN()
        self.w.show()


class MAIN(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.flag = False
        self.tableWidget.setColumnWidth(0, 40)
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setColumnWidth(2, 180)
        self.tableWidget.setColumnWidth(3, 150)
        self.tableWidget.setColumnWidth(4, 400)
        self.tableWidget.setColumnWidth(5, 40)
        self.tableWidget.setColumnWidth(6, 45)
        self.tableWidget.setHorizontalHeaderLabels(['ID', 'название сорта', 'степень обжарки', 'молотый/в зернах', 'описание вкуса', 'цена', 'объем'])
        self.show_info()
        self.editButton.clicked.connect(self.edit)
        self.addButton.clicked.connect(self.add)
        self.tableWidget.selectionModel().selectionChanged.connect(self.on_selectionChanged)

    def on_selectionChanged(self, selected):
        global selind
        selind = int('{0}'.format(selected.indexes()[0].row())) + 1
        self.flag = True




    def show_info(self):
        global row_count
        row_count = 0
        connection = sqlite3.connect('coffee.db')
        cur = connection.cursor()
        sqlquery = ('SELECT *'
                    'FROM coffee ORDER BY ID')
        for i in cur.execute(sqlquery):
            row_count += 1
        self.tableWidget.setRowCount(row_count)
        tablerow = 0
        for row in cur.execute(sqlquery):
            self.tableWidget.setItem(tablerow, 0, QTableWidgetItem(str(row[0])))
            self.tableWidget.setItem(tablerow, 1, QTableWidgetItem(row[1]))
            self.tableWidget.setItem(tablerow, 2, QTableWidgetItem(row[2]))
            self.tableWidget.setItem(tablerow, 3, QTableWidgetItem(row[3]))
            self.tableWidget.setItem(tablerow, 4, QTableWidgetItem(row[4]))
            self.tableWidget.setItem(tablerow, 5, QTableWidgetItem(row[5]))
            self.tableWidget.setItem(tablerow, 6, QTableWidgetItem(row[6]))
            tablerow += 1

    def add(self):
        self.add = ADD()
        self.add.show()
        self.close()


    def edit(self):
        if self.flag:
            self.edit = EDIT(selind)
            self.edit.show()
            self.close()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MAIN()
    ex.show()
    sys.exit(app.exec())