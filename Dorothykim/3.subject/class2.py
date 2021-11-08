
# 클래스 호출

class Student:
    def __init__(self):
        print("학생 생성자 실행")
        print("학생 클래스가 호출될 때 실행")
        self.math = 0
        python = 0

class Professor:

    def __init__(self):
        print("교수 생성자 실행")
        print("교수 클래스가 호출될 때 실행")
        self.pay=0
    python = 0

class University:
    def __init__(self):
        print("university 실행")

        student = student()
        student.python = 100


uni = University()
pro = Professor()
stu = Student()

pro.pay = 1000000
pro.python = 90

print(pro.pay)
print(stu.python)





# 상속의 활용

    #부모의 클래스 선언

class Parent:
    def __init__(self):
        self.value = "테스트"
        print("Parent 클래스의 __init()__ 메소드가 호출되었습니다.")
    def test(self):
        print("Parent 클래스의 test() 메소드입니다.")
    #자식 클래스 선언

class Child(Parent):
    def __init__(self):
        Parent.__init__(self)
        print("Child 클래스의 __init()__ 메소드가 호출되었습니다.")

#자식 클래스의 인스턴스를 생성하고 부모의 메소드를 호출
child = Child()
child.test()
print(child.value)

#사용자 정의 예외 클래스 만들기
class CustomException(Exception):
    def __init__(self):
        Exception.__init__(self)
        print("#####내가 만든 오류가 생성####")
    def __str__(self):
        return "오류가 발생하였습니다"
raise CustomException



#isinstance() 함수 활용

class Student:
    def study(self):
        print("공부를 합니다")

#선생님 클래스 선언
class Teacher:
    def teach(self):
        print("학생을 가르칩니다")

#교실 내부의 객체 리스트를 생성
classroom = [Student(), Student(), Teacher(), Student(),Student()]

# 반복을 적용해서 적절한 함수를 호출
for person in classroom:
    if isinstance(person, Student):
        person.study()
    elif isinstance(person, Teacher):
        person.teach()

#__str__()함수

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
        return self.get_sum() /4
    def __str__(self):
        return "{}\t{}\t{}".format(self.name,self.get_sum(),self.get_average())

# 학생 리시트 선언
students = [
    Student("윤인성",87,98,88,95),
    Student("연하진",92,98,96,98),
    Student("구지연",76,96,94,90),
    Student("나선주",98,92,96,92),
    Student("윤아린",95,98,98,98),
    Student("윤명월",64,88,92,92)
]

#출력
print("이름","총점","평균", sep="\t")
for student in students:
    print(str(student))




class Professor:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science


professors = [
    Professor("윤인성",87,98,88,95),
    Professor("연하진",92,98,96,98),
    Professor("구지연",76,96,94,90),
    Professor("나선주",98,92,96,92),
    Professor("윤아린",95,98,98,98),
    Professor("윤명월",64,88,92,92)
]


print("이름","총점","평균",sep="\t")
for p in professors:
    print(str(p))