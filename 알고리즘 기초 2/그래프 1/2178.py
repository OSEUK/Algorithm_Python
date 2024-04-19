# 백준 2178, 미로 탐색 (SILVER I)

import sys
from collections import deque
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

def bfs():
    global result
    
    q = deque()
    # 현재 x좌표, y좌표, 지나고 있는 칸 수
    # 무조건 (0,0) 부터 시작하는 문제
    q.append((0, 0, 1))
    maze[0][0] = '0'

    # bfs 로직
    while q:
        pos = q.popleft()

        if pos[0] == N-1 and pos[1] == M-1:
            if pos[2] < result:
                result = pos[2]

        for i in range(4):
            nx = pos[0] + dx[i]
            ny = pos[1] + dy[i]

            if nx >= 0 and nx < N and ny >= 0 and ny < M and maze[nx][ny] == '1':
                # append할때 0으로 만들어놔야 q에 중복으로 들어가지 않음
                maze[nx][ny] = '0'
                q.append((nx, ny, pos[2] + 1))

if __name__ == "__main__":
    N, M = map(int, input().split())

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    maze = [list(input()) for _ in range(N)]
    result = 10000

    bfs()
    print(result)