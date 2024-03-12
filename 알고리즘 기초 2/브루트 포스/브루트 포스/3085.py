# 백준 3085, 사탕 게임

def lSwap(x, col):
    colors[x][col], colors[x+1][col] = colors[x+1][col], colors[x][col]
def rSwap(y, row):  
    colors[row][y], colors[row][y+1] = colors[row][y+1], colors[row][y]


def check_max():
    cnt = 0
    max_cnt = 1
    for i in range(n):
        for j in range(1, n):
            if colors[i][j] == colors[i][j-1]:
                cnt += 1
                if cnt > max_cnt:
                    max_cnt = cnt
            else:
                cnt = 1
        cnt = 0

    for i in range(n):
        for j in range(1, n):
            if colors[j][i] == colors[j][i-1]:
                cnt += 1
                if cnt > max_cnt:
                    max_cnt = cnt
            else:
                cnt = 1
    
    return max_cnt
    
n = int(input())

colors = []

for i in range(n):
    colors.append(list(input().strip()))

arr = colors
result = 0

for i in range(n-1):
    for j in range(n-1):
        lSwap(i, j)
        if check_max() > result:
            result = check_max()
        lSwap(i, j)

        rSwap(i, j)
        if check_max() > result:
            result = check_max()
        rSwap(i, j)

print(result)
