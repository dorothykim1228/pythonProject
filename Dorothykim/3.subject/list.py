"""

#날짜, 시간

import datetime
now = datetime.datetime.now()

if now.hour < 12:
    print("현재 시간은 {}시로 오전입니다.".format(now.hour, now.minute))
if now.hour >= 12:
    print("현재 시간은 {}시로 오후입니다.".format(now.hour, now.minute))

if  3 <= now.month <=5:
    print("이번 달은 {}월로 봄입니다".format(now.month))
if  6 <= now.month <=8:
    print("이번 달은 {}월로 여름입니다".format(now.month))
if  9 <= now.month <=11:
    print("이번 달은 {}월로 가을입니다".format(now.month))
if  12 <= now.month <=2:
    print("이번 달은 {}월로 겨울입니다".format(now.month))

print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)


# 홀수 짝수
number = input("정수를 입력해주세요:")
number = int(number)


if number % 2 == 0:
    print("짝수입니다")
if number % 2 == 1:
    print("홀수입니다")



score = float(input(">학점을 입력해주세요:"))

if score == 4.5:
    print("신")
elif 4.2 <= score:
    print("교수의 사랑")
else:
    print("없음")


# 리스트에 요소 추가하기
list_a = [1,2,3]

print("리스트 뒤에 요소 추가")
list_a.append(4)
list_a.append(5)
print(list_a)
print()

#인덱스로 제가
#1. del 연산자
#2. pop()함수
# 값으로 제거
# 1. remove()함수

a=[1,2,3,4,5,6,7]
print(a)
del a[0:3]
print(a)

a=[1,2,3,4,5,6,7]
a.pop(1)
print(a)

a=[100,200,300,400,500]
a.remove(100)
print(a)

a=[1,2,3,4,5,6,7]
a.clear()
print(a)


#for<요소 변수 이름> in 리스트:

a = [1,2,3,4,5,6,7,]

for element in a:
    print(element)

numbers = [273,103,5,332,65,9,72,800,99]

for number in numbers:
    if number >= 100:
        print("-100 이상의 수: {}".format(number))

for number in numbers:
    if number % 2 == 0:
        print("{}는 짝수 입니다".format(number))
    else:
        print("{}는 짝수 입니다".format(number))

for number in numbers:
    print("{}는 {} 자리수입니다.".format(number,len(str(number))))

list_of_list =[
    [1,2,3],
    [4,5,6,7],
    [8,9]
    ]

for a in list_of_list:
    [1,2,3] > [4,5,6,7] > [8,9]
    for b in a:
        1,2,3//4,5,6,7//8,9
        print(b)

for number in numbers:
    1,2,3,4,5,6,7,8,9
output=[(number-1)%3].append(number)
print(output)

holzzak = ["짝수","홀수"]
for number in numbers:
    print("{}는 {}입니다.".format(number,holzzak[number % 2]))



#딕셔너리 선언
딕셔너리 = {
    "문자열" : "값",
    273: [1,2,3,4],
}
#반복문
for key in 딕셔너리:
    print("{} : {}".format(key,딕셔너리[key]))
#요소 추가
딕셔너리["키"] = "값"
print()
for key in 딕셔너리:
    print("{} : {}".format(key,딕셔너리[key]))
#요소 제거
del 딕셔너리 ["키"]
print()
for key in 딕셔너리:
    print("{} : {}".format(key, 딕셔너리[key]))

pets = [
    {"name" : "구름","age":5 },
    {"name": "초코", "age": 3},
    {"name": "아지", "age": 1},
    {"name": "호랑이", "age": 1}
    ]
print("우리동네 애완 동물들")
for pet in pets:
    print("{}{}살".format(pet["name"], pet["age"]))



numbers =[1,2,6,8,3,2,1,9,5,4,9,7,2,1,3,5,4,8,9,7,2,3]
counter = {}

for number in numbers:
    if number in counter:
        counter[number] += 1
    else:
        counter[number] = 1
print(counter)

character = {
    "name" : "기사",
    "level" : 12,
    "items" : {
        "sword" : "불꽃의 검",
        "armor": "풀플레이트"
    },
        "skill" : ["베기","세게 베기","아주 세게 베기"]
}

#for 반복문 사용
for key in character:
    if type(character[key]) is dict:
        for k in character[key]:
            print("{} : {}".format(k,character[key][k]))
    elif type(character[key]) is dict:
       for item in character[key]:
           print("{} : {}".format(key,item))
    else:
        print("{} : {}.format(key,character[key]")

#range(시작, 끝, 단계)
#range(시작,끝) #단계 =1 생략
#range(끝) 시작=0 과 단계=1 생략

for i in range(0,10,1):  #특정 횟수를 반복함
    print(i)

"""

numbers = [1,2,1,2,1,2,1,2]

while 1 in numbers:
    numbers.remove(1)
print(numbers)


# 5초 대기후 프로그램이 종료
import time

처음 = time.time()
while 처음 + 5 >=  time.time():
    pass
print("프로그램이 종료되었습니다")