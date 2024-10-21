n= 5

for i in range(n) :
    a = 4
    k = i+1
    for j in range(i+1) :
        print(k, end="  ")
        k += a
        a -= 1
    print(end="\n")
