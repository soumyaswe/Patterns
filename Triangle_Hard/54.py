N = 12345
s = str(N)
for i in range(len(s), 0, -1) :
    for j in range(i) :
        print(s[j], end="")
    s = s[1:]
    print()