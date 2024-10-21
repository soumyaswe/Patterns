n = 5
k = 1
for i in range(1, n+1) :
    if(i%2 == 1) :
        for j in range(i) :
            if(k < 10) : print(k, end="  ")
            else : print(k, end=" ")
            k += 1
    else :
        a = k + i- 1
        for j in range(i) :
            if(a < 10) : print(a, end="  ")
            else : print(a, end=" ")
            a -= 1
        k += i
    print()