n = 5
for i in range(1,6) :
    for j in range(1,6) :
        if(j < i) :
            print("", end=" ")
        else : 
            print("*", end=" ")
    print(end="\n")

for i in range(5, 0, -1) :
    for j in range(1,6) :
        if(j < i) :
            print("", end=" ")
        else : 
            print("*", end=" ")
    print(end="\n")
