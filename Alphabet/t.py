import string
ch = list(string.ascii_uppercase)
n = 5
k = 0 
for i in range(n, 0, -1) :
    for j in range(1, n+1) :
        if(j < i) :
            print(" ", end=" ")
        else :
            print(ch[k], end=" ")
    k += 1
    print(end="\n")