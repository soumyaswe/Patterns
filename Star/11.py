n = 5
a = 1
b = 9
for i in range(1,n+1) :
    for j in range(1,2*n) :
        if(i == 1) :
            print("*", end="")
        else :
            if(j == a or j == b) : 
                print("*", end="")
            else :
                print(" ", end="")
    a += 1
    b -= 1
    print(end="\n")