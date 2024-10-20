n = 5

for i in range(1, n*2, 2) :
    for j in range(1,i+1) :
        print(j, end="")
    print()

for i in range(2*(n-1)-1, 0, -2) :
    for j in range(1, i+1) :
        print(j, end="")
    print()
