n = 5
for i in range(1,n+1) :
    k = i
    for j in range(n, 0, -1) :
        if(k > n) :
            print(j, end="")
        else :
            print(k, end="")
            k += 1        
    print(end="\n")