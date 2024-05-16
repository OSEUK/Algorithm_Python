# 백준 9663, N-Queen (GOLD IV)

N = int(input())
board = [[0] * N for _ in range(N)]
visited = [[False] * N for _ in range(N)]

count_queens = 0

def dfs(board, row):
    global count_queens

    if row == N-1:
        count_queens += 1
        return 
    
    for i in range(N):
        if not visited[row][i]:
            visited[row] = [True] * N