# 백준 9663, N-Queen (GOLD IV)

N = int(input())
board = [0] * N
count = 0

def is_safe(row, col):
    for i in range(row):
        if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
            return False
    return True

def backtrack(row):
    global count
    if row == N:
        count += 1
    for col in range(N):
        if is_safe(row, col):
            board[row] = col
            backtrack(row + 1)
            board[row] = 0
    
backtrack(0)

print(count)