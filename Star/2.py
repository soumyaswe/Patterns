n = 6
for i in range(1,7) :
    # beginning spaces
    for k in range (1,i+1) :
        print("", end = " ")
    
    # no. of stars = nth row
    for j in range(1, n+1) :
        print("*", end=" ")
    
    n -= 1
    print(end="\n")
    
    
