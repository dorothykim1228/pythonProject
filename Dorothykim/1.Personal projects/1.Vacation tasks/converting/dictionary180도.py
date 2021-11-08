'''dictionary= {

    "떡볶이" : "4000",
    "라면" : "3500",
    "순대" : "4000",
}

key = input("> 접근하고자 하는 키:")
if key in dictionary:
    print(dictionary[key])
else:
    print("존재하지 않는 키에 접근하고 있습니다.")


#리스트를 선언합니다.
list_a = [1,2,3]

#리스트 뒤에 요소 추가하기
print("# 리스트 뒤에 요소 추가하기")
list_a.append(5)
list_a.append(6)
print(list_a)
print()

#리스트 중간에 요소 추가하기
print("리스트 중간에 여서 추가하기")
list_a.insert(3,4)
print(list_a)


list_c= []
list_a = [1,2,3,4,5]
list_b = [6,7,8,9,10]
list_c.append(list_a)
list_c.append(list_b)
print(list_c)

#변수 선언

array = [i * i for i in range(0, 20,2)]

print(array)

array = ["사과", "자두", "초콜릿", "바나나","체리"]
output = [fruit for fruit in array if fruit != "초콜릿"]

print(output)

#함수 선언
example_dictionary={
    "키A" : "값A",
    "키B" : "값B",
    "키C" : "값C",
}
#딕셔너리 items()함수 결과 출력
print("#딕셔너리의 items()함수")
print("items():", example_dictionary.items())
print()

#for반복문과 items()함수 조합해서 사용
print("#딕셔너리의 items() 함수와 반복문 조합하기")

for key, element in example_dictionary.items():
    print("dictionary[{}] ={}".format(key,element))

#break 키워드

i=0 #변수 선언

while True:
    print("{}번쨰 반복문입니다.".format(i))
    i=i+1
    input_txt =input(">종료하시겠습니까?(y/n): ")
    if input_txt in ["y","Y"]:
        print("반복을 종료합니다.")
        break

numbers = [5,15,6,20,7,25]

for number in numbers:
    if number < 10:
         continue
    print(number)

list_c= []
list_a = [1,2,3,4,5]
list_b = [6,7,8,9,10]
list_c.append(list_a)
list_c.append(list_b)
print(list_c)
'''






'''
for i in range(5):
    list_aa = [i for i in range(a, b)]
    list_doro.append(list_aa)
    a += 5
    b += 5
    for k in reversed(list_doro):
        print(k)


'''


list_doro = []
a = 21
b = 26

for i in range(5):
    list_aa = [i for i in reversed(range(a, b))]
    list_doro.append(list_aa)
    a -= 5
    b -= 5

print(list_doro)


