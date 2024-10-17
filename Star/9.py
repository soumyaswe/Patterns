for i in range(6, 0, -1) :
    for j in range(1,7) :
        if(j < i) :
            print("", end=" ")
        else : 
            print("*", end=" ")
    print(end="\n")

n = 5
for i in range(1,6) :
    for k in range (1,i+1) :
        print("", end = " ")
    
    for j in range(1, n+1) :
        print("*", end=" ")
    
    n -= 1
    print(end="\n")
