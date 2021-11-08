import sys, re, webbrowser, sqlite3, pymysql
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from datetime import *
from random import *
page0 = "star0.ui"
page1 = "star1.ui"
page2 = "star2.ui"
page3 = "star3.ui"
page4 = "star4.ui"
page5 = "star_kiosk.ui"
page6 = "star5.ui"


connection = pymysql.connect \
    (host='192.168.0.54', port=3306, user='root', password='1234', db='headquarter', charset='utf8')
# 커서 가져오기(연결할 db와 상호작용하기 위해서 cursor 객채생성 필요)
cursor = connection.cursor()

conn = sqlite3.connect("STARBUCKS2.db", isolation_level=None)
cur = conn.cursor()

class greater:
    my_acoount_info = []
    total_money = 0
    menu_list = [] # 메뉴 가격 리스트
    price_list = []

class variable:
    total_money = 0
    # 메뉴 가격 리스트
    menu_list = []
    price_list = []
    my_bsinfo = []

class Simplify:
    def images(self):

        #이미지
        self.reward_btn.setStyleSheet('image:url(이미지/reward.jpg);')
        self.summer_btn.setStyleSheet('image:url(이미지/123.jpg);')

        # 커피 이미지
        self.Btn_1.setStyleSheet('image:url(이미지/음료/에스프레소/아이스 카페 라떼.jpg);')
        self.Btn_2.setStyleSheet('image:url(이미지/음료/에스프레소/아이스 카페 모카.jpg);')
        self.Btn_3.setStyleSheet('image:url(이미지/음료/에스프레소/아이스 카푸치노.jpg);')
        self.Btn_4.setStyleSheet('image:url(이미지/음료/에스프레소/아이스 카페 아메리카노.jpg);')
        self.Btn_5.setStyleSheet('image:url(이미지/음료/에스프레소/아이스 라벤더 카페 브레베.jpg);')
        self.Btn_6.setStyleSheet('image:url(이미지/음료/에스프레소/럼 샷 코르타도.jpg);')
        self.Btn_7.setStyleSheet('image:url(이미지/음료/에스프레소/사케라또 비얀코 오버 아이스.jpg);')
        self.Btn_8.setStyleSheet('image:url(이미지/음료/에스프레소/아이스 바닐라 빈 라떼.jpg);')
        self.Btn_9.setStyleSheet('image:url(이미지/음료/에스프레소/아이스 카라멜 마키아또.jpg);')
        self.Btn_10.setStyleSheet('image:url(이미지/음료/에스프레소/아이스 카페 라떼.jpg);')
        self.Btn_11.setStyleSheet('image:url(이미지/음료/에스프레소/아이스 카페 모카.jpg);')
        self.Btn_12.setStyleSheet('image:url(이미지/음료/에스프레소/아이스 카페 아메리카노.jpg);')
        self.Btn_13.setStyleSheet('image:url(이미지/음료/에스프레소/아이스 카푸치노.jpg);')
        self.Btn_14.setStyleSheet('image:url(이미지/음료/에스프레소/에스프레소.jpg);')
        self.Btn_15.setStyleSheet('image:url(이미지/음료/콜드 브루/나이트로 바닐라 크림.jpg);')
        self.Btn_16.setStyleSheet('image:url(이미지/음료/콜드 브루/나이트로 콜드 브루.jpg);')
        self.Btn_17.setStyleSheet('image:url(이미지/음료/콜드 브루/돌체 콜드 브루.jpg);')
        self.Btn_18.setStyleSheet('image:url(이미지/음료/콜드 브루/바닐라 크림 콜드 브루.jpg);')
        self.Btn_19.setStyleSheet('image:url(이미지/음료/콜드 브루/벨벳 다크 모카 나이트로.jpg);')
        self.Btn_20.setStyleSheet('image:url(이미지/음료/콜드 브루/제주 비자림 콜드 브루.jpg);')
        self.Btn_21.setStyleSheet('image:url(이미지/음료/콜드 브루/콜드 브루 몰트.jpg);')
        self.Btn_22.setStyleSheet('image:url(이미지/음료/콜드 브루/콜드 브루 오트 라떼.jpg);')
        self.Btn_23.setStyleSheet('image:url(이미지/음료/콜드 브루/콜드 브루 플로트.jpg);')
        self.Btn_24.setStyleSheet('image:url(이미지/음료/콜드 브루/콜드 브루.jpg);')
        self.Btn_25.setStyleSheet('image:url(이미지/음료/콜드 브루/프렌치 애플 타르트 나이트로.jpg);')
        self.Btn_26.setStyleSheet('image:url(이미지/푸드/샌드위치/B.E.L.T. 샌드위치.jpg);')
        self.Btn_27.setStyleSheet('image:url(이미지/푸드/샌드위치/단호박 에그 샌드위치.jpg);')
        self.Btn_28.setStyleSheet('image:url(이미지/푸드/샌드위치/돌코롬 쫍지롱 와플 샌드.jpg);')
        self.Btn_29.setStyleSheet('image:url(이미지/푸드/샌드위치/브렉퍼스트 잉글리쉬 머핀.jpg);')
        self.Btn_30.setStyleSheet('image:url(이미지/푸드/샌드위치/에그에그 샌드위치.jpg);')
        self.Btn_31.setStyleSheet('image:url(이미지/푸드/샌드위치/올라 쿠바노 샌드위치.jpg);')
        self.Btn_32.setStyleSheet('image:url(이미지/푸드/샌드위치/제주 녹차 베이컨 치즈 베이글.jpg);')
        self.Btn_33.setStyleSheet('image:url(이미지/푸드/샌드위치/제주 흑돼지 아보카도 샌드위치.jpg);')
        self.Btn_34.setStyleSheet('image:url(이미지/푸드/샌드위치/크랜베리 치킨 치즈 샌드위치.jpg);')
        self.Btn_35.setStyleSheet('image:url(이미지/푸드/샌드위치/포크 커틀릿 샌드위치.jpg);')
        self.Btn_36.setStyleSheet('image:url(이미지/푸드/샌드위치/플랜트 햄 루꼴라 샌드위치.jpg);')
        self.Btn_37.setStyleSheet('image:url(이미지/푸드/케이크/(제주)제주 녹차 생크림 롤.jpg);')
        self.Btn_38.setStyleSheet('image:url(이미지/푸드/케이크/당근 현무암 케이크.jpg);')
        self.Btn_39.setStyleSheet('image:url(이미지/푸드/케이크/라즈베리 쇼콜라.jpg);')
        self.Btn_40.setStyleSheet('image:url(이미지/푸드/케이크/마스카포네 티라미수 케이크.jpg);')
        self.Btn_41.setStyleSheet('image:url(이미지/푸드/케이크/몽블랑 치즈 케이크.jpg);')
        self.Btn_42.setStyleSheet('image:url(이미지/푸드/케이크/밀당 에그 타르트.jpg);')
        self.Btn_43.setStyleSheet('image:url(이미지/푸드/케이크/번트 치즈 케이크.jpg);')
        self.Btn_44.setStyleSheet('image:url(이미지/푸드/케이크/부드러운 생크림 카스텔라.jpg);')
        self.Btn_45.setStyleSheet('image:url(이미지/푸드/케이크/부드러운 티라미수 롤.jpg);')
        self.Btn_46.setStyleSheet('image:url(이미지/푸드/케이크/블루베리 쿠키 치즈 케이크.jpg);')
        self.Btn_47.setStyleSheet('image:url(이미지/푸드/케이크/상큼한 샤인 머스캣 스윗박스.jpg);')
        self.Btn_48.setStyleSheet('image:url(이미지/푸드/케이크/호두 당근 케이크.jpg);')
        #결제 사진
        self.label_pay.setStyleSheet('image:url(이미지/결제.jpg);')
        self.label_close.setStyleSheet('image:url(이미지/주문완료.jpg);')

#################################################################################################################
# page0
###################################################################################################################

class Page0(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None, Qt.WindowStaysOnTopHint)
        uic.loadUi(page0, self)
        self.register_pb.clicked.connect(self.register)
    def register(self):
        # 접속
        connection = pymysql.connect \
        (host='192.168.0.54', port=3306, user='root', password='1234', db='headquarter', charset='utf8')
        # 커서 가져오기(연결할 db와 상호작용하기 위해서 cursor 객채생성 필요)
        cursor = connection.cursor()

        # 본사 정보
        qy = """
                    select bsname from bsinfo  #본사 정보
                    """
        # sql문 실행
        cursor.execute(qy)
        iy = cursor.fetchall()
        bsname = list(map(lambda x: x[0], iy))
        # print(bsname, type(bsname))
        # 지사 정보 가져올때
        cur.execute("SELECT * FROM bsinfo")
        result = cur.fetchone()
        # print(result)

        for i in result:
            variable.my_bsinfo.append(i)
        # print(variable.my_bsinfo)

        if variable.my_bsinfo[1] in bsname:
            a = 'A'
            qy = """
                        update bsinfo set APPROVE = %s where bsname = %s
                        """
            cursor.execute(qy, (a, variable.my_bsinfo[1]))
            connection.commit()
            connection.close()

            self.sh = Page1()
            self.sh.show()
            self.close()
        else:
            QMessageBox.information(self, 'Starbucks', '지점등록을 해주세요')


########################################################################################################################
# page 1
########################################################################################################################
class Page1(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None, Qt.WindowStaysOnTopHint)
        uic.loadUi(page1, self)
        self.pb_Login.clicked.connect(self.login)
        self.pb_Join.clicked.connect(self.join)
        self.pb_Admin.clicked.connect(self.admin)
        self.label_star.setStyleSheet('image:url(이미지/12345.jpg);')



    # 매출 정보
    def admin(self):
        try:
            qy1 = "select * from bsinfo"
            cur.execute(qy1)
            my_info = cur.fetchone()

            qy2 = """
            SELECT menu, price, sum(quantity) from ORDERDETAILE
            where paydate = STRFTIME('%Y-%m-%d', 'now', 'localtime')
            GROUP by MENU order by sum(quantity) desc limit 1
            """
            cur.execute(qy2)
            result1 = cur.fetchone()
            # print(result1)
            hq = list(result1)
            # print(hq)
            # print(type(hq[1]))
            # print(type(hq[2]))
            pxq = int(hq[1]) * hq[2]
            # print(pxq)
            # print(type(pxq))
            intn = int(hq[1])
            qy3 = "select sum(total) from orderdetaile where paydate = STRFTIME('%Y-%m-%d', 'now', 'localtime')"
            cur.execute(qy3)
            result2 = cur.fetchone()
            # print(result2)
            # print(type(result2[0]))
            time = datetime.now()
            ddate = time.strftime("%Y-%m-%d")

            connection = pymysql.connect \
                (host='192.168.0.54', port=3306, user='root', password='1234', db='headquarter', charset='utf8')
            # 커서 가져오기(연결할 db와 상호작용하기 위해서 cursor 객채생성 필요)
            cursor = connection.cursor()
            qy4 = "insert into dsinfo (country, bsname, menu, price, quantity, agg, sales, ddate) values (%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(qy4, (my_info[0], my_info[1], hq[0], intn, hq[2], pxq, result2[0], ddate))
            connection.commit()
            connection.close()
        except Exception as e:
            print(e)
            pass

    def join(self):
        self.Pg = Page2()
        self.Pg.show()
        self.close()

    def login(self):
        conn = sqlite3.connect("STARBUCKS2.db", isolation_level=None)
        cur = conn.cursor()
        cur.execute("SELECT * FROM MEMBERSHIP WHERE ID = '{}'".format(self.lineEdit_id.text()))
        result = cur.fetchone()
        print(result)
        if result == None:
            QMessageBox.critical(self, " ", "계정 혹은 비밀번호가 일치하지 않습니다.")
        else:
            for row in result:
                print(row)
                greater.my_acoount_info.append(row)
                print(greater.my_acoount_info)

            if greater.my_acoount_info[1] == self.lineEdit_pw.text():
                self.page3 = Page3()
                self.page3.show()
                self.close()
            else:
                greater.my_acoount_info.clear()
                QMessageBox.information(self, " ", "계정 혹은 비밀번호가 일치하지 않습니다.", QMessageBox.Ok)


########################################################################################################################
# page 2 회원가입
########################################################################################################################

class Page2(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None, Qt.WindowStaysOnTopHint)
        uic.loadUi(page2, self)

        self.next_check = []
        self.pb_check.clicked.connect(self.click)
        self.pb_next.clicked.connect(self.next)
        self.pb_cancel.clicked.connect(self.cancel)
        self.lineEdit.textEdited.connect(self.text_edited) # 아이디 입력란 수정시 시그널
        self.label_star.setStyleSheet('image:url(이미지/12345.jpg);')


    # 중복 체크
    def click(self):
        conn = sqlite3.connect("STARBUCKS2.db", isolation_level=None)
        cur = conn.cursor()
        cur.execute("SELECT ID FROM MEMBERSHIP WHERE ID = '{}'".format(self.lineEdit.text()))
        result = cur.fetchall()
        id_list = []
        for row in result:
            id_list.append(row)

        if self.lineEdit.text() in id_list:
            QMessageBox.critical(self, " ", "중복된 아이디입니다.")
        else:
            check = QMessageBox.information(self, " ", "사용 가능한 아이디입니다.")
            if check == QMessageBox.Ok:
                print(111111)
                self.next_check.append("yes")
                print(self.next_check)

    def text_edited(self):
        self.next_check.clear()
        print(self.next_check)

    def next(self):
        if "yes" not in self.next_check:
            QMessageBox.information(self, " ", "아이디 중복 확인을 해주세요.")
        elif len(self.lineEdit.text()) < 5:
            QMessageBox.critical(self, " ", "아이디를 최소 5 이상 입력해주세요.")
        elif len(self.lineEdit_2.text()) < 8:
            QMessageBox.critical(self, " ", "비밀번호를 최소 8 이상 입력해주세요.")
        elif len(self.lineEdit_3.text()) < 1:
            QMessageBox.critical(self, " ", "닉네임를 최소 한글자 이상 입력해주세요.")
        else:
            id = self.lineEdit.text()
            pw = self.lineEdit_2.text()
            nick = self.lineEdit_3.text()
            conn = sqlite3.connect("STARBUCKS2.db", isolation_level=None)
            cur = conn.cursor()
            cur.execute("insert into MEMBERSHIP values(?,?,?)", (id, pw, nick))
            self.page = Page1()
            self.page.show()
            self.close()

    def cancel(self):
        Pg.show()
        self.close()


########################################################################################################################
# page 3
########################################################################################################################
class Page3(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None, Qt.WindowStaysOnTopHint)
        uic.loadUi(page3, self)

        self.pb_membership.clicked.connect(self.membership)
        self.pb_home.clicked.connect(self.home)
        self.pb_remove.clicked.connect(self.remove)
        self.pb_check.clicked.connect(self.check)
        self.label_confirm.setText("{} 님, Welcome to Starbucks".format(greater.my_acoount_info[0]))

    def check(self):
        year = re.findall(r'\d+', self.comboBox_year.currentText())
        year = year[0]
        # print(year)
        month = re.findall(r'\d+', self.comboBox_month.currentText())
        month = month[0]
        # print(month)
        day = re.findall(r'\d+', self.comboBox_day.currentText())
        day = day[0]
        # print(day)
        try:
            conn = sqlite3.connect("STARBUCKS2.db", isolation_level=None)
            cur = conn.cursor()
            qy1 = """
            SELECT MAX(NUMBER) FROM ORDERDETAILE WHERE ID = '{}' AND PAYDATE = '{}.{}.{}'
            """
            cur.execute(qy1.format(greater.my_acoount_info[0], year, month, day))
            number = cur.fetchone()  # 예시 [(5, 3), (3, 4), (1, 2)] // cur.fetchone() # (5, 3)
            print(number[0])
            if number[0] == None:
                count = None
                pass
            else:
                count = int(number[0]) + 1
            print(count)
        except Exception as e:
            print(e)
            pass
        try:
            for i in range(count):
                qy2 = """
                SELECT TOTAL, PAYDATE, PAYTIME FROM ORDERDETAILE WHERE ID = '{}' AND PAYDATE = '{}.{}.{}'
                """
                cur.execute(qy2.format(greater.my_acoount_info[0], year, month, day))
                result_1 = cur.fetchall()
                print(result_1)
                total, date, time = zip(*result_1)
                list_total = list(dict.fromkeys(total))
                list_date = list(dict.fromkeys(date))
                list_time = list(dict.fromkeys(time))
                print(list_total)
                print(list_date)
                print(list_time)
                self.textBrowser.append('{} ★ {}'.format(list_date[0], list_time[i]))

                qy3 = """
                SELECT MENU, PRICE FROM ORDERDETAILE WHERE ID = '{}' AND PAYDATE = '{}.{}.{}' and NUMBER = '{}'
                """
                cur.execute(qy3.format(greater.my_acoount_info[0], year, month, day, i))
                result_2 = cur.fetchall()
                print(result_2)
                for j in range(len(result_2)):
                    menu = result_2[j]
                    self.textBrowser.append('{} ￦{}'.format(menu[0], menu[1]))
                self.textBrowser.append('TOTAL ￦{}'.format(list_total[i]))
                self.textBrowser.append("")
        except Exception as e:
            print(e)
            pass

    def remove(self):
        remove = QMessageBox.information(self, " ", "{} 님 정말 탈퇴하시겠습니까?".format(greater.my_acoount_info[0]),
                                         QMessageBox.No | QMessageBox.Yes, QMessageBox.No)
        if remove == QMessageBox.Yes:
            conn = sqlite3.connect("STARBUCKS2.db", isolation_level=None)
            cur = conn.cursor()
            cur.execute("delete FROM MEMBERSHIP WHERE ID = '{}'".format(greater.my_acoount_info[0]))
            greater.my_acoount_info.clear()
            Pg.show()
            self.close()
        else:
            pass

    def home(self):
        self.Pg = Page5()
        self.Pg.show()
        self.close()
    def membership(self):
        self.dorothy = Page4()
        self.dorothy.show()
        self.close()
    def display(self):
        self.show()


########################################################################################################################
# page 4
########################################################################################################################
class Page4(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None, Qt.WindowStaysOnTopHint)
        uic.loadUi(page4, self)

        self.pb_cancel.clicked.connect(self.cancel)
        self.pb_confirm.clicked.connect(self.confirm)
        self.label.setText(greater.my_acoount_info[0])

    def cancel(self):
        self.Pg = Page3()
        self.Pg.show()
        self.close()

    def confirm(self):
        if greater.my_acoount_info[1] == self.lineEdit_mi1.text():
            conn = sqlite3.connect("STARBUCKS2.db", isolation_level=None)
            cur = conn.cursor()
            pw = self.lineEdit_mi2.text()
            nick = self.lineEdit_mi3.text()
            cur.execute("UPDATE MEMBERSHIP SET (PASSWORD, NICKNAME) = ('{}', '{}') where ID = '{}'".format(pw, nick,
                                                                                                           greater.my_acoount_info[
                                                                                                               0]))
            greater.my_acoount_info[1] = pw
            greater.my_acoount_info[2] = nick
            print(greater.my_acoount_info)
            check = QMessageBox.information(self, " ", "회원정보가 변경되었습니다.", QMessageBox.Ok)
            if check == QMessageBox.Ok:
                self.dorothy = Page3()
                self.dorothy.show()
                self.close()


########################################################################################################################
# page 5
########################################################################################################################



class Page5(QMainWindow, Simplify):
    def __init__(self):
        QMainWindow.__init__(self, None, Qt.WindowStaysOnTopHint)
        Simplify.__init__(self)
        uic.loadUi(page5, self)
        Simplify.images(self)
        self.setWindowTitle('Starbucks')
        self.setGeometry(400, 500, 761, 789)

        # 버튼에 링크 추가하기
        self.new_btn.clicked.connect(lambda: webbrowser.open('https://www.starbucks.co.kr/whats_new/index.do'))
        self.summer_btn.clicked.connect(
            lambda: webbrowser.open('https://www.starbucks.co.kr/index.do'))
        self.reward_btn.clicked.connect(
            lambda: webbrowser.open('https://www.starbucks.co.kr/msr/msreward/level_benefit.do'))

        ###next 버튼 실행시 페이지 전환
        self.Btn_pay_next1.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_pay2))
        self.Btn_pay_next2.clicked.connect(self.pay_succeed)

        # 첫 페이지 설정
        ### 홈
        self.tabWidget.setCurrentWidget(self.tab_home)
        ### 음료
        self.tabWidget_drink_and_food.setCurrentWidget(self.tab_drink)
        ### 음료 & 푸드 new
        self.tool_drink.setCurrentWidget(self.page_drink_new)
        self.tool_food.setCurrentWidget(self.page_food_new)
        ### 결제
        self.stackedWidget.setCurrentWidget(self.page_pay1)

        # 결제 창 리셋 시그널 준 부분
        self.tabWidget.currentChanged.connect(self.reset)

        ##버튼 1-58번
        self.Btn_1.clicked.connect(lambda: self.tabWidget.setCurrentWidget(self.tab_pay))
        self.Btn_2.clicked.connect(lambda: self.tabWidget.setCurrentWidget(self.tab_pay))
        self.Btn_3.clicked.connect(lambda: self.tabWidget.setCurrentWidget(self.tab_pay))
        self.Btn_4.clicked.connect(lambda: self.tabWidget.setCurrentWidget(self.tab_pay))

        self.Btn_1.clicked.connect(
            lambda state, button=self.Btn_1, price=4600, menu="아이스 카페 라떼": self.add_menu(state, button, price, menu))
        self.Btn_2.clicked.connect(
            lambda state, button=self.Btn_2, price=5100, menu="아이스 카페 모카": self.add_menu(state, button, price, menu))
        self.Btn_3.clicked.connect(
            lambda state, button=self.Btn_3, price=4600, menu="아이스 카푸치노": self.add_menu(state, button, price, menu))
        self.Btn_4.clicked.connect(
            lambda state, button=self.Btn_4, price=4100, menu="아이스 카페 아메리카노": self.add_menu(state, button, price, menu))
        self.Btn_5.clicked.connect(
            lambda state, button=self.Btn_5, price=7500, menu="아이스 라벤더 카페 브레베": self.add_menu(state, button, price, menu))
        self.Btn_6.clicked.connect(
            lambda state, button=self.Btn_6, price=7500, menu="럼 샷 코르타도": self.add_menu(state, button, price, menu))
        self.Btn_7.clicked.connect(
            lambda state, button=self.Btn_7, price=7500, menu="사케라또 비얀코 오버 아이스": self.add_menu(state, button, price, menu))
        self.Btn_8.clicked.connect(
            lambda state, button=self.Btn_8, price=7000, menu="아이스 바닐라 빈 라떼": self.add_menu(state, button, price, menu))
        self.Btn_9.clicked.connect(
            lambda state, button=self.Btn_9, price=5600, menu="아이스 카라멜 마끼아또": self.add_menu(state, button, price, menu))
        self.Btn_10.clicked.connect(
            lambda state, button=self.Btn_10, price=4600, menu="아이스 카페 라떼": self.add_menu(state, button, price, menu))
        self.Btn_11.clicked.connect(
            lambda state, button=self.Btn_11, price=5100, menu="아이스 카페 모카": self.add_menu(state, button, price, menu))
        self.Btn_12.clicked.connect(
            lambda state, button=self.Btn_12, price=4100, menu="아이스 아메리카노": self.add_menu(state, button, price, menu))
        self.Btn_13.clicked.connect(
            lambda state, button=self.Btn_13, price=4600, menu="아이스 카푸치노": self.add_menu(state, button, price, menu))
        self.Btn_14.clicked.connect(
            lambda state, button=self.Btn_14, price=3600, menu="에스프레소": self.add_menu(state, button, price, menu))
        self.Btn_15.clicked.connect(
            lambda state, button=self.Btn_15, price=5600, menu="나이트로 바닐라 크림": self.add_menu(state, button, price, menu))
        self.Btn_16.clicked.connect(
            lambda state, button=self.Btn_16, price=5800, menu="나이트로 콜드 브루": self.add_menu(state, button, price, menu))
        self.Btn_17.clicked.connect(
            lambda state, button=self.Btn_17, price=5800, menu="돌체 콜드 브루": self.add_menu(state, button, price, menu))
        self.Btn_18.clicked.connect(
            lambda state, button=self.Btn_18, price=5500, menu="바닐라 크림 콜드 브루": self.add_menu(state, button, price, menu))
        self.Btn_19.clicked.connect(
            lambda state, button=self.Btn_19, price=8500, menu="벨벳 다크 모카 나이트로": self.add_menu(state, button, price, menu))
        self.Btn_20.clicked.connect(
            lambda state, button=self.Btn_20, price=6800, menu="제주 비자림 콜드 브루": self.add_menu(state, button, price, menu))
        self.Btn_21.clicked.connect(
            lambda state, button=self.Btn_21, price=8500, menu="콜드 브루 몰트": self.add_menu(state, button, price, menu))
        self.Btn_22.clicked.connect(
            lambda state, button=self.Btn_22, price=5600, menu="콜드 브루 오트 라떼": self.add_menu(state, button, price, menu))
        self.Btn_23.clicked.connect(
            lambda state, button=self.Btn_23, price=8000, menu="콜드 브루 플로트": self.add_menu(state, button, price, menu))
        self.Btn_24.clicked.connect(
            lambda state, button=self.Btn_24, price=4500, menu="콜드 브루": self.add_menu(state, button, price, menu))
        self.Btn_25.clicked.connect(
            lambda state, button=self.Btn_25, price=8500, menu="프렌치 애플 타르트 나이트로": self.add_menu(state, button, price, menu))
        self.Btn_26.clicked.connect(
            lambda state, button=self.Btn_26, price=5900, menu="B.E.L.T 샌드위치": self.add_menu(state, button, price, menu))
        self.Btn_27.clicked.connect(
            lambda state, button=self.Btn_27, price=4900, menu="단호박 에그 샌드위치": self.add_menu(state, button, price, menu))
        self.Btn_28.clicked.connect(
            lambda state, button=self.Btn_28, price=7800, menu="돌코롬 쫍지롱 와플 샌드": self.add_menu(state, button, price, menu))
        self.Btn_29.clicked.connect(
            lambda state, button=self.Btn_29, price=4200, menu="블렉퍼스트 잉글리쉬 머핀": self.add_menu(state, button, price, menu))
        self.Btn_30.clicked.connect(
            lambda state, button=self.Btn_30, price=4400, menu="에그에그 샌드위치": self.add_menu(state, button, price, menu))
        self.Btn_31.clicked.connect(
            lambda state, button=self.Btn_31, price=6300, menu="올라 쿠바노 샌드위치": self.add_menu(state, button, price, menu))
        self.Btn_32.clicked.connect(
            lambda state, button=self.Btn_32, price=6200, menu="제주 녹차 베이컨 치즈 베이글": self.add_menu(state, button, price, menu))
        self.Btn_33.clicked.connect(
            lambda state, button=self.Btn_33, price=7200, menu="제주 흑돼지 아보카도 샌드위치": self.add_menu(state, button, price, menu))
        self.Btn_34.clicked.connect(
            lambda state, button=self.Btn_34, price=4500, menu="크랜베리 치킨 치즈 샌드위치": self.add_menu(state, button, price, menu))
        self.Btn_35.clicked.connect(
            lambda state, button=self.Btn_35, price=5900, menu="포크 커틀릿 샌드위치": self.add_menu(state, button, price, menu))
        self.Btn_36.clicked.connect(
            lambda state, button=self.Btn_36, price=5400, menu="플랜트 햄&루꼴라 샌드위치": self.add_menu(state, button, price, menu))
        self.Btn_37.clicked.connect(
            lambda state, button=self.Btn_37, price=7500, menu="(제주)제주 녹차 생크림 롤": self.add_menu(state, button, price, menu))
        self.Btn_38.clicked.connect(
            lambda state, button=self.Btn_38, price=6800, menu="당근 현무암 케이크": self.add_menu(state, button, price, menu))
        self.Btn_39.clicked.connect(
            lambda state, button=self.Btn_39, price=5900, menu="라즈베리 쇼콜라": self.add_menu(state, button, price, menu))
        self.Btn_40.clicked.connect(
            lambda state, button=self.Btn_40, price=5900, menu="마스카포네 티라미수 케이크": self.add_menu(state, button, price, menu))
        self.Btn_41.clicked.connect(
            lambda state, button=self.Btn_41, price=6900, menu="몽블랑 치즈 케이크": self.add_menu(state, button, price, menu))
        self.Btn_42.clicked.connect(
            lambda state, button=self.Btn_42, price=4200, menu="밀당 에그 타르트": self.add_menu(state, button, price, menu))
        self.Btn_43.clicked.connect(
            lambda state, button=self.Btn_43, price=6900, menu="번트 치즈 케이크": self.add_menu(state, button, price, menu))
        self.Btn_44.clicked.connect(
            lambda state, button=self.Btn_44, price=4500, menu="부드러운 생크림 카스텔라": self.add_menu(state, button, price, menu))
        self.Btn_45.clicked.connect(
            lambda state, button=self.Btn_45, price=4500, menu="부드러운 티라미수 롤": self.add_menu(state, button, price, menu))
        self.Btn_46.clicked.connect(
            lambda state, button=self.Btn_46, price=6900, menu="블루베리 쿠키 치즈 케이크": self.add_menu(state, button, price, menu))
        self.Btn_47.clicked.connect(
            lambda state, button=self.Btn_47, price=7900, menu="상큼한 샤인 머스캣 스윗박스": self.add_menu(state, button, price, menu))
        self.Btn_48.clicked.connect(
            lambda state, button=self.Btn_48, price=6500, menu="호두 당근 케이크": self.add_menu(state, button, price, menu))


        self.Btn_cancel1.clicked.connect(self.cancel_menu) # 결제부분 취소
        self.Btn_cancel2.clicked.connect(self.cancel_menu)
        self.Btn_close.clicked.connect(self.end) #결제 마지막

    # 테이블에 메뉴 상품명, 상품에 대한 가격, 총 주문한 상품의 가격(결제할 총 금액)
    def add_menu(self, state, button, price, menu):
        self.textBrowser.append("{} {}원이 추가 되었습니다.".format(menu, price))
        print(menu)
        variable.total_money += price
        variable.menu_list.append(menu)
        variable.price_list.append(price)
        self.total_money1.setText("{}".format(variable.total_money))
        self.total_money2.setText("{}".format(variable.total_money))
        print(variable.menu_list)
        print(variable.price_list)

    def reset(self):
        self.stackedWidget.setCurrentWidget(self.page_pay1)
    def cancel_menu(self):
        variable.total_money = 0
        variable.menu_list.clear()
        variable.price_list.clear()
        print(variable.menu_list)
        print(variable.price_list)
        self.total_money1.clear()
        self.total_money2.clear()
        self.textBrowser.clear()
        self.tabWidget.setCurrentWidget(self.tab_home)
    def pay_succeed(self):
        try:
            time = datetime.now()
            paydate = time.strftime("%Y-%m-%d")
            paytime = time.strftime("%H:%M:%S")
            conn = sqlite3.connect("STARBUCKS2.db", isolation_level=None)
            cur = conn.cursor()

            qy1 = """
                    SELECT MAX(NUMBER) FROM ORDERDETAILE
                    WHERE ID = '{}' AND PAYDATE = STRFTIME('%Y.%m.%d', 'now', 'localtime')
                    """
            cur.execute(qy1.format(greater.my_acoount_info[0]))
            iy = cur.fetchone()
            print(iy[0])
            if iy[0] == None:
                number = 0
            else:
                number = int(iy[0]) + 1
            # 수량(랜덤으로)
            ri = randint(1, 5)
            for i, value in enumerate(variable.menu_list):  # 메뉴와 가격이 같이 들어가기 때문에 둘 중 하나만 넣어도 됨
                qy = "INSERT INTO ORDERDETAILE VALUES(?,?,?,?,?,?,?,?)"
                cur.execute(qy, (
                    greater.my_acoount_info[0], variable.menu_list[i], variable.price_list[i], variable.total_money,
                    paydate, paytime, number, ri))
            # db테이블에 데이터를 넣을 때 - for문 활용하기(리스트이기 때문에) for i, value in enumerate(variable):
            self.stackedWidget.setCurrentWidget(self.page_pay3)
            variable.total_money = 0
            variable.menu_list.clear()
            variable.price_list.clear()
            self.total_money1.clear()
            self.total_money2.clear()
            self.textBrowser.clear()
        except Exception as e:
            print(e)
            pass

    def end(self):
        self.page3 = Page3()
        self.page3.display()
        self.close()

########################################################################################################################
# page 6
########################################################################################################################

class Page6(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None, Qt.WindowStaysOnTopHint)
        uic.loadUi(page6, self)

        self.pb_back.clicked.connect(self.back)
    def back(self):
        self.sh = Page1()
        self.sh.show()
        self.close()

########################################################################################################################
########################################################################################################################
app = QApplication(sys.argv)
cur.execute("SELECT bsname FROM bsinfo")
result = cur.fetchone()
result = result[0]

qy = """
select APPROVE from bsinfo where bsname = '{}'
"""
    # sql문 실행
cursor.execute(qy.format(result))
approve = cursor.fetchone()
connection.commit()
connection.close()
print(approve)
print(approve[0])
if approve[0] == '0':
    Pg = Page0()
    Pg.show()
    app.exec_()
else:
    # approve = approve[0] #(approve에 a를 가져옴)
    if approve[0] == 'A':
        Pg = Page1()
        Pg.show()
        app.exec_()
    else:
        pass