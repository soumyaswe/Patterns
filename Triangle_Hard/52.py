n = 5

for i in range(1, n+1) :
    for j in range(1, i+1) :
        if(i > (n/2)+1) :
            print(n-i+1, end="")
        else :
            print(i, end="")
    print()