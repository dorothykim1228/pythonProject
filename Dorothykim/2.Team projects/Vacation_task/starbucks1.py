import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic



form_class = uic.loadUiType("starbuck1.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.tabWidget.setStyleSheet("QTabBar:tab {"" height: 500px; width: 500px;"" }")
        self.setWindowTitle("StarBucks")
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()

