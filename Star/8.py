r = 8
c = 2*r

for i in range(1,r+1) :
    for j in range(1,c+1) :
        if(j <= (c/2 - i) and j >= (c/2 + i-1)) :
            print("*", end="")
        else :
            print("_", end="")
    print(end="\n")
afs