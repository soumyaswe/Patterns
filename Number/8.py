n = 5
k = n
for i in range(1,n+1) :
    for j in range(1,n+1) :
        if(i == j or j == k) :
            print("1", end="")
        else :
            print("0", end="")
    k -= 1
    print(end="\n")