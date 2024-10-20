import string
ch = list(string.ascii_uppercase)
n= 5

for i in range(n) :
    char = chr(ord('A') + i)
    a = 4
    for j in range(i+1) :
        print(char, end=" ")
        char = chr(ord(char) + a)
        a -= 1
    
    print(end="\n")
