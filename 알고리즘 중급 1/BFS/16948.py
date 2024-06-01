# 백준 16948, 데스 나이트 (SILVER I)

from collections import deque

def bfs(r1 : int, c1 : int, r2 : int, c2 : int):
    global N
    visited = [[False] * N for _ in range(N)]

    q = deque()
    count = 0
    q.append((r1, c1, count))
    visited[r1][c1] = True
    
    next_pos = [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]
    
    while q:
        x, y, cnt = q.popleft()

        if x == r2 and y == c2:
            return cnt
        
        for pos in next_pos:
            nx = x + pos[0]
            ny = y + pos[1]

            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue

            if not visited[nx][ny]:
                q.append((nx, ny, cnt + 1))
                visited[nx][ny] = True
    
    return -1

if __name__ == "__main__":
    N = int(input())

    r1, c1, r2, c2 = map(int, input().split())

    print(bfs(r1, c1, r2, c2))
    
