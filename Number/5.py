n = 5
for i in range(1,n+1) :
    for j in range(1,n+1) :
        if(i == 3 and j == 3) :
            print("0", end="")
        else :
            print("1", end="")
    print(end="\n")