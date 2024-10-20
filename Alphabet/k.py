import string
ch_u = list(string.ascii_uppercase)
ch_l = list(string.ascii_lowercase)
n= 5
k = 0
for i in range(1,n+1) :
    for j in range(0, i) :
        if(i == 1 or i == n-1 or i == n) :
            if((j+1)%2 == 0) :
                print(ch_u[k], end=" ")
            else :
                print(ch_l[k], end=" ")
        else :
            if((j+1)%2 == 0) :
                print(ch_l[k], end=" ")
            else :
                print(ch_u[k], end=" ")
        k += 1
    print(end="\n")
