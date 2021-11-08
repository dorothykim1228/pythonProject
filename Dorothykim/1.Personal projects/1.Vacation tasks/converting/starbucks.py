print("==========스타벅스에 오신걸 환영합니다============\n\n\n")

money = int(input("================돈을 넣어주세요==================\n\n"))

print(" 넣은 금액  {} \n 충전금액 {} WON\n".format(money,money))
print("=========어떤음료를 선택하시겠습니까? ===============\n\n")

print("===================[menu]===================\n")
print(" 1. 아메리카노 2000원 \n")
print(" 2. 카페라떼 2500원\n")
print(" 3. 카라멜 마끼아또 2700원\n")
print(" 4. 카페모카 2700원 \n")
print(" 5. 헤이즐넛 2600원\n")
print("=============================================\n")
menu = int(input("음료를 선택해주세요"))

order = 0
munu = 0
price = 0
while(1):
    if order == 0:
        menu = int(menu)
        if menu == 1:
            select = input("아메리카노를 선택하셨습니다.\n(1) HOT 아메리카노 (2)ICE 아메리카노 \n아이스는 300원 추가됩니다.")
            select = int(select)
            if select == 1:
                print("HOT 아메리카노를 선택하셨습니다")
                price += 2000
            elif select == 2:
                print("ICE 아메리카노를 선택하셨습니다")
                price += 2300
            else:
                break


        elif menu == 2:
            select = input("카페라떼를 선택하셨습니다.\n(1) HOT 카페라떼 (2)ICE 카페라떼 \n아이스는 300원 추가됩니다.")
            select = int(select)
            if select == 1:
                print("HOT 카페라떼를 선택하셨습니다")
                price += 2500
            elif select == 2:
                print("ICE 카페라떼를 선택하셨습니다")
                price += 2800


        elif menu == 3:
            select = input("헤이즐넛를 선택하셨습니다.\n(1) HOT 카페라떼 (2)ICE 카페라떼 \n아이스는 300원 추가됩니다.")
            select = int(select)
            if select == 1:
                print("HOT 헤이즐넛를 선택하셨습니다")
                price += 2600
            elif select == 2:
                print("ICE 헤이즐넛를 선택하셨습니다")
                price += 2900
        elif menu == 4:
            select = input("모카를 선택하셨습니다.\n(1) HOT 모카 (2)ICE 모카 \n아이스는 300원 추가됩니다.")
            select = int(select)
            if select == 1:
                print("HOT 모카를 선택하셨습니다")
                price += 2700
            elif select == 2:
                print("ICE 모카를 선택하셨습니다")
                price += 3000
        elif menu == 5:
            select = input("카라멜 마끼아또를 선택하셨습니다.\n(1) HOT 카라멜마끼아또 (2)ICE 카라멜마끼아또 \n아이스는 300원 추가됩니다.")
            select = int(select)
            if select == 1:
                print("HOT 카라멜 마끼아또를 선택하셨습니다")
                price += 2700
            elif select == 2:
                print("ICE 카라멜 마끼아또를 선택하셨습니다")
                price += 3000

            else:
                break

if money < price:
    print("요금이 부족합니다. %d원을 반환합니다" % money)
else:
    print("총 가격은 {}원 입니다. 잔돈은 {}입니다.".format(price, money - price))