n = 5
k = 2*n - 1

for i in range(1, 2*n) :
    for j in range(1, 2*n) :
        if(i == j or j == k-i+1) :
            if(i > 5) :
                print(2*n-i, end="")
            else :
                print(i, end="")
        else :
            print(" ", end="")
    print()


