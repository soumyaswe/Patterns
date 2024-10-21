n = 5

for i in range(1, n+1) :
    k = 2
    for j in range(1, 2*i) :
        if(j == 1 or j == 2*i-1) :
            print(2, end="")
        else :
            if(j <= i) :
                k += 2
                print(k, end="")
            else :
                k -= 2
                print(k, end="")
    print()