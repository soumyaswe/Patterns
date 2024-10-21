n = 5
k = 0
for i in range(0, n) :
    for j in range(2**i) :
        if(k < 9) : 
            k += 1
            print(k, end="")
        else : 
            k = 1
            print(k, end="")
    print()