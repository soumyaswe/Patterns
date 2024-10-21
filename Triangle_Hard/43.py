n = 5

for i in range(1, n+1) :
    for j in range(1, 2*i) :
        if(j == 1 or j == 2*i-1) :
            print(1, end="")
        else :
            if(j <= i) :
                print(j, end="")
            else :
                print((2*i-1)-(j-1), end="")
    print()