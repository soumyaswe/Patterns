n = 5
size = 2*n-1
for i in range(size) :
    for j in range(size) :
        min_dist = min(i, j, size-1-i, size-1-j)
        print(n-min_dist, end=" ")
    print()