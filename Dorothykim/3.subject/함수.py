#매개변수의 기본

def print_n_times(value, n):
    #n번 반복
    for i in range(n):
        print(value)

print_n_times("안녕하세요",5)


#가변 매개변수 함수
def print_n_times(n,*values):
    #n번 반복
    for i in range(n):
        #values는 리스트처럼 활용
        for value in values:
            print(value)
            #단순 줄 바꿈
            print()
#함수 호출
print_n_times(3, "안녕하세요","즐거운", "파이썬 프로그래밍")


def print_n_times(value, n=2):
    for i in range(n):
        print(value)

print_n_times("안녕하세요")



##키워드 매개변수와 가변매개변수를 활용
##유저로 부터 입력받는 값을 배개변수로 실행해야되는 함수
##유저가 잘못입력하거나 예측하지 못하게 입력하는 걸 방지 할 수 있음

def print_n_times(*values, n=2):
    for i in range(n):
        for value in values:
            print(value)
        print()

print_n_times("안녕하세요","즐거운","파이썬 프로그래밍")



def test(a, b=10, c=100):
    print(a +b+ c)

    #1)기본형태
    test(10,20,30)
    #2)키워드 매개변수로 모든 매개변수를 지정한 형태
    test(a=10, b=100, c=200)
    #3)키워드 매개변수로 모든 매개변수를 마구잡이로 지정한 형태
    test(c=10, a=100, b=200)
    #4)키워드 매개변수로 일부 매개변수만 지정한 형태
    test(10, c=200)




def test(a, b=10, c=100):
    print(a +b+ c)

#1)기본형태
test(10,20,30)
#2)키워드 매개변수로 모든 매개변수를 지정한 형태
test(a=10, b=100, c=200)
#3)키워드 매개변수로 모든 매개변수를 마구잡이로 지정한 형태
test(c=10, a=100, b=200)
#4)키워드 매개변수로 일부 매개변수만 지정한 형태
test(10, c=200)


#함수 내에서 어떤 시전이나 코드에서 바로 함수를 끝내고 싶을때 return을 활용한다.
def return_test(n):
    if(n==2):
        print("A 위치입니다.")
        return
    print("B 위치입니다.")

return_test(2)


#범위 내부의 정수를 모두 더하는 함수
#함수 선언
def sum_all(start,end):
    #변수 선언
    output = 0
    #반복문을 돌려 숫자를 더함
    for i in range(start, end+1):
        output += i
    #값을 리턴
    return output
#함수 호출
print("0 to 100:", sum_all(0,100))
print("0 to 1000:", sum_all(0,1000))
print("50 to 100:", sum_all(50,100))
print("500 to 1000:", sum_all(500,1000))


#기본 매개변수와 키워드 매개변수 활용해 범위의 범수 더하는 함수
#함수 선언
def sum_all(start=0, end=100, step=1):
    #변수 선언
    output = 0
    #반복문을 돌려 숫자 더함
    for i in range(start, end +1, step):
        output += i
    #리턴
    return output
#함수 호출
print("A.", sum_all(0,100,10))
print("B.", sum_all(end=100))
print("C.", sum_all(end=100, step=2))

#반복문으로 팩토리얼 구하기
#함수 선언
def factorial(n):
    #변수 선언
    output = 1
    #반복문을 돌려 숫자를 더함
    for i in range(1, n+1):
        output *= i
    #리턴
    return output
#함수 호출
print("1!:", factorial(1))
print("2!:", factorial(2))
print("3!:", factorial(3))
print("4!:", factorial(4))
print("5!:", factorial(5))

#재귀함수 사용해 팩토리얼 구하기

#함수선언
def factorial(n):
#n이 0이라면 1을 리턴
    if n == 0:
        return 1
#n이 0이 아니라면 n*(n-1)!을 리턴
    else:
        return n * factorial(n-1)
#함수 호출
print("1!:", factorial(1))
print("2!:", factorial(2))
print("3!:", factorial(3))
print("4!:", factorial(4))
print("5!:", factorial(5))


#재귀 함수로 구현한 피보나치 수열(1)
#함수 선언
def fibonacci(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
#함수호출
print("fibonacci(1):",fibonacci(1))
print("fibonacci(2):",fibonacci(2))
print("fibonacci(3):",fibonacci(3))
print("fibonacci(4):",fibonacci(4))
print("fibonacci(5):",fibonacci(5))



#재귀 함수로 구현하는 피보니나치 수열(2)
#변수 선언
counter = 0
#함수 선언
def fibonacci(n):
    #어떤 피보나치 수를 구하는지 출력
    print("fibonacci({})를 구합니다.".format(n))
    global counter
    counter += 1
    #피보나치 수 구함
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
#함수 호출
fibonacci(10)
print("---")
print("fibonacci(10) 계산에 활용된 덧셈 횟수는 {}번입니다.".format(counter))


#메모화
#메모 변수

dictionary = {
    1: 1,
    2: 1
}
#함수선언
def fibonacci(n):
    if n in dictionary:
       #메모가 있으면 메모된 값 리턴
        return dictionary[n]
    else:
        #메모가 없으면 값을 구함
        output = fibonacci(n-1) + fibonacci(n-2)
        dictionary[n] = output
        return output

#함수 호출
print("fibonacci(10):", fibonacci(10))
print("fibonacci(20):", fibonacci(20))
print("fibonacci(30):", fibonacci(30))
print("fibonacci(40):", fibonacci(40))
print("fibonacci(50):", fibonacci(50))




