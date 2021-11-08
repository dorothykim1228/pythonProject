# 튜플(tuple)
# 리스트와 튜플의 특이한 사용

[a,b] = [10,20]
(c,d) =  (10,20)

# 출력
print("a:",a)
print("b:",b)
print("c:",c)
print("d:",d)

# 괄호가 없는 튜플
tuple_test = 10,20,30,40
print("#괄호가 없는 튜플의 값과 자료형 출력")
print("tuple_test:", tuple_test)
print("type(tuple_test):", type(tuple_test))
print()

# 괄호가 없는 튜플 활용
a,b,c = 10,20,30
print("#괄호가 없는 튜플을 활용한 할당")
print("a:",a)
print("b:",b)
print("c:",c)

# 변수의 값을 교환하는 튜플
a,b = 10,20

print("#교환 전 값")
print("a:", a)
print("b:", b)
print()

# 값 교환
a,b = b,a

print("# 교환 후 값")
print("a:", a)
print("b:", b)
print()

# 튜플과 함수: 함수의 리턴에 튜플을 사용하면 여러 개의 값을 리턴하고 할당 가능
# 여러개의 값 리턴하기
    # 함수선언
def test():
    return (10,20)
#여러개의 값을 리턴
a,b = test()

#출력
print("a:",a)
print("b:",b)

# 람다(lambda): 익명 함수(anonymous function)를 생성하기 위한 함수

# 함수의 매개변수로 함수 전달하기
    # 매개 변수로 받은 함수를 10번 호출하는 함수
def call_10_times(func):
    for i in range(10):
        func()
# 간단한 출력하는 함수
def print_hello():
    print("안녕하세요")

# 조합하기
call_10_times(print_hello)

# map()함수와 filter()함수
# 함수선언
def power(item):
    return item*item
def under_3(item):
    return item<3
# 변수 선언
list_input_a = [1,2,3,4,5]

# map()함수 사용
output_a = map(power,list_input_a)
print("# map() 함수의 실행결과")
print("map(power, list_input_a):", output_a)
print("map(power, list_input_a):", list(output_a))
print()

# filter 함수사용
output_b = filter(under_3,list_input_a)
print("# filter() 함수의 실행결과")
print("filter(under_3, list_input_a):", output_b)
print("map(under_3, list_input_a):", list(output_b))
print()

# 람다식으로 변환
    # 함수 선언
power = lambda x:x*x
under_3 = lambda  x:x < 3
# 변수 선언
list_input_a = [1,2,3,4,5]

# map()함수 사용
output_a = map(power,list_input_a)
print("# map() 함수의 실행결과")
print("map(power, list_input_a):", output_a)
print("map(power, list_input_a):", list(output_a))
print()

# filter 함수사용
output_b = filter(under_3,list_input_a)
print("# filter() 함수의 실행결과")
print("filter(under_3, list_input_a):", output_b)
print("map(under_3, list_input_a):", list(output_b))
print()


# 파일 처리: (w: write 모드[새로 쓰기 모드], a: append 모드[뒤에서 이어서 쓰기모드], r : read 모드[읽기모드])
# 파일 열고 닫기
# 파일을 엽니다

file = open("basic.txt", "w")
# 파일에 텍스트를 씀
file.write("hello Python programming...!")
# 파일을 닫음
file.close()

# file open <with open("basic.txt","w") as file>
# text in file <file.write("hello Python programming...!")>

# read() 함수로 텍스트 읽기
# 파일 오픈
with open("basic.txt", "r") as file:
    # 파일을 읽고 출력
    contents = file.read()
print(contents)

# 랜덤하게 1000명의 키와 몸무게 만들기
# 랜덤한 숫자를 만들기 위해 가져옴
import random
hanguls = list("가나다라마바사아자차카타파하")

with open("info.txt","w")as file:
    for i in range(1000):
        name = random.choice(hanguls) + random.choice(hanguls)
        weight = random.randrange(40, 100)
        height = random.randrange(140, 200)

        file.write("{},{},{}\n".format(name,weight,height))


#반복문으로 파일 한 줄씩 읽기

with open("info.txt","r")as file:
    for line in file:
        #변수 선언
        (name, weight,height) = line.strip().split(",")

        #데이터 문제 확인: 문제 없을시 pass
        if (not name) or (not weight) or (not height):
            continue
            #결과 계산
            bmi = int(weight)/ ((int(height)/ 100) ** 2)
            result = ""
            if 25<= bmi:
                result = "과체중"
            elif 18.5<= bmi:
                result = "정상 체중"
            else:
                result = "저체중"
            #출력
            print('\n'.join(["이름: {}","몸무게:{}", "키:{}", "bmi:{}","결과:{}"]).format(name, weight,height, bmi,result))
            print()

#제너레이터 객체와 next()함수
    # 함수 선언
def test():
    print("A지점 통과")
    yield 1
    print("B지점 통과")
    yield 2
    print("C지점 통과")
    # 함수 호출
output =test()
#next()함수 호출
print("D지점 통과")
a = next(output)
print(a)
print("E지점 통과")
b = next(output)
print(b)
print("F지점 통과")
#c= next(output)
#print(c)
# 한번더 실행
#next(output)

#예외 상황 확인하기
#숫자 입력
""""
number_input_a = int(input("정수 입력>"))

#출력
print("원의 반지름:", number_input_a)
print("원의 둘레:", 2*3.14*number_input_a)
print("원의 넓이:", 3.14 *number_input_a*number_input_a )

#try except구문
    # try except 구문으로 예외처리

try:
    #숫자 변환
    number_input_a = int(input("정수 입력>"))
# 출력
    print("원의 반지름:", number_input_a)
    print("원의 둘레:", 2*3.14*number_input_a)
    print("원의 넓이:", 3.14 *number_input_a*number_input_a )
except:
    print("무언가 잘못되었습니다.")
"""

#숫자로 변환되는 것들만 리스트 넣기
    #변수 선언
list_input_a = ["52","273","32","스파이","103"]

    #반복적용
list_number = []
for item in list_input_a:
    #숫자 변환해서 리스트 추가

    try:
        float(item)#예외 발생시 알아서 다음진행 안됨
        list_number.append(item)
    except:
        pass
#출력
print("{}내부에 있는 숫자는".format(list_input_a))
print("{}입니다.".format(list_number))

# finally 구문
# try except 구문으로 예외처리 된다
try:
    #숫자 변환
    number_input_a = int(input("정수 입력>"))
# 출력
    print("원의 반지름:", number_input_a)
    print("원의 둘레:", 2*3.14*number_input_a)
    print("원의 넓이:", 3.14 *number_input_a*number_input_a )
except:
    print("정수 입력력하세요")
else:
    print("예외가 발생하지 않았습니다.")
finally:
    print("일단 프로그램이 어떻게든 끝났습니다.")

#파일이 제대로 닫혔는지 확인

try:
    #파일 open
    file = open("info.txt","w")
    #여러가지 처리 수행
    #파일 닫음
    file.close()
except exception as ee:
    print(e)
print("#파일이 제대로 닫혔는지 확인하기")
print("file.closed:", file.closed)








# finally 키워드 활용
 #함수선언
def write_text_file(filename, text):
    #try except 구문 사용
    try:
        #파일을 연다.
        file = open(filename,"w")
        #여러가지 처리 수행
        return
        #팦일에 텍스트 입력
        file.write(text)
    except exception as e:
        print(e)
    finally:
        #파일 닫음
        file.close()
#함수 호출
write_text_file("text.txt","안녕하세요!")