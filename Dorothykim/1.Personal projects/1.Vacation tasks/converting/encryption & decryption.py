dictionary={

"a":"0","b":"1","c":"2","d":"3","e":"4",
"f":"5","g":"6","h":"7","i":"8","j":"9",
"k":"A","m":"B","n":"C","o":"D",
"p":"F","q":"G","r":"H","s":"I","t":"J",
"u":"K","v":"L","w":"M","x":"N","y":"O",
"z":"P",
}

#Encrpytion(암호화)
key1 = input("Please enter encryption\n")
for i in range(len(key1)):
    if key1[i] in dictionary:
        print(dictionary[key1[i]],end='')
print()

#Decryption(복호화)
key2=input("Please enter decryption\n")
for a in range(len(key2)):
    for j,k in dictionary.items():
        if k == key2[a]:
            print(j,end='')
print()



