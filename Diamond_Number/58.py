n = 5

for i in range(1, n+2) :
    k = i-1
    for j in range(1,2*i) :
        if(j == 1 or j == 2*i-1) :
            print("*", end="")
        else :
            if(j < i) :
                print(j-1, end="")
            else :
                print(k, end="")
                k -= 1
    print()

for i in range(n, 0, -1) :
    k = i-1
    for j in range(1, 2*i) :
        if(j == 1 or j == 2*i-1) :
            print("*", end="")
        else :
            if(j < i) :
                print(j-1, end="")
            else :
                print(k, end="")
                k -= 1
    print()
