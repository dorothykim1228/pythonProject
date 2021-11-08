#모듈

#random 모듈

import random
print("# random 모듈")

# random(): 0.0 <= x <1.0 사이의 float를 리턴
print("-random():", random.random())

#uniform(min,max) : 지정한 범위 사이의 float를 리턴
print("-uniform(10,20):", random.uniform(10,20))

#randrange(): 지정한 범위의 int를 리턴
#-randrange(max) : 0부터 max 사이의 값 리턴
#-randrange(min, max) : min부터 max 사이의 값 리턴
print("-choice([1,2,3,4,5]):",random.choice([1,2,3,4,5]))

#shuffle(list): 리스트의 요소들을 랜덤으로 섞음
print("-shuffle([1,2,3,4,5]):", random.shuffle([1,2,3,4,5]))

#sample(list, k=<숫자>): 리스트 요소 중에 k를 뽑음
print("-sample([1,2,3,4,5], k=2):", random.sample([1,2,3,4,5], k=2))



#sys 모듈

#모듈을 읽어 들임

import sys

#명령 매개변수 출력
print(sys.argv)
print("---")

#컴퓨터 환경과 관련된 정보 출력
print("getwindowsversion:()", sys.getwindowsversion())
print("---")
print("copyright:", sys.copyright)
print("---")
print("version:", sys.version)

# 프로그램 강제종료
sys.exit()



#datetime 모듈

#모듈을 읽음
import datetime

#현재 시각을 구하고 출력
print("#현재 시각 출력")
now = datetime.datetime.now()
print(now.year, "년")
print(now.month, "월")
print(now.day, "일")
print(now.hour, "시")
print(now.minute, "분")
print(now.second, "초")
print()

#시간 출력 방법
print("# 시간을 포맷에 맞춰 출력하기")
output_a = now.strfttime("%Y.%m.%d $H:%M:%S")
output_b = "{}년 {}월 {}일 {}시 {}분 {}초".format(now.year,\now.month,\now.day,\now.hour,\now.minute,\now.second)
output_c = now.strfttime("%Y.%m.%d %H:%M:%S").format(*"년월일시분초")

print(output_a)
print(output_b)
print(output_c)
print



#time 모듈

import time

print("지금부터 5초 동안 정지합니다!")
time.sleep(5)
print("프로그램을 종료합니다")

# 시간 처리하기
import datetime
now = datetime.datetime.now()

# 특정시간 이후의 시간 구하기
print(" #datetime.timedelta로 시간 더하기")
after = now +datetime.timedelta(\
    weeks=1,
    days=1,\
    hours=1,\
    minutes=1,\
    seconds=1)
print(after.strftime(("%Y{}%m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초"))
print()

# 특정 시간 요소 교체하기
print("#now.replace()로 1년 더하기")
output = now.replace(year = (now.year + 1 ))
print(output.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초"))





#urllib 모듈

#모듈 읽기
from urllib import request

target = request.urlopen("https://google.com")
output =target.read()

#출력
print(output)

#beautifulsoup 모듈로 날씨 가져오기
#모듈울 앍어옴

from urllib import request
from bs4 import BeautifulSoup

# urlopen()함수로 기상청의 전국 날씨를 읽음
target = request.urlopen("http: www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")

#BeautifulSoup을 사용해 웹 페이지를 분석함
soup = BeautifulSoup(target, "html.parser")

#location 태그 찾음
for location in soup.select("location"):
    #내부의 city,wf,tmn,tmx 태그를 찾아 출력
    pirnt("도시:", location.select_one("city").string)
    pirnt("날씨:", location.select_one("wf").string)
    pirnt("최저기온:", location.select_one("tmn").string)
    pirnt("최고기온:", location.select_one("tmx").string)
    print()



#함수데코레이터
def test(function):
    def wrapper():
        print("인사가 시작되었습니다.")
        function()
        print("인사가 종료되었습니다.")
    return wrapper
#데코레이터를 붙여 함수를 만듬
@test
def hello():
    print("hello")

#함수 호출
hello()



#flask 모듈 사용하기

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1> hello world!</h1>"


