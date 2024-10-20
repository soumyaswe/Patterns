import string
ch = list(string.ascii_uppercase)
n = 5
for i in range(1, n+1) :
    for j in range(0, i) :
        print(ch[n-i], end=" ")
    print(end="\n")