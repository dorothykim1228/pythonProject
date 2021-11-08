import sys
import webbrowser
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import QCoreApplication




form_class = uic.loadUiType("star_kiosk.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Starbucks')
        self.setGeometry(800, 800, 800, 800)

        # 버튼에 링크 추가하기
        self.new_btn.clicked.connect(lambda: webbrowser.open('https://www.starbucks.co.kr/whats_new/index.do'))
        self.summer_btn.clicked.connect(
            lambda: webbrowser.open('https://www.starbucks.co.kr/whats_new/campaign_view.do?pro_seq=1864'))
        self.reward_btn.clicked.connect(
            lambda: webbrowser.open('https://www.starbucks.co.kr/msr/msreward/level_benefit.do'))


        ## 이전, 다음 버튼

        self.Btn_previous1.clicked.connect(self.prev_tab)
        self.Btn_next1.clicked.connect(self.next_tab)
        self.Btn_next1.clicked.connect(self.total)
        self.Btn_cancel2.clicked.connect(self.prev_tab2)

        self.Btn_next4.clicked.connect(self.next_tab3)
        self.Btn_next5.clicked.connect(self.next_tab3)
        self.Btn_cancel1.clicked.connect(self.prev_tab2)
        self.Btn_cancel1.clicked.connect(self.btsclear)
        self.Btn_close.clicked.connect(QCoreApplication.instance().quit)

        
        ##버튼 1-58번
        self.Btn_1.clicked.connect(self.next_tab2)
        self.Btn_1.clicked.connect(self.input_1)
        self.Btn_1.clicked.connect(self.output)
        self.Btn_1.clicked.connect(self.total)

        self.Btn_2.clicked.connect(self.next_tab2)
        self.Btn_2.clicked.connect(self.input_2)
        self.Btn_2.clicked.connect(self.output)
        self.Btn_2.clicked.connect(self.total)

        self.Btn_3.clicked.connect(self.next_tab2)
        self.Btn_3.clicked.connect(self.input_3)
        self.Btn_3.clicked.connect(self.output)
        self.Btn_3.clicked.connect(self.total)

        self.Btn_4.clicked.connect(self.next_tab2)
        self.Btn_order.clicked.connect(self.next_tab)
        self.Btn_4.clicked.connect(self.input_4)
        self.Btn_4.clicked.connect(self.output)
        self.Btn_4.clicked.connect(self.total)

        self.Btn_5.clicked.connect(self.input_5)
        self.Btn_5.clicked.connect(self.output)

        self.Btn_6.clicked.connect(self.input_6)
        self.Btn_6.clicked.connect(self.output)

        self.Btn_7.clicked.connect(self.input_7)
        self.Btn_7.clicked.connect(self.output)

        self.Btn_8.clicked.connect(self.input_8)
        self.Btn_8.clicked.connect(self.output)

        self.Btn_9.clicked.connect(self.input_9)
        self.Btn_9.clicked.connect(self.output)

        self.Btn_10.clicked.connect(self.input_10)
        self.Btn_10.clicked.connect(self.output)

        self.Btn_11.clicked.connect(self.input_11)
        self.Btn_11.clicked.connect(self.output)

        self.Btn_12.clicked.connect(self.input_12)
        self.Btn_12.clicked.connect(self.output)

        self.Btn_13.clicked.connect(self.input_13)
        self.Btn_13.clicked.connect(self.output)

        self.Btn_14.clicked.connect(self.input_14)
        self.Btn_14.clicked.connect(self.output)

        self.Btn_15.clicked.connect(self.input_15)
        self.Btn_15.clicked.connect(self.output)

        self.Btn_16.clicked.connect(self.input_16)
        self.Btn_16.clicked.connect(self.output)

        self.Btn_17.clicked.connect(self.input_17)
        self.Btn_17.clicked.connect(self.output)

        self.Btn_18.clicked.connect(self.input_18)
        self.Btn_18.clicked.connect(self.output)

        self.Btn_19.clicked.connect(self.input_19)
        self.Btn_19.clicked.connect(self.output)

        self.Btn_20.clicked.connect(self.input_20)
        self.Btn_20.clicked.connect(self.output)

        self.Btn_21.clicked.connect(self.input_21)
        self.Btn_21.clicked.connect(self.output)

        self.Btn_22.clicked.connect(self.input_22)
        self.Btn_22.clicked.connect(self.output)

        self.Btn_23.clicked.connect(self.input_23)
        self.Btn_23.clicked.connect(self.output)

        self.Btn_24.clicked.connect(self.input_24)
        self.Btn_24.clicked.connect(self.output)

        self.Btn_25.clicked.connect(self.input_25)
        self.Btn_25.clicked.connect(self.output)

        self.Btn_26.clicked.connect(self.input_26)
        self.Btn_26.clicked.connect(self.output)

        self.Btn_27.clicked.connect(self.input_27)
        self.Btn_27.clicked.connect(self.output)

        self.Btn_28.clicked.connect(self.input_28)
        self.Btn_28.clicked.connect(self.output)

        self.Btn_29.clicked.connect(self.input_29)
        self.Btn_29.clicked.connect(self.output)

        self.Btn_30.clicked.connect(self.input_30)
        self.Btn_30.clicked.connect(self.output)

        self.Btn_31.clicked.connect(self.input_31)
        self.Btn_31.clicked.connect(self.output)

        self.Btn_32.clicked.connect(self.input_32)
        self.Btn_32.clicked.connect(self.output)

        self.Btn_33.clicked.connect(self.input_33)
        self.Btn_33.clicked.connect(self.output)

        self.Btn_34.clicked.connect(self.input_34)
        self.Btn_34.clicked.connect(self.output)

        self.Btn_35.clicked.connect(self.input_35)
        self.Btn_35.clicked.connect(self.output)

        self.Btn_36.clicked.connect(self.input_36)
        self.Btn_36.clicked.connect(self.output)

        self.Btn_37.clicked.connect(self.input_37)
        self.Btn_37.clicked.connect(self.output)

        self.Btn_38.clicked.connect(self.input_38)
        self.Btn_38.clicked.connect(self.output)

        self.Btn_39.clicked.connect(self.input_39)
        self.Btn_39.clicked.connect(self.output)

        self.Btn_40.clicked.connect(self.input_40)
        self.Btn_40.clicked.connect(self.output)

        self.Btn_41.clicked.connect(self.input_41)
        self.Btn_41.clicked.connect(self.output)

        self.Btn_42.clicked.connect(self.input_42)
        self.Btn_42.clicked.connect(self.output)

        self.Btn_43.clicked.connect(self.input_43)
        self.Btn_43.clicked.connect(self.output)

        self.Btn_44.clicked.connect(self.input_44)
        self.Btn_44.clicked.connect(self.output)

        self.Btn_45.clicked.connect(self.input_45)
        self.Btn_45.clicked.connect(self.output)

        self.Btn_46.clicked.connect(self.input_46)
        self.Btn_46.clicked.connect(self.output)

        self.Btn_47.clicked.connect(self.input_47)
        self.Btn_47.clicked.connect(self.output)

        self.Btn_48.clicked.connect(self.input_48)
        self.Btn_48.clicked.connect(self.output)

        self.Btn_49.clicked.connect(self.input_49)
        self.Btn_49.clicked.connect(self.output)

        self.Btn_50.clicked.connect(self.input_50)
        self.Btn_50.clicked.connect(self.output)

        self.Btn_51.clicked.connect(self.input_51)
        self.Btn_51.clicked.connect(self.output)

        self.Btn_52.clicked.connect(self.input_52)
        self.Btn_52.clicked.connect(self.output)

        self.Btn_53.clicked.connect(self.input_53)
        self.Btn_53.clicked.connect(self.output)

        self.Btn_54.clicked.connect(self.input_54)
        self.Btn_54.clicked.connect(self.output)

        self.Btn_55.clicked.connect(self.input_55)
        self.Btn_55.clicked.connect(self.output)

        self.Btn_56.clicked.connect(self.input_56)
        self.Btn_56.clicked.connect(self.output)

        self.Btn_57.clicked.connect(self.input_57)
        self.Btn_57.clicked.connect(self.output)

        self.Btn_58.clicked.connect(self.input_58)
        self.Btn_58.clicked.connect(self.output)



        self.Bts_1 = 0
        self.Bts_2 = 0
        self.Bts_3 = 0
        self.Bts_4 = 0
        self.Bts_5 = 0
        self.Bts_6 = 0
        self.Bts_7 = 0
        self.Bts_8 = 0
        self.Bts_9 = 0
        self.Bts_10 = 0
        self.Bts_11 = 0
        self.Bts_12 = 0
        self.Bts_13 = 0
        self.Bts_14 = 0
        self.Bts_15 = 0
        self.Bts_16 = 0
        self.Bts_17 = 0
        self.Bts_18 = 0
        self.Bts_19 = 0
        self.Bts_20 = 0
        self.Bts_21 = 0
        self.Bts_22 = 0
        self.Bts_23 = 0
        self.Bts_24 = 0
        self.Bts_25 = 0
        self.Bts_26 = 0
        self.Bts_27 = 0
        self.Bts_28 = 0
        self.Bts_29 = 0
        self.Bts_30 = 0
        self.Bts_31 = 0
        self.Bts_32 = 0
        self.Bts_33 = 0
        self.Bts_34 = 0
        self.Bts_35 = 0
        self.Bts_36 = 0
        self.Bts_37 = 0
        self.Bts_38 = 0
        self.Bts_39 = 0
        self.Bts_40 = 0
        self.Bts_41 = 0
        self.Bts_42 = 0
        self.Bts_43 = 0
        self.Bts_44 = 0
        self.Bts_45 = 0
        self.Bts_46 = 0
        self.Bts_47 = 0
        self.Bts_48 = 0
        self.Bts_49 = 0
        self.Bts_50 = 0
        self.Bts_51 = 0
        self.Bts_52 = 0
        self.Bts_53 = 0
        self.Bts_54 = 0
        self.Bts_55 = 0
        self.Bts_56 = 0
        self.Bts_57 = 0
        self.Bts_58 = 0
        self.totalprice = 0

        ## +1페이지

    def next_tab(self):
        cur_index = self.tabWidget.currentIndex()
        if cur_index < len(self.tabWidget) - 1:
            self.tabWidget.setCurrentIndex(cur_index + 1)

        ## +2페이지

    def next_tab2(self):
        cur_index = self.tabWidget.currentIndex()
        if cur_index < len(self.tabWidget) - 1:
            self.tabWidget.setCurrentIndex(cur_index + 2)

        ## -1페이지(이전)

    def prev_tab(self):
        cur_index = self.tabWidget.currentIndex()
        if cur_index > 0:
            self.tabWidget.setCurrentIndex(cur_index - 1)

    def prev_tab2(self):
        cur_index = self.tabWidget.currentIndex()
        if cur_index > 0:
            self.tabWidget.setCurrentIndex(cur_index - 2)

        ## 결제창 탭 이동

    def next_tab3(self):
        cur_index = self.tabWidget_6.currentIndex()
        if cur_index < len(self.tabWidget_6) - 1:
            self.tabWidget_6.setCurrentIndex(cur_index + 1)

    def input_1(self,n):
        for i in range(n+1):
            self.Bts_1 +=1

    def input_2(self,n):
        for i in range(n+1):
            self.Bts_2 +=1

    def input_3(self, n):
        for i in range(n + 1):
            self.Bts_3 += 1

    def input_4(self,n):
        for i in range(n+1):
            self.Bts_4 +=1

    def input_5(self,n):
        for i in range(n+1):
            self.Bts_5 +=1

    def input_6(self, n):
        for i in range(n + 1):
            self.Bts_6 += 1

    def input_7(self, n):
        for i in range(n + 1):
            self.Bts_7 += 1

    def input_8(self, n):
        for i in range(n + 1):
            self.Bts_8 += 1

    def input_9(self, n):
        for i in range(n + 1):
            self.Bts_9 += 1

    def input_10(self, n):
        for i in range(n + 1):
            self.Bts_10 += 1

    def input_11(self, n):
        for i in range(n + 1):
            self.Bts_11 += 1

    def input_12(self, n):
        for i in range(n + 1):
            self.Bts_12 += 1

    def input_13(self, n):
        for i in range(n + 1):
            self.Bts_13 += 1

    def input_14(self, n):
        for i in range(n + 1):
            self.Bts_14 += 1

    def input_15(self, n):
        for i in range(n + 1):
            self.Bts_15 += 1

    def input_16(self, n):
        for i in range(n + 1):
            self.Bts_16 += 1

    def input_17(self, n):
        for i in range(n + 1):
            self.Bts_17 += 1

    def input_18(self, n):
        for i in range(n + 1):
            self.Bts_18 += 1

    def input_19(self, n):
        for i in range(n + 1):
            self.Bts_19 += 1

    def input_20(self, n):
        for i in range(n + 1):
            self.Bts_20 += 1

    def input_21(self, n):
        for i in range(n + 1):
            self.Bts_21 += 1

    def input_22(self, n):
        for i in range(n + 1):
            self.Bts_22 += 1

    def input_23(self, n):
        for i in range(n + 1):
            self.Bts_23 += 1
    def input_24(self,n):
        for i in range(n+1):
            self.Bts_24 +=1

    def input_25(self,n):
        for i in range(n+1):
            self.Bts_25 +=1

    def input_26(self, n):
        for i in range(n + 1):
            self.Bts_26 += 1
    def input_27(self,n):
        for i in range(n+1):
            self.Bts_27 +=1

    def input_28(self,n):
        for i in range(n+1):
            self.Bts_28 +=1

    def input_29(self, n):
        for i in range(n + 1):
            self.Bts_29 += 1

    def input_30(self, n):
        for i in range(n + 1):
            self.Bts_30 += 1

    def input_31(self, n):
        for i in range(n + 1):
            self.Bts_31 += 1

    def input_32(self, n):
        for i in range(n + 1):
            self.Bts_32 += 1

    def input_33(self, n):
        for i in range(n + 1):
            self.Bts_33 += 1

    def input_34(self, n):
        for i in range(n + 1):
            self.Bts_34 += 1

    def input_35(self, n):
        for i in range(n + 1):
            self.Bts_35 += 1

    def input_36(self, n):
        for i in range(n + 1):
            self.Bts_36 += 1

    def input_37(self, n):
        for i in range(n + 1):
            self.Bts_37 += 1

    def input_38(self, n):
        for i in range(n + 1):
            self.Bts_38 += 1

    def input_39(self, n):
        for i in range(n + 1):
            self.Bts_39 += 1

    def input_40(self, n):
        for i in range(n + 1):
            self.Bts_40 += 1

    def input_41(self, n):
        for i in range(n + 1):
            self.Bts_41 += 1

    def input_42(self, n):
        for i in range(n + 1):
            self.Bts_42 += 1

    def input_43(self, n):
        for i in range(n + 1):
            self.Bts_43 += 1

    def input_44(self, n):
        for i in range(n + 1):
            self.Bts_44 += 1

    def input_45(self, n):
        for i in range(n + 1):
            self.Bts_45 += 1

    def input_46(self, n):
        for i in range(n + 1):
            self.Bts_46 += 1

    def input_47(self,n):
        for i in range(n+1):
            self.Bts_47 +=1

    def input_48(self,n):
        for i in range(n+1):
            self.Bts_48 +=1

    def input_49(self, n):
        for i in range(n + 1):
            self.Bts_49 += 1

    def input_50(self,n):
        for i in range(n+1):
            self.Bts_50+=1

    def input_51(self,n):
        for i in range(n+1):
            self.Bts_51 +=1

    def input_52(self, n):
        for i in range(n + 1):
            self.Bts_5 += 1

    def input_53(self, n):
        for i in range(n + 1):
            self.Bts_53 += 1

    def input_54(self, n):
        for i in range(n + 1):
            self.Bts_54 += 1

    def input_55(self, n):
        for i in range(n + 1):
            self.Bts_55 += 1

    def input_56(self, n):
        for i in range(n + 1):
            self.Bts_56 += 1

    def input_57(self, n):
        for i in range(n + 1):
            self.Bts_57+= 1

    def input_58(self, n):
        for i in range(n + 1):
            self.Bts_58 += 1



    def output(self):
        self.textBrowser.clear()
        if self.Bts_1 >0:
            self.textBrowser.append("오늘의 커피 * {}".format(self.Bts_1))
        if self.Bts_2 > 0:
            self.textBrowser.append("허니 자몽 블랙티 * {}".format(self.Bts_2))
        if self.Bts_3 > 0:
            self.textBrowser.append("유기농 말치 프라푸치노 * {}".format(self.Bts_3))
        if self.Bts_4 > 0:
            self.textBrowser.append("아메리카노 * {}".format(self.Bts_4))
        if self.Bts_5 > 0:
            self.textBrowser.append("루비 레드 칠링 아이스티 * {}".format(self.Bts_5))
        if self.Bts_6 > 0:
            self.textBrowser.append("제스트 그린 블렌디드 * {}".format(self.Bts_6))
        if self.Bts_7 > 0:
            self.textBrowser.append("루프탑 그레이 라떼 * {}".format(self.Bts_7))
        if self.Bts_8 > 0:
            self.textBrowser.append("아이스크림 블렌딩 콜드브루 * {}".format(self.Bts_8))
        if self.Bts_9 > 0:
            self.textBrowser.append("아이스 유자 & 유자베리 티  * {}".format(self.Bts_9))
        if self.Bts_10 > 0:
            self.textBrowser.append("트윙클 스타 핑크 블렌디드 * {}".format(self.Bts_10))
        if self.Bts_11 > 0:
            self.textBrowser.append("제주까망 크림 프라푸치노 * {}".format(self.Bts_11))
        if self.Bts_12 > 0:
            self.textBrowser.append("쑥떡 크림 프라푸치노 * {}".format(self.Bts_12))
        if self.Bts_13 > 0:
            self.textBrowser.append("별다방 땅콩 프라푸치노 * {}".format(self.Bts_13))
        if self.Bts_14 > 0:
            self.textBrowser.append("천혜향 블랙티 블렌디드 * {}".format(self.Bts_14))
        if self.Bts_15 > 0:
            self.textBrowser.append("제주 청귤 레모네이드 * {}".format(self.Bts_15))
        if self.Bts_16 > 0:
            self.textBrowser.append("별다방 땅콩 라떼 * {}".format(self.Bts_16))
        if self.Bts_17 > 0:
            self.textBrowser.append("아메리카노 * {}".format(self.Bts_17))
        if self.Bts_18 > 0:
            self.textBrowser.append("카페 라떼 * {}".format(self.Bts_18))
        if self.Bts_19 > 0:
            self.textBrowser.append("카페 모카 * {}".format(self.Bts_19))
        if self.Bts_20 > 0:
            self.textBrowser.append("돌체 라떼 * {}".format(self.Bts_20))
        if self.Bts_21 > 0:
            self.textBrowser.append("바닐라 플랫 화이트 * {}".format(self.Bts_21))
        if self.Bts_22 > 0:
            self.textBrowser.append("디카페인 아메리카노 * {}".format(self.Bts_22))
        if self.Bts_23 > 0:
            self.textBrowser.append("유기농 말차 크림 프라푸치노 * {}".format(self.Bts_23))
        if self.Bts_24 > 0:
            self.textBrowser.append("자바칩 프라푸치노 * {}".format(self.Bts_24))
        if self.Bts_25 > 0:
            self.textBrowser.append("화이트 타이거 프라푸치노 * {}".format(self.Bts_25))
        if self.Bts_26 > 0:
            self.textBrowser.append("카라멜 프라푸치노 * {}".format(self.Bts_26))
        if self.Bts_27 > 0:
            self.textBrowser.append("화이트 딸기 크림 프라푸치노 * {}".format(self.Bts_27))
        if self.Bts_28 > 0:
            self.textBrowser.append("모카 프라푸치노 * {}".format(self.Bts_28))
        if self.Bts_29 > 0:
            self.textBrowser.append("민트 초콜릿칩 블렌디드 * {}".format(self.Bts_29))
        if self.Bts_30 > 0:
            self.textBrowser.append("딸기 딜라이트 요거트 블렌디드 * {}".format(self.Bts_30))
        if self.Bts_31 > 0:
            self.textBrowser.append("망고 바나나 블렌디드 * {}".format(self.Bts_31))
        if self.Bts_32 > 0:
            self.textBrowser.append("망고 패션 프루트 블렌디드 * {}".format(self.Bts_32))
        if self.Bts_33 > 0:
            self.textBrowser.append("제스트 그린 블렌디드 * {}".format(self.Bts_33))
        if self.Bts_34 > 0:
            self.textBrowser.append("트윙클 스타 핑크 블렌디드 * {}".format(self.Bts_34))
        if self.Bts_35 > 0:
            self.textBrowser.append("블루베리 치즈 케이크 * {}".format(self.Bts_35))
        if self.Bts_36 > 0:
            self.textBrowser.append("헤이즐럿 브라우니 * {}".format(self.Bts_36))
        if self.Bts_37 > 0:
            self.textBrowser.append("밤콩 달콩 두유 브레드 * {}".format(self.Bts_37))
        if self.Bts_38 > 0:
            self.textBrowser.append("샤인 머스캣 스윗박스 * {}".format(self.Bts_38))
        if self.Bts_39 > 0:
            self.textBrowser.append("(제주) 녹차 생크림 롤 * {}".format(self.Bts_39))
        if self.Bts_40 > 0:
            self.textBrowser.append("돌코롬 쫍지롱 와플샌드 * {}".format(self.Bts_40))
        if self.Bts_41 > 0:
            self.textBrowser.append("베이컨 치즈 토스트 * {}".format(self.Bts_41))
        if self.Bts_42 > 0:
            self.textBrowser.append("리코타 치즈 바게트 샌드위치 * {}".format(self.Bts_42))
        if self.Bts_43 > 0:
            self.textBrowser.append("바베큐 치킨 치즈 치아바타 * {}".format(self.Bts_43))
        if self.Bts_44 > 0:
            self.textBrowser.append("트리플 치즈 크로크 무슈 * {}".format(self.Bts_44))
        if self.Bts_45 > 0:
            self.textBrowser.append("부드러운 생크림 카스텔라 * {}".format(self.Bts_45))
        if self.Bts_46 > 0:
            self.textBrowser.append("튜나 멜트 샌드위치 * {}".format(self.Bts_46))
        if self.Bts_47 > 0:
            self.textBrowser.append("리얼 블루베리 베이글 * {}".format(self.Bts_47))
        if self.Bts_48 > 0:
            self.textBrowser.append("클래식 스콘 * {}".format(self.Bts_48))
        if self.Bts_49 > 0:
            self.textBrowser.append("연유 밀크모닝 * {}".format(self.Bts_49))
        if self.Bts_50 > 0:
            self.textBrowser.append("프렌치 크로아상 * {}".format(self.Bts_50))
        if self.Bts_51 > 0:
            self.textBrowser.append("(제주)앙녹차 베이글 * {}".format(self.Bts_51))
        if self.Bts_52 > 0:
            self.textBrowser.append("우유를 품은 초콜릿 크로와상 * {}".format(self.Bts_52))
        if self.Bts_53 > 0:
            self.textBrowser.append("부드러운 티라미수 롤 * {}".format(self.Bts_53))
        if self.Bts_54 > 0:
            self.textBrowser.append("진한 녹차 생크림 케이크 * {}".format(self.Bts_54))
        if self.Bts_55 > 0:
            self.textBrowser.append("번트 치즈 케이크 * {}".format(self.Bts_55))
        if self.Bts_56 > 0:
            self.textBrowser.append("레드 벨벳 크림치즈 케이크 * {}".format(self.Bts_56))
        if self.Bts_57 > 0:
            self.textBrowser.append("당근 현무암케이크 * {}".format(self.Bts_57))
        if self.Bts_58 > 0:
            self.textBrowser.append("새코롬 돌코롬 한라봉 케이크 * {}".format(self.Bts_58))


    def btsclear(self):
        self.textBrowser.clear()
        self.Bts_1 = 0
        self.Bts_2 = 0
        self.Bts_3 = 0
        self.Bts_4 = 0
        self.Bts_5 = 0
        self.Bts_6 = 0
        self.Bts_7 = 0
        self.Bts_8 = 0
        self.Bts_9 = 0
        self.Bts_10 = 0
        self.Bts_11 = 0
        self.Bts_12 = 0
        self.Bts_13 = 0
        self.Bts_14 = 0
        self.Bts_15 = 0
        self.Bts_16 = 0
        self.Bts_17 = 0
        self.Bts_18 = 0
        self.Bts_19 = 0
        self.Bts_20 = 0
        self.Bts_21 = 0
        self.Bts_22 = 0
        self.Bts_23 = 0
        self.Bts_24 = 0
        self.Bts_25 = 0
        self.Bts_26 = 0
        self.Bts_27 = 0
        self.Bts_28 = 0
        self.Bts_29 = 0
        self.Bts_30 = 0
        self.Bts_31 = 0
        self.Bts_32 = 0
        self.Bts_33 = 0
        self.Bts_34 = 0
        self.Bts_35 = 0
        self.Bts_36 = 0
        self.Bts_37 = 0
        self.Bts_38 = 0
        self.Bts_39 = 0
        self.Bts_40 = 0
        self.Bts_41 = 0
        self.Bts_42 = 0
        self.Bts_43 = 0
        self.Bts_44 = 0
        self.Bts_45 = 0
        self.Bts_46 = 0
        self.Bts_47 = 0
        self.Bts_48 = 0
        self.Bts_49 = 0
        self.Bts_50 = 0
        self.Bts_51 = 0
        self.Bts_52 = 0
        self.Bts_53 = 0
        self.Bts_54 = 0
        self.Bts_55 = 0
        self.Bts_56 = 0
        self.Bts_57 = 0
        self.Bts_58 = 0


    def total(self):
        self.totalprice =   self.Bts_1 * 3800 + \
                            self.Bts_2 * 5800 + \
                            self.Bts_3 * 6300 + \
                            self.Bts_4 * 4100 +\
                            self.Bts_5 * 8300 +\
                            self.Bts_6 * 8600 +\
                            self.Bts_7 * 8500 +\
                            self.Bts_8 * 6600 +\
                            self.Bts_9 * 5900 +\
                            self.Bts_10 * 6300 +\
                            self.Bts_11 * 7500 +\
                            self.Bts_12 * 7500 +\
                            self.Bts_13 * 7500 +\
                            self.Bts_14 * 7500 +\
                            self.Bts_15 * 7000 +\
                            self.Bts_16 * 7200 +\
                            self.Bts_17 * 4100 +\
                            self.Bts_18 * 4600 +\
                            self.Bts_19 * 5100 +\
                            self.Bts_20 * 5600 +\
                            self.Bts_21 * 5600 +\
                            self.Bts_22 * 4400 +\
                            self.Bts_23 * 6300 +\
                            self.Bts_24 * 6100 +\
                            self.Bts_25 * 6500 +\
                            self.Bts_26 * 5600 +\
                            self.Bts_27 * 6100 +\
                            self.Bts_28 * 5600 +\
                            self.Bts_29 * 6100 +\
                            self.Bts_30 * 6100 +\
                            self.Bts_31 * 6300 +\
                            self.Bts_32 * 5000 +\
                            self.Bts_33 * 8600 +\
                            self.Bts_34 * 6300 +\
                            self.Bts_35 * 6900 +\
                            self.Bts_36 * 3500 +\
                            self.Bts_37 * 4500 +\
                            self.Bts_38 * 7900 +\
                            self.Bts_39 * 7500 +\
                            self.Bts_40 * 7800 +\
                            self.Bts_41 * 4900 +\
                            self.Bts_42 * 6200 +\
                            self.Bts_43 * 5800 +\
                            self.Bts_44 * 5200 +\
                            self.Bts_45 * 4500 +\
                            self.Bts_46 * 5900 +\
                            self.Bts_47 * 3000 +\
                            self.Bts_48 * 3300 +\
                            self.Bts_49 * 4300 +\
                            self.Bts_50 * 3200 +\
                            self.Bts_51 * 4900 +\
                            self.Bts_52 * 4900 +\
                            self.Bts_53 * 5900 +\
                            self.Bts_54 * 5700 +\
                            self.Bts_55 * 6900 +\
                            self.Bts_56 * 5500 +\
                            self.Bts_57 * 6800 +\
                            self.Bts_58 * 6500
        if self.totalprice > 0:
            self.total_1.clear()
            self.total_2.clear()
            self.total_1.setText(str(self.totalprice))
            self.total_2.setText(str(self.totalprice))






if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()