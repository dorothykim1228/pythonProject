import random
import time
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import *
from PyQt5 import QtWidgets, QtGui, QtCore

dic_mine = {"Lv.1": 20, "Lv.2":25, "Lv.3":30, "Lv.4":35, "Lv.5":40, "Lv.6":45 }

ui1 = "poket1.ui"
ui2 = "poket2.ui"
ui3 = "poket3.ui"
ui4 = "poket4.ui"




class llist:
    CN = []
    name = []
    a = 0
    lv = 1
    exp = []
    hp = []
    now_hp = []
    hatt = 7
    latt = 3
    att_ = 0
    skill = {
"피카츄":["전광석화", "울음소리", "전기쇼크"],
"이브이" : ["몸통박치기", "모래뿌리기", "전광석화"],
"꼬부기" : ["몸통박치기", "꼬리흔들기", "물대포"],
"이상해씨" : ["몸통박치기", "울음소리", "덩쿨채찍"]
}
    elv = []
    ehhp = 21
    elhp = 10
    ehp = []
    now_ehp = []
    ehtt = 6
    eltt = 2
    eatt = 0
    enemy_name = ["파이리", "도지", "모다피", "딱충이", "마임맨", "따라큐", "꼬지모", "왕구리","치렁", "단데기"]
    enemy = {
    "파이리": ["할퀴기", "울음소리", "불꽃세례"],
    "도지": ["나락보내기", "b", "c"],
    "모다피": ["덩굴채찍", "성장", "독가루"],
    "딱충이": ["단단해지기", "단단해지기", "단단해지기"],
    "마임맨": ["염동력", "배리어", "빛의장막"],
    "따라큐": ["우드래머", "튀어오르기", "할퀴기"],
    "꼬지모": ["돌떨구기", "흉내내기", "바둥바둥"],
    "왕구리": ["물대포", "연속뺨치기", "최면술"],
    "치렁": ["김밥말이", "울음소리", "놀래키기"],
    "단데기": ["단단해지기", "단단해지기", "단단해지기"]
}


class Poket1(QMainWindow) :

    def __init__(self):
        super().__init__()
        loadUi(ui1, self)
        self.movie = QMovie("together.gif")
        self.title.setMovie(self.movie)
        self.movie.start()
        self.start_game.clicked.connect(self.start)
        self.end_game.clicked.connect(self.end)

    def start(self):
        self.Poket2 = Poket2()
        self.start = Poket2()
        self.start.show()
        self.close()

    def end(self):
        self.close()






class Poket2(QMainWindow):
    global name
    def __init__(self):
        super().__init__()
        loadUi(ui2, self)

        self.movie = QMovie("ohoh.gif")
        self.ohoh_label.setMovie(self.movie)
        self.movie.start()

        self.pika_btn.clicked.connect(self.pika)
        self.eve_btn.clicked.connect(self.eve)
        self.sang_btn.clicked.connect(self.sang)
        self.ggo_btn.clicked.connect(self.ggo)

    def pika(self):
        llist.CN.append("피카츄")
        name.append("피카츄")

        self.pika1 = Poket3()
        self.pika1.show()
        self.close()
        self.movie = QMovie("pikag.gif")
        self.pika1.poket.setMovie(self.movie)
        self.movie.start()

        # print(name)
        # print(type(name))
        # print(name[0])
        # print(type(name[0]))

    def eve(self):
        llist.CN.append("이브이")
        name.append("이브이")

        self.eve1 = Poket3()
        self.eve1.show()
        self.close()
        self.movie = QMovie("eveg.gif")
        self.eve1.poket.setMovie(self.movie)
        self.movie.start()

    def sang(self):
        llist.CN.append("이상해씨")
        name.append("이상해씨")
        self.sang1 = Poket3()
        self.sang1.show()
        self.close()
        self.movie = QMovie("strange.gif")
        self.sang1.poket.setMovie(self.movie)
        self.movie.start()

    def ggo(self):
        llist.CN.append("꼬부기")
        name.append("꼬부기")

        self.ggo1 = Poket3()
        self.ggo1.show()
        self.close()
        self.movie = QMovie("gogog.gif")
        self.ggo1.poket.setMovie(self.movie)
        self.movie.start()




class Poket3(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi(ui3, self)
        self.go_fight.clicked.connect(self.fight)
        self.poket_info.setPlainText(f"이름 : {str(llist.CN[0])}")
        self.poket_info.append(f"레벨 : {lv}")
        self.poket_info.append(f"체력: {now_hp}/{hp}")
        self.poket_info.append(f"공격력: {latt}~{hatt}")
        self.poket_info.append(f"{llist.CN[0]}의 스킬목록")
        self.poket_info.append(f"{skill[llist.CN[0]]}")


    def fight(self):
        self.fight1 = Poket4()
        self.fight1.show()
        self.close()


class Poket4(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi(ui4, self)

        if llist.CN[0] == "피카츄":
            self.movie = QMovie("pikag.gif")
            self.bettlepokemon.setMovie(self.movie)
            self.movie.start()
        elif llist.CN[0] == "이브이":
            self.movie = QMovie("eveg.gif")
            self.bettlepokemon.setMovie(self.movie)
            self.movie.start()
        elif llist.CN[0] == "이상해씨":
            self.movie = QMovie("strange.gif")
            self.bettlepokemon.setMovie(self.movie)
            self.movie.start()
        elif llist.CN[0] == "꼬부기":
            self.movie = QMovie("gogog.gif")
            self.bettlepokemon.setMovie(self.movie)
            self.movie.start()
        else:
            pass

        self.skill1.setText(skill[llist.CN[0]][0])
        self.skill2.setText(skill[llist.CN[0]][1])
        self.skill3.setText(skill[llist.CN[0]][2])
        self.skill1.clicked.connect(self.ski1)
        # self.skill2.clicked.connect(self.ski2)
        # self.skill3.clicked.connect(self.ski3)

        self.run.clicked.connect(self.running)
        self.name_level.setText(f"레벨:{lv}\t이름:{llist.CN[0]}")

        for i in range(0,1): #상대방 능력치 설정(매번다른걸 위해 포문사용)
            enemyname_range = random.randrange(0,10)
            elv_range = random.randrange(1,6)
            elv.append(elv_range)
            ehp_range= random.randrange(5+(elv[0]*5), 16+(elv[0]*5))
            ehp.append(ehp_range)
            self.ename_level.setText(f"레벨:{elv[0]}\t이름:{enemy_name[enemyname_range]}")
            print(elv[0], ehp[0])

    def ski1(self): #1번째 스킬 설정중
        for i in range(0,1):
            att_ = random.randrange(1+(lv*2), 6+(lv*2))
            print(ehp, att_)
            now_ehp.append(sum(ehp)- att_)
            print(now_ehp)

            hp.append(15+(lv*5))
            print(hp[0])
            eatt = random.randrange(0+(elv[0]*2), 4+(elv[0]*2))
            print(eatt)
            now_hp.append(sum(hp) - eatt)
            print(now_hp)


    def running(self): #도망가기
        self.sh = Poket3()
        self.sh.show()
        self.close()






app = QApplication(sys.argv)
myWindow = Poket1()
myWindow.show()
app.exec_()