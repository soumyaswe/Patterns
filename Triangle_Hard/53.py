n = 12345

for i in range(len(str(n)), 0, -1) :
    for j in range(i) :
        print(j+1, end="")
    n /= 10
    print()