n = 5 

for i in range(1,n+1) :
    if i%2 == 0 : k = i
    for j in range(1,i+1) :
        if(i%2 == 0) :
            print(k, end="")
            k -= 1
        else :
            print(j, end="")
    print()
