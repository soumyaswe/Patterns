n = 5
matrix = [[0] * n for _ in range(n)]
num = 1
top, left = 0, 0
bottom, right = n - 1, n - 1

while (top <= bottom and left <= right) :
    for i in range(left, right + 1):
        matrix[top][i] = num
        num += 1
    top += 1
    for i in range(top, bottom + 1):
        matrix[i][right] = num
        num += 1
    right -= 1
    for i in range(right, left - 1, -1):
        matrix[bottom][i] = num
        num += 1
    bottom -= 1
    for i in range(bottom, top - 1, -1):
        matrix[i][left] = num
        num += 1
    left += 1

a = 0
for row in matrix:
    if(row[a] < 9) :
        print("   ".join(map(str, row)))
    else :
        print("  ".join(map(str, row)))
    a +=1 
