
#예외 객체
#try except 구문으로 예외처리
try:
    #숫자로 변환
    number_input_a = int(input("정수입력>"))
    #출력
    print("원의 반지름:", number_input_a)
    print("원의 둘레:", 2*3.14*number_input_a*number_input_a)
    print("원의 넓이:", 3.14 * number_input_a * number_input_a)
except exception as exception:
    #예외 객체 출력
    print("type(exception):", type(exception))
    print("exception:", exception)

# 여러가지 예외가 발생할수 있는 코드
    # 변수선언

list_number = [52, 273, 32, 72, 100]
    #try except 구문으로 예외 처리
try:
    #숫자 입력
    number_input = int(input("정수 입력>"))
    #리스트 요소 출력
    print("{}번째 요소: {}".format(number_input, list_number[number_input]))
except ValueError:
    print("정수 입력")
except IndexError:
   print("리스트의 인덱스를 벗어났어요")


#변수 선언
import datetime

list_number = [52, 273, 32, 72, 100]
    #try except 구문으로 예외 처리

def write_log(exception):
    file = open("log.txt",'a') #파일을 연다('a'파일에 마지막줄에 추가하는 옵션)
    #파일에 쓸 내용을 변수에 적는 과정(exception의 type과 내용)
    logtext ="\n{},{},{}".format(datetime.datetime.now(),type(exception),exception)
    file.write(logtext)
    #위의 내용을 파일에 쓴다
    #파일을 닫는다
    file.close()
try:
    #숫자 입력
    number_input = int(input("정수 입력>"))
    #리스트 요소 출력
    print("{}번째 요소: {}".format(number_input, list_number[number_input]))
    예외.발생해주세요()
except ValueError as exception:
    #value error가 발생할 경우
    print("정수 입력")
    print(type(exception),exception)
    write_log()
except IndexError as exception:
    #index error가 발생할 경우
    print("리스트 인덱스를 벗어남")
    print(type(exception),exception)
    write_log()
except Exception as exception:
    #이외의 예외가 발생할 경우
    print("미리 파악하지 못한 예외가 발생")
    print(type(exception),exception)
    write_log()




#딕셔너리로 객체 만들기

#학생 리스트 선언

student =[
    {"name":"윤인상","korean": 87,"math": 98 ,"english": 88 ,"science": 95},
    {"name":"연하진","korean": 92,"math": 98, "english": 96,"science": 98},
    {"name":"구지연","korean": 76,"math": 96, "english": 94,"science": 90},
    {"name":"나선주","korean": 98,"math": 92, "english": 96,"science": 92},
    {"name":"윤아린","korean": 95,"math": 98, "english": 98,"science": 98},
    {"name":"윤명월","korean": 64,"math": 92, "english": 92,"science": 92}
]

#학생을 한명씩 반복
print("이름", "총점", "평균", "math", sep = "\t")

for student in student:
    #w점수의 총합과 평균을 구합니다

    score_sum = student["korean"] + student["math"] +\
                student["english"] +student["science"]
    score_average= score_sum/4
    score_math = student["math"]
    #출력
    print(student["name"],score_sum,score_average, score_math, sep = "\t" )



#각 과목들의 평균과 최소점 최고점을 구하기

scores = {"korean": [87,92,76,98,95,64], "math": [98,98,96,92,98,88],
        "english": [88,96,94,96,98,92], "science": [95,98,90,98,92],
        "python": [80,85,96,100,60,70]}

for key, element in scores.items():
    print("과목:{}, 평균:{}, 최고점:{}, 최소점:{}".format({key},sum(element)/len(element),max(element),min(element)))



#class

#클래스 선언
class student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

#학생리스트 선언
students =[

    student("윤인성", 87,98,88,95),
    student("연하진", 92,98,96,88),
    student("구지연", 76,96,94,90),
    student("나선주", 98,92,96,92),
    student("윤아린", 95,98,98,98),
    student("윤명월", 64,88,92,92)
    ]

#student 인스턴스의 속성에 접근하는 방법
students[0].name
students[0].korean
students[0].math
students[0].english
students[0].science

for student in students:
    print(student.name,student.korean,student.math,student.english,student.science)


#클래스 내부에 함수(메소드)선언
    #클래스 선언

class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
    def get_sum(self):
        return self.korean + self.math + self.english + self.science

    def get_average(self):
        return self.get_sum()/4
    def to_string(self):
        return "{}\t{}\t{}".format(self.name,self.get_sum(),self.get_average())

#학생 리스트 선언

students = [
    Student("윤인성", 87, 98, 88, 95),
    Student("연하진", 92, 98, 96, 88),
    Student("구지연", 76, 96, 94, 90),
    Student("나선주", 98, 92, 96, 92),
    Student("윤아린", 95, 98, 98, 98),
    Student("윤명월", 64, 88, 92, 92)
]
    #학생을 한명씩 반복
print("이름","총점","평균",sep="\t")
for a in students:
    #출력
    print(a.to_string())