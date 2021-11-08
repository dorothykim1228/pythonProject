list_dorothy = []
a = 1
b = 26

for i in range(5):
    list_aa = [i for i in reversed(range (a,b,5)) ]
    list_dorothy.append(list_aa)
    a+=1
    b+=1

print(list_dorothy)