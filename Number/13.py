n = 5
k = 1
for i in range(1,n+1) :
    for j in range(1,n+1) :
        if(k < 10) :
            print(k, end="  ")
        else :
            print(k, end=" ")
        k += 1
    print(end="\n")