# making 99dan

print("========================Start========================")

for i in range(2,10):
    print(" {}단 start.".format(i))
    for j in range(1,10):
            print("{}*{}={}".format(i,j,i*j))

# odd number and even number
# 1. odd number
# i: multiplication
# j: dan number


# J : 홀수, 짝수
print("==================Odd or Even number===================")
dan = int(input(" which dan would you like to select ? \n (1) odd number (2) even number "))

for i in range(2,10):
    if(dan == 1 and i%2 == 0 ):
        continue
    elif(dan == 2 and i%2 == 1 ):
        continue
    print(" {}단 start.".format(i))
    for j in range(2, 10):
        print("{}*{}={}".format(i, j, i * j))


print("==========================End==========================")


#구구단 원치 않는 숫자 뺴기
print("==================Select unlike dan=====================")
dan = int(input("Which dan would you unlike to select?\n"))

for i in range(2,10):
    print(" {}단 start.".format(i))
    for j in range(2, 10):
        if(dan == j):
            continue
        print("{}*{}={}".format(i, j, i * j))

print("==========================End===========================")
