
coin = int(input("insert coin"))
print("You insert coin : {}".format(coin))

if(coin<600):
    print("short of money, return coin : {}".format(coin))
else:
    price=0
    print("===================[menu]===================\n")
    print(" 1. Sprite \n")
    print(" 2. Coca cola\n")
    print(" 3. Pocari\n")
    print(" 4. Cabonated water\n")
    print("=============================================\n")
    print("Select a drink\n")
    drink = int(input("Press number"))

    if drink == 1 :
        print("sprite\n")
        print("price : 600")
        price = 600
        print("Change {} WON.\n".format(coin - price))
        coin -= price
    elif drink == 2 :
        print("coca cola\n")
        print("price : 5200")
        price = 5200
        print("Change {} WON.\n".format(coin - price))
    elif drink == 3 :
        print("Pocari Sweat\n")
        print("price : 900")
        coin = 900
        print("Change {} WON.\n".format(coin - price))
    elif drink == 4 :
        print("cabonated water\n")
        print("price : 1000")
        coin = 1000
        print("Change {} WON.\n".format(coin - price))
    else:
        print("No Select drink")

