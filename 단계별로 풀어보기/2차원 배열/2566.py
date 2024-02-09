A = [[0]*9 for _ in range(9)]

for i in range(9):
    row = list(map(int, input().split()))
    A[i] = row

maxNum = 0

for i in range(9):
    for j in range(9):
        if A[i][j] >= maxNum:
            maxNum = A[i][j]
            maxRow = i+1
            maxCol = j+1

print(maxNum)
print('%d %d' %(maxRow,maxCol))        