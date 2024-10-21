print(1, end="\n")
for i in range(2,6) :
    for j in range(i+1, i+i) :
        print(j, end="")
    for k in range(2*i-2, i-1, -1) :
        print(k, end="")
    print()