import sys
from PyQt5.QtWidgets import *
import pymysql
import pandas as pd
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

page1 = uic.loadUiType("openCV.ui")[0]

class MainWindow(QMainWindow, page1):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # conn = pymysql.connect(host='192.168.0.95', port=3306, user='root', password='1234', db='starbucks',
        #                        charset='utf8')
        # curs = conn.cursor()
        # sql = "select * from openCV"
        #
        # curs.execute(sql)
        # rows = curs.fetchall()
        # print(rows)

        conn.close()

        page1 = uic.loadUiType("openCV.ui")[0]

        #버튼
        self.btn.clicked.connect(self.gload)
        self.btn_2.clicked.connect(self.gload2)

        #날짜 시그널
        year1 = self.cb_year1.currentText()
        month1 = self.cb_month.currentText()
        day1 = self.cb_day1.currentText()
        year2 = self.cb_year2.currentText()
        month2 = self.cb_month2.currentText()
        day2 = self.cb_day2.currentText()

        #그래프
        canvas = FigureCanvas()
        vbox = QVBoxLayout(self.widget)
        vbox.addWidget(canvas)
        self.ax = canvas.figure.subplots()

    def gload(self):
        dayday = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17',
                  '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']

        money = [1213, 2546, 3787, 4587, 1667, 7797, 5144, 8796]

        BabyDataset = list(zip(dayday, money))

        df = pd.DataFrame(data=BabyDataset, columns=['day', 'money'])

        y = df['money']
        x = df['day']

        self.ax.clear()
        self.ax.plot(x, y)
        self.ax.figure.canvas.draw()

    def gload2(self):
        dayday = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17',
                  '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']

        money = [4555, 5146, 8787, 1587, 4567, 797, 1144, 3796, 4567, 6666, 7777, 1111, 2222, 3333]

        BabyDataset = list(zip(dayday, money))

        df = pd.DataFrame(data=BabyDataset, columns=['day', 'money'])

        y = df['money']
        x = df['day']

        self.ax.clear()
        self.ax.plot(x, y)
        self.ax.figure.canvas.draw()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MainWindow()
    myWindow.show()
    app.exec_()
