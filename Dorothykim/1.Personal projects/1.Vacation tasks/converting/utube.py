import random

contents=0

ch = input("Please enter a name for YouTube channel.")

print("===================[Contents]===================\n")
print(" 1. Music \n")
print(" 2. mukbang(Eating Show)\n")
print(" 3. game\n")
print(" 4. vlog \n")
print(" 5. beauty\n")
print("=============================================\n")
print("Select Contents\n")
menu = int(input("Select contents"))


add=0
sub=0

for i in range(1,20):
    for j in range(1,10):
        viewer = random.randint(50, 2500)
        add=add+viewer
        print("viewer : {}".format(viewer))

    rem = random.randint(1, 5)
    sub= sub+add/rem
    print("sub : {}".format(sub))
    print("today's viewer: {}".format(add))
    add = 0

if (sub>= 100000):
    print("get silver button")
else:
    print("Boom~~~~~~~!")

