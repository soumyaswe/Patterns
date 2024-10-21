n = 5
k = 1
d = 0
for i in range(1, n+1) :
    for j in range(1, i+1) :
        if(k < 10) :
            print(k, end="  ")
        else :
            print(k, end=" ")
        d += 1
        k += d
    print()