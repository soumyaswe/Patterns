n = 5

for i in range(n) :
    for j in range(i,n) :
        print(" ", end=" ")
    
    for j in range(i+1) :
        print(chr(65+j), end=" ")
    
    for k in range(i-1, -1, -1) :
        print(chr(65+k), end=" ")
    
    print()