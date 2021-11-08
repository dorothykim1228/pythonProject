import random
turn =0

while 1:
    pika = 500#피카츄 체력
    enemy = random.randint(100, 450)#적들의 체력
    num = random.randint(1, 5)#적들 랜덤

    if num == 1:
        while 1:
            pika_a = random.randint(1, 150)  # 피카츄 공력데미지
            enemy_a = random.randint(1, 150)  # 적들의 공격데미지2
            enemy = enemy - pika_a
            pika = pika - enemy_a
            print("피카츄가 신나게 얻어맞았다. 피카츄 체력은 {}이다.".format(pika))
            print("파이리도 신나게 얻어맞았다. 파이리 체력은 {}이다.".format(enemy))

            if pika<=0:
                print("피카츄 안녕 ~ 잘가~")
                break
            elif enemy<=0:
                print("파이리 안녕~ 잘가~")
                turn = turn + 1
                pika = 500
                break
    elif num == 2:
        while 1:
            pika_a = random.randint(1, 150)  # 피카츄 공력데미지
            enemy_a = random.randint(1, 150)  # 적들의 공격데미지2
            enemy = enemy - pika_a
            pika = pika - enemy_a
            print("피카츄가 신나게 얻어맞았다. 피카츄 체력은 {}이다.".format(pika))
            print("꼬부기도 신나게 얻어맞았다. 꼬부기 체력은 {}이다.".format(enemy))

            if pika <= 0:
                print("피카츄 안녕 ~ 잘가~")
                break
            elif enemy <= 0:
                print("꼬부기 안녕~ 잘가~")
                turn = turn + 1
                pika = 500
                break
    elif num == 3:
        while 1:
            pika_a = random.randint(1, 150)  # 피카츄 공력데미지
            enemy_a = random.randint(1, 150)  # 적들의 공격데미지2
            enemy = enemy - pika_a
            pika = pika - enemy_a
            print("피카츄가 신나게 얻어맞았다. 피카츄 체력은 {}이다.".format(pika))
            print("버터풀도 신나게 얻어맞았다. 버터풀 체력은 {}이다.".format(enemy))

            if pika <= 0:
                print("피카츄 안녕 ~ 잘가~")
                break
            elif enemy <= 0:
                print("버터풀 안녕~ 잘가~")
                turn = turn + 1
                pika = 500
                break

    elif num == 4:
        while 1:
            pika_a = random.randint(1, 150)  # 피카츄 공력데미지
            enemy_a = random.randint(1, 150)  # 적들의 공격데미지2
            enemy = enemy - pika_a
            pika = pika - enemy_a
            print("피카츄가 신나게 얻어맞았다. 피카츄 체력은 {}이다.".format(pika))
            print("야도란도 신나게 얻어맞았다. 야도란 체력은 {}이다.".format(enemy))

            if pika <= 0:
                print("피카츄 안녕 ~ 잘가~")
                break
            elif enemy <= 0:
                print("야도란 안녕~ 잘가~")
                turn = turn + 1
                pika = 500
                break
    elif num == 5:
        while 1:
            pika_a = random.randint(1, 150)  # 피카츄 공력데미지
            enemy_a = random.randint(1, 150)  # 적들의 공격데미지2
            enemy = enemy - pika_a
            pika = pika - enemy_a
            print("피카츄가 신나게 얻어맞았다. 피카츄 체력은 {}이다.".format(pika))
            print("이브이도 신나게 얻어맞았다. 이브이 체력은 {}이다.".format(enemy))

            if pika <= 0:
                print("피카츄 안녕 ~ 잘가~")
                break
            elif enemy <= 0:
                print("이브이 안녕~ 잘가~")
                turn = turn + 1
                pika = 500
                break



    if pika <= 0:
        break
print("{}턴동안 싸우고 싶지 않았는데 싸우느라 힘들었다. ".format(turn))



