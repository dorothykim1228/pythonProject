import random

Ryu = input("Make Ryu's nickname")
honny = input("Make Ryu's girl friend name")

fish= 2
turn = 0
mom = 1
sec= 0

while(fish<1000):
    for i in range(mom):
        born = random.randint(1, 5)
        babies = born*2
        fish = fish + babies
        turn = turn + 1
        sec = sec + 10
    if(turn>1):

        die = random.randint(1, 5)
        fish = fish-die*2
        print(" dead fish : {}".format(die))
    print("fish : {}".format(fish))
    mom = fish//2

    if(fish<0):
        break

print("total gold fish : {}, number of repetitions : {}".format(fish, turn))
print("total gold fish : {}, time of repetitions : {}".format(fish, sec))


