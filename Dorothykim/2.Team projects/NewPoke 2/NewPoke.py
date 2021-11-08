from random import*
import time
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import *
from PyQt5 import QtWidgets, QtGui, QtCore


ui1 = "poket1.ui"
ui2 = "poket2.ui"
ui3 = "poket3.ui"
ui4 = "poket4.ui"

class Variable:
    S_pokemon = 0 #스타팅 포켓몬 선택
    E_pokemon = 0


class PokeSt: #포켓몬 능력치
    def __init__(self, name, n_hp, hp, n_mp, mp, n_exp, exp, skill_1_name,skill_2_name,skill_3_name):
        self.name = name #이름
        self.n_hp = n_hp #현재 체력
        self.hp = hp #최대 체력
        self.n_mp = n_mp #현재 마나
        self.mp = mp #최대 마나
        self.n_exp = n_exp #현재 경험치
        self.exp = exp #최대 경험치
        self.skill_1_name = skill_1_name #1스킬 이름
        self.skill_2_name = skill_2_name #2스킬 이름
        self.skill_3_name = skill_3_name #3스킬 이름
       # self.skill_1 = skill_1 #1스킬 데미지
        #self.skill_2 = skill_2 #2스킬 데미지
        #self.skill_3 = skill_3 #3스킬 데미지

pokemons = [
    PokeSt("피카츄", 100, 100, 50, 50, 0, 100, "전광석화", "아이언테일", "백만볼트"),#, 10, 20, 50),
    PokeSt("이브이", 100, 100, 50, 50, 0, 100,"물기", "스피드스타", "브이브이브레이크",),# 15, 30, 60),
    PokeSt("김상희씨",  100, 100, 50, 50, 0, 100, "몸통박치", "덩쿨채찍","솔라빔", ),#10, 30, 70),
    PokeSt("꼬부기", 100, 100, 50, 50, 0, 100, "물대포", "아쿠아테일","하이드로펌프") #20, 30, 40)
]


class EpokeSt: #적 포켓몬 능력치
    def __init__(self, name, n_hp, hp, skill_1_name,skill_2_name,skill_3_name):
        self.name = name
        self.n_hp = n_hp
        self.hp = hp
        self.skill_1_name = skill_1_name
        self.skill_2_name = skill_2_name
        self.skill_3_name = skill_3_name
        #self.skill_1 = skill_1
        #self.skill_2 = skill_2
        #self.skill_3 = skill_3


Epokemons = [
    EpokeSt("따라큐", 120, 120, "야습", "섀도크루", "치근거리기"), #a, b, c),
    EpokeSt("파이리", 80, 80, "할퀴기", "화염방사", "지구던지기"),  #a, b, c),
    EpokeSt("치렁", 70, 70, "김밥말이", "놀래키기", "소란피기"),#  a, b, c),
    EpokeSt("우츠보트", 60, 60, "김밥말이", "덩굴채찍", "파워휩"),#  a, b, c),
    EpokeSt("또가스", 90, 90, "몸통박치기", "스모그", "오물공격"),#  a, b, c),
    EpokeSt("가디", 50, 50, "물기", "불꽃사레", "화염방사"),#  a, b, c),
    EpokeSt("뮤", 40, 70, "막치기", "원시의힘", "환상빔"),# a, b, c),
    EpokeSt("개굴닌자", 60, 90, "풀베기", "제비반환", "물수리검"),# a, b, c),
    EpokeSt("마임맨", 30, 80, "염동력", "환상빔", "사이코키네시스"),# a, b, c),
    EpokeSt("푸린", 90, 70, "사슬묶이", "막치기", "애교부리기")# a, b, c)
]




class Poket4(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None)
        loadUi(ui4, self)
        if Variable.S_pokemon == 0:
            self.movie = QMovie("pikag.gif")
            self.bettlepokemon.setMovie(self.movie)
            self.movie.start()
        elif Variable.S_pokemon == 1:
            self.movie = QMovie("eveg.gif")
            self.bettlepokemon.setMovie(self.movie)
            self.movie.start()
        elif Variable.S_pokemon == 2:
            self.movie = QMovie("strange.gif")
            self.bettlepokemon.setMovie(self.movie)
            self.movie.start()
        elif Variable.S_pokemon == 3:
            self.movie = QMovie("gogog.gif")
            self.bettlepokemon.setMovie(self.movie)
            self.movie.start()

        if Variable.E_pokemon == 0:
            self.movie = QMovie("que.gif")
            self.bettlepokemon_2.setMovie(self.movie)
            self.movie.start()
        elif Variable.E_pokemon == 1:
            self.movie = QMovie("fire.gif")
            self.bettlepokemon_2.setMovie(self.movie)
            self.movie.start()
        elif Variable.E_pokemon == 2:
            self.movie = QMovie("rung.gif")
            self.bettlepokemon_2.setMovie(self.movie)
            self.movie.start()
        elif Variable.E_pokemon == 3:
            self.movie = QMovie("bot.gif")
            self.bettlepokemon_2.setMovie(self.movie)
            self.movie.start()
        elif Variable.E_pokemon == 4:
            self.movie = QMovie("dodo.gif")
            self.bettlepokemon_2.setMovie(self.movie)
            self.movie.start()
        elif Variable.E_pokemon == 5:
            self.movie = QMovie("gadi.gif")
            self.bettlepokemon_2.setMovie(self.movie)
            self.movie.start()
        elif Variable.E_pokemon == 6:
            self.movie = QMovie("mue.gif")
            self.bettlepokemon_2.setMovie(self.movie)
            self.movie.start()
        elif Variable.E_pokemon == 7:
            self.movie = QMovie("ninja.gif")
            self.bettlepokemon_2.setMovie(self.movie)
            self.movie.start()
        elif Variable.E_pokemon == 8:
            self.movie = QMovie("man.gif")
            self.bettlepokemon_2.setMovie(self.movie)
            self.movie.start()
        elif Variable.E_pokemon == 9:
            self.movie = QMovie("purin.gif")
            self.bettlepokemon_2.setMovie(self.movie)
            self.movie.start()








        self.run.clicked.connect(self.running)
        self.skill1.clicked.connect(self.ski1)
        # self.skill2.clicked.connect(self.ski2)
        # self.skill3.clicked.connect(self.ski3)
        # self.skill1.clicked.connect(self.battle)
        # self.skill2.clicked.connect(self.battle)
        # self.skill3.clicked.connect(self.battle)


    # def ski1(self):
    #     print("{}의 {}!\n{}의 데미지!".format(pokemons[Variable.S_pokemon].name, pokemons[Variable.S_pokemon].skill_1_name, pokemons[Variable.S_pokemon].skill_1))
    #     Epokemons[Variable.E_pokemon].n_hp -= pokemons[Variable.S_pokemon].skill_1
    #     print("{}의 남은 체력 {}\n".format(Epokemons[Variable.E_pokemon].name, Epokemons[Variable.E_pokemon].n_hp))
    #     if Epokemons[Variable.E_pokemon].n_hp <= 0:
    #         print("{}은 쓰러졌다. {}은 적을 물리쳐서 슬프다 힝힝".format(Epokemons[Variable.E_pokemon].name, pokemons[Variable.S_pokemon].name))
    #         self.Poket3 = Poket3()
    #         self.Poket3.show()
    #         self.close()


    #
    # def ski2(self):
    #     print("{}의 {}!\n{}의 데미지!".format(pokemons[Variable.S_pokemon].name, pokemons[Variable.S_pokemon].skill_2_name,
    #                                      pokemons[Variable.S_pokemon].skill_2))
    #     Epokemons[Variable.E_pokemon].n_hp -= pokemons[Variable.S_pokemon].skill_2
    #     print("{}의 남은 체력 {}\n".format(Epokemons[Variable.E_pokemon].name, Epokemons[Variable.E_pokemon].n_hp))
    #     if Epokemons[Variable.E_pokemon].n_hp <= 0:
    #         print("{}은 쓰러졌다. {}은 적을 물리쳐서 슬프다 힝힝".format(Epokemons[Variable.E_pokemon].name, pokemons[Variable.S_pokemon].name))
    #         self.Poket3 = Poket3()
    #         self.Poket3.show()
    #         self.close()

    # def ski3(self):
    #     print("{}의 {}!\n{}의 데미지!".format(pokemons[Variable.S_pokemon].name, pokemons[Variable.S_pokemon].skill_3_name,
    #                                      pokemons[Variable.S_pokemon].skill_3))
    #     Epokemons[Variable.E_pokemon].n_hp -= pokemons[Variable.S_pokemon].skill_3
    #     print("{}의 남은 체력 {}\n".format(Epokemons[Variable.E_pokemon].name, Epokemons[Variable.E_pokemon].n_hp))
    #     if Epokemons[Variable.E_pokemon].n_hp <= 0:
    #         print("{}은 쓰러졌다. {}은 적을 물리쳐서 슬프다 힝힝".format(Epokemons[Variable.E_pokemon].name, pokemons[Variable.S_pokemon].name))
    #         self.Poket3 = Poket3()
    #         self.Poket3.show()
    #         self.close()
    #
    # def battle(self):
    #     if Epokemons[Variable.E_pokemon].n_hp > 0:
    #         print("{}의 {}!\n{}의 데미지!".format(Epokemons[Variable.E_pokemon].name, Epokemons[Variable.E_pokemon].skill_1_name, Epokemons[Variable.E_pokemon].skill_1 ))
    #         pokemons[Variable.S_pokemon].n_hp -= Epokemons[Variable.E_pokemon].skill_1
    #         print("{}의 남은 체력 {}\n".format(pokemons[Variable.S_pokemon].name, pokemons[Variable.S_pokemon].n_hp))

    def ski1(self):

        #self.Enermy.Hp_e -= MyPo.attack
        #적 hp_e -= 우리 공격
        #self.enemyHPprogressBar.setValue(Enermy.Hp_e)

        Epokemons[0].n_hp -= randint(20,40)
        self.progressBar_1.setValue(Epokemons[0].n_hp)






    def running(self): #도망가기
        self.Poket3 = Poket3()
        self.Poket3.show()
        self.close()




class Poket3(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None)
        loadUi(ui3, self)
        if Variable.S_pokemon == 0:
            self.movie = QMovie("pikag.gif")
            self.poket.setMovie(self.movie)
            self.movie.start()
        elif Variable.S_pokemon == 1:
            self.movie = QMovie("eveg.gif")
            self.poket.setMovie(self.movie)
            self.movie.start()
        elif Variable.S_pokemon == 2:
            self.movie = QMovie("strange.gif")
            self.poket.setMovie(self.movie)
            self.movie.start()
        elif Variable.S_pokemon == 3:
            self.movie = QMovie("gogog.gif")
            self.poket.setMovie(self.movie)
            self.movie.start()

        self.poket_info.append("이름 : {}".format(pokemons[Variable.S_pokemon].name))
        self.poket_info.append("HP : {} / {}".format(pokemons[Variable.S_pokemon].n_hp, pokemons[Variable.S_pokemon].hp))
        self.poket_info.append("MP : {} / {}".format(pokemons[Variable.S_pokemon].n_mp, pokemons[Variable.S_pokemon].mp))
        self.poket_info.append("EXP : {} / {}".format(pokemons[Variable.S_pokemon].n_exp, pokemons[Variable.S_pokemon].exp))

        self.go_fight.clicked.connect(self.fight)


    def fight(self):
        a = randint(0, 9)
        Variable.E_pokemon = a
        self.Poket4 = Poket4()
        self.Poket4.show()
        self.close()








class Poket2(QMainWindow):
    global name
    def __init__(self):
        QMainWindow.__init__(self, None)
        loadUi(ui2, self)
        self.movie = QMovie("ohoh.gif")
        self.ohoh_label.setMovie(self.movie)
        self.movie.start()

        self.pika_btn.clicked.connect(self.pika)
        self.pika_btn.clicked.connect(self.show_3)
        self.eve_btn.clicked.connect(self.eve)
        self.eve_btn.clicked.connect(self.show_3)
        self.sang_btn.clicked.connect(self.sang)
        self.sang_btn.clicked.connect(self.show_3)
        self.ggo_btn.clicked.connect(self.ggo)
        self.ggo_btn.clicked.connect(self.show_3)

    def pika(self):
        Variable.S_pokemon = 0

    def eve(self):
        Variable.S_pokemon = 1

    def sang(self):
        Variable.S_pokemon = 2

    def ggo(self):
        Variable.S_pokemon = 3


    def show_3(self):
        self.Poket3 = Poket3()
        self.Poket3.show()
        self.close()






class Poket1(QMainWindow) :

    def __init__(self):
        QMainWindow.__init__(self, None)
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



app = QApplication(sys.argv)
myWindow = Poket1()
myWindow.show()
app.exec_()