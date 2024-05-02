# 백준 1261, 알고스팟 (GOLD IV)
# 0-1 bfs

import sys
input = sys.stdin.readline
from collections import deque

def bfs(x, y, broken_wall):
    global visited, min_broken_wall

    q = deque()
    
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    q.append((x, y, broken_wall))
    visited[x][y] = True

    while q:
        pos = q.popleft()

        if pos[0] == N-1 and pos[1] == M-1:
            if pos[2] < min_broken_wall:
                min_broken_wall = pos[2]

        for i in range(4):
            nx = pos[0] + dx[i]
            ny = pos[1] + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            
            if not visited[nx][ny]:
                if maze[nx][ny] == '0':
                    # 벽을 안부수는 경우를 appendleft로 큐 앞에 넣어주는 것이 핵심
                    q.appendleft((nx, ny, pos[2]))
                    visited[nx][ny] = True
                else:
                    q.append((nx, ny, pos[2] + 1))
                    visited[nx][ny] = True

        
if __name__ == "__main__":
    M, N = map(int, input().split())

    maze = [list(input()) for _ in range(N)]
    visited = [[False]*M for _ in range(N)]

    min_broken_wall = 10000

    bfs(0, 0, 0)

    print(min_broken_wall)