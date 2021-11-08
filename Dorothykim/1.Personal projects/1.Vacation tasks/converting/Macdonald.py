print("==========Welcome to Mcdonalds============\n\n\n")
print("==========Put the money in, Please=========\n\n")
money = int(input("insert coin"))

print(" enter the money  {} \n Charging amount {} WON\n".format(money,money))
print("=========Aavailable time ===============\n\n")
print("enter the time in, Please \n\n")

time = int(input("input rocal time"))
min = int(input("input minute" ))
print("Now {} hour {}min\n".format(time,min))
time = time*60+min

if(360 <= time <= 630):
    print("===============Time Attack==============\n");
    print("===========[Breakfast Menu]=============\n");
    print(" 1) BLT Egg Muffin (5500 WON)\n");
    print(" 2) Chicken'n Cheese Muffin (5200 WON)\n");
    print(" 3) Bacon & Egg McMuffin (5000 WON)\n");
    print(" 4) Susage & Egg McMuffin (5000 WON)\n");
    print(" press number\n");


    BM = int(input("Select Breakfast menu"))
    num = 0
    price = 0
    BM = int(BM)

    if BM == 1 :
        print("BLT Egg Muffin\n")
        print("price : 5500")
        price = 5500
        print("Change {} WON.\n".format(money - price))
        money -= price
    elif BM == 2 :
        print("Chicken'n Cheese Muffin\n")
        print("price : 5200")
        price = 5200
        print("Change {} WON.\n".format(money - price))
    elif BM == 3 :
        print("Bacon & Egg McMuffin\n")
        print("price : 5000")
        price = 5000
        print("Change {} WON.\n".format(money - price))
    elif BM == 4 :
        print("Susage & Egg McMuffin\n")
        print("price : 5000")
        price = 5000
        print("Change {} WON.\n".format(money - price))
    else:
        print("No Select Menu")

else:
    print("===================[menu]===================\n")
    print(" 1. burgers && meals \n")
    print(" 2. snacks && sides\n")
    print(" 3. Beberages && deserts\n")
    print("=============================================\n")
    print("Select a Menu\n")
    menu = int(input("Select menu"))

