import sys
import sqlite3

from PyQt6.QtWidgets import *
from PyQt6 import uic

class MAIN(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.tableWidget.setColumnWidth(0, 40)
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setColumnWidth(2, 180)
        self.tableWidget.setColumnWidth(3, 150)
        self.tableWidget.setColumnWidth(4, 400)
        self.tableWidget.setColumnWidth(5, 40)
        self.tableWidget.setColumnWidth(6, 45)
        self.tableWidget.setHorizontalHeaderLabels(['ID', 'название сорта', 'степень обжарки', 'молотый/в зернах', 'описание вкуса', 'цена', 'объем'])
        self.show_info()

    def show_info(self):
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
            self.tableWidget.setItem(tablerow, 0, QTableWidgetItem(row[0]))
            self.tableWidget.setItem(tablerow, 1, QTableWidgetItem(row[1]))
            self.tableWidget.setItem(tablerow, 2, QTableWidgetItem(row[2]))
            self.tableWidget.setItem(tablerow, 3, QTableWidgetItem(row[3]))
            self.tableWidget.setItem(tablerow, 4, QTableWidgetItem(row[4]))
            self.tableWidget.setItem(tablerow, 5, QTableWidgetItem(row[5]))
            self.tableWidget.setItem(tablerow, 6, QTableWidgetItem(row[6]))
            tablerow += 1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MAIN()
    ex.show()
    sys.exit(app.exec())