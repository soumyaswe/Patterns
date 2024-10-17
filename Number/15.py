n = 5
for i in range(1,n+1) :
    k = i
    for j in range(1,n+1) :
        if(k > n) :
            print(n, end=" ")
        else :
            print(k, end=" ")
            k += 1      
    print(end="\n")