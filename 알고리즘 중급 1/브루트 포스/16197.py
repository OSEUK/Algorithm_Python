# 백준 16197, 두 동전 (GOLD IV)

from collections import deque

N, M = map(int, input().split())

board = [input() for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

coins = [(i, j) for i in range(N) for j in range(M) if board[i][j] == 'o']
visited = set((coins[0][0], coins[0][1], coins[1][0], coins[1][1]))
q = deque([(coins[0][0], coins[0][1], coins[1][0], coins[1][1], 0)])

def in_bounds(x, y):
    return 0 <= x < N and 0 <= y < M

def bfs():
    while q:
        x1, y1, x2, y2, depth = q.popleft()

        if depth == 10:
            return -1
        for i in range(4):
            nx1, ny1 = x1 + dx[i], y1 + dy[i]
            nx2, ny2 = x2 + dx[i], y2 + dy[i]
            fall1 = not in_bounds(nx1, ny1)
            fall2 = not in_bounds(nx2, ny2)

            if fall1 and fall2:
                continue
            if fall1 or fall2:
                return depth + 1
            
            if board[nx1][ny1] == '#':
                nx1, ny1 = x1, y1
            if board[nx2][ny2] == '#':
                nx2, ny2 = x2, y2

            if (nx1, ny1, nx2, ny2) not in visited:
                visited.add((nx1, ny1, nx2, ny2))
                q.append((nx1, ny1, nx2, ny2, depth + 1))
        
    return -1

print(bfs())
                 
