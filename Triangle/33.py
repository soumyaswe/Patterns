n = 5
for i in range(n, 0, -1) :
    for j in range(1,i+1) :
        print(i+j-1, end="")
    print(end="\n")
