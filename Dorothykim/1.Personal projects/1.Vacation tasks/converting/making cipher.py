dictionary = {

"A" : "0", "B" : "1", "C" : "2","D" : "3","E" : "4",
"F" : "5", "G" : "6","H" : "7","I" : "8", "J" : "9",
"K" : "a", "L" : "b", "M" : "c","N" : "d","O" : "e",
"P" : "f", "Q" : "g", "R" : "h","S" : "i","T" : "j",
"U" : "k", "V" : "l", "W" : "m","X" : "n","Y" : "o",
"Z" : "p",

}

#암호화
key1 = input("> 암호화 입력 :")
for i in range(len(key1)):
    if key1[i] in dictionary:
        print(dictionary[key1[i]],end='')

print()

#복호화
key_2 = input("> 복호화 입력 :")
for mm in range(len(key_2)):
    for jj,kk in dictionary.items():
        if kk == key_2[mm]:
            print(jj,end='')
print()









#print("items():", dictionary.items())
#print()


##   for key, element in dictionary.items():
##   print("dictionary[{}]={}".format(key,element))