# 상속의 활용

    #부모의 클래스 선언

class Parent:
    def __init__(self):
        self.value = "테스트"

    def test(self):
        print("Parent 클래스의 test() 메소드입니다.")
    #자식 클래스 선언

class Child(Parent):
    def __init__(self):
        Parent.__init__(self)


#자식 클래스의 인스턴스를 생성하고 부모의 메소드를 호출
child = Child()
child.test()
