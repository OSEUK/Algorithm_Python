# 백준 7576, 토마토 (GOLD V)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)
from collections import deque

# 현재 좌표의 토마토가 익어있는지 검사
def is_one(x, y):
    if tomatoes[x][y] == 1:
        return True
    else:
        return False

# 토마토 박스에 모든 토마토가 익거나 들어있지 않은지 검사
def check_all_one():
    for i in range(N):
        for j in range(M):
            if tomatoes[i][j] == 0:
                return False
    return True

def bfs():
    q = deque()

    # 익어있는 토마토를 q에 삽입
    for i in range(N):
        for j in range(M):
            if is_one(i, j):
                # x, y, 해당 토마토가 익은 날짜
                q.append((i, j, 0))

    max_cnt = 0

    if check_all_one():
        return 0
    else:
        while q:
            pos = q.popleft()

            if pos[2] > max_cnt:
                max_cnt = pos[2]

            for i in range(4):
                nx = pos[0] + dx[i]
                ny = pos[1] + dy[i]

                if nx >= 0 and nx < N and ny >= 0 and ny < M and tomatoes[nx][ny] == 0:
                    tomatoes[nx][ny] = 1
                    q.append((nx, ny, pos[2] + 1))
        
        if not check_all_one():
            return -1
        else:
            return max_cnt            

if __name__ == "__main__":
    M, N = map(int, input().split())

    tomatoes = [list(map(int, input().split())) for _ in range(N)]
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    print(bfs())
