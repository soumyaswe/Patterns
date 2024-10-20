n = 5

for i in range(1, n+1) :
    for k in range(i,n) :
        print(" ", end=" ")
    
    for k in range(i, 0, -1) :
        print(chr(64+k), end=" ")
    
    for j in range(2, i+1) :
        print(chr(64+j), end=" ")
        
    print()