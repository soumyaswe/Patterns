n = 5
for i in range(n, 0, -1) :
    k = n
    for j in range(n, 0, -1) :        
        if(i < j) :
            print(k, end="")
            k -= 1
        else :
            print(k, end="")
    print(end="\n")