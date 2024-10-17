n = 5
for i in range(1,n+1) :
    for j in range(1,n+1) :
        # left of 1, decreasing
        if(i-j+1 > 1) :
            print(i-j+1, end="")
        # right of 1, increasing
        else :
            print(j-i+1, end="")
    print(end="\n")