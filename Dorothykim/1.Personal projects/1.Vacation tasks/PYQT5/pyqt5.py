import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton,QMessageBox
from PyQt5.QtWidgets import QDialog


class Exam(QMainWindow) :##메인윈도우로 해야함




    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.statusBar()##상태표시줄
        self.statusBar().showMessage("Welcome to Starbucks")
        menu = self.menuBar() #메뉴바 생성

        # self.dialog = QDialog()

        btn = QPushButton('음          료\n', self)
        btn.resize(btn.sizeHint())
        btn.move(100, 200)  ##이동사이즈



        btn = QPushButton('푸          드\n', self)
        btn.resize(btn.sizeHint())
        btn.move(300, 200)



        self.setGeometry(300,300,400,500)
        self.setWindowTitle("StarBucks")
        self.show()

class StWidgetForm(QGroupBox):
    """
    위젯 베이스 클래스
    """

    def __init__(self):
        QGroupBox.__init__(self)
        self.box = QBoxLayout(QBoxLayout.TopToBottom)
        self.setLayout(self.box)

class Widget_1(StWidgetForm):
    """
    버튼 그룹
    """

    def __init__(self):
        super(Widget_1, self).__init__()
        self.setTitle("Widget_1")
        self.box.addWidget(QPushButton("Test_1"))
        self.box.addWidget(QPushButton("Test_2"))
        self.box.addWidget(QPushButton("Test_3"))

class Widget_2(StWidgetForm):
    def __init__(self):
        super(Widget_2, self).__init__()
        self.setTitle("Widget_2")
        self.box.addWidget(QTextEdit())

class Widget_3(StWidgetForm):
    def __init__(self):
        super(Widget_3, self).__init__()
        self.setTitle("Widget_3")
        self.box.addWidget(QLabel("Test Label"))

class Form(QWidget):
    def __init__(self):
        QWidget.__init__(self, flags=Qt.Widget)
        self.stk_w = QStackedWidget(self)
        self.init_widget()

    def init_widget(self):
        self.setWindowTitle("Hello World")
        widget_laytout = QBoxLayout(QBoxLayout.LeftToRight)

        group = QGroupBox()
        box = QBoxLayout(QBoxLayout.TopToBottom)
        group.setLayout(box)
        group.setTitle("Buttons")
        widget_laytout.addWidget(group)

        fruits = ["Buttons in GroupBox", "TextBox in GroupBox", "Label in GroupBox", "TextEdit"]
        view = QListView(self)
        model = QStandardItemModel()
        for f in fruits:
            model.appendRow(QStandardItem(f))
        view.setModel(model)
        box.addWidget(view)

        self.stk_w.addWidget(Widget_1())
        self.stk_w.addWidget(Widget_2())
        self.stk_w.addWidget(Widget_3())
        self.stk_w.addWidget(QTextEdit())

        widget_laytout.addWidget(self.stk_w)
        self.setLayout(widget_laytout)

        # 시그널 슬롯 연결
        view.clicked.connect(self.slot_clicked_item)

    @pyqtSlot(QModelIndex)
    def slot_clicked_item(self, QModelIndex):
        self.stk_w.setCurrentIndex(QModelIndex.row())

    def closeEvent(self, QCloseEvent):
        a = QMessageBox.question(self, "종료 확인","종료 하시겠습니까?", QMessageBox.Yes | QMessageBox.No)
        if a == QMessageBox.Yes:
            QCloseEvent.accept()
        else :
            QCloseEvent.ignore()

app = QApplication(sys.argv)
w= Exam()
sys.exit(app.exec())
