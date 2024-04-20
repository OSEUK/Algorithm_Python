# 백준 7562, 나이트의 이동 (SILVER I)

import sys
input = sys.stdin.readline
from collections import deque

def bfs(curr_x, curr_y, l): # 현재 좌표, 체스판 크기 lxl
    q = deque()
    q.append((curr_x , curr_y, 0)) # 현재 좌표, 이동한 횟수
    visited[curr_x][curr_y] = True

    while q:
        pos = q.popleft()

        for i in range(8):
            nx = pos[0] + dpos[i][0]
            ny = pos[1] + dpos[i][1]

            if nx >= 0 and nx < l and ny >= 0 and ny < l:
                if visited[nx][ny] == False:
                    if chessmap[nx][ny] == 1:
                        return pos[2] + 1
                    if chessmap[nx][ny] == 0:
                        visited[nx][ny] = True
                        q.append((nx, ny, pos[2] + 1))
                

if __name__ == "__main__":
    T = int(input())

    # 나이트의 이동 방법
    dpos = [(-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2)]

    for _ in range(T):
        l = int(input())
        
        chessmap = [[0] * l for _ in range(l)]
        visited = [[False]*l for _ in range(l)]

        # 시작 좌표, 목적지 좌표
        start_x, start_y = map(int, input().split())
        chessmap[start_x][start_y] = 1
        des_x, des_y = map(int, input().split())
        chessmap[des_x][des_y] = 1

        # 시작 좌표와 목적지 좌표가 같으면 0 출력
        if (start_x, start_y) == (des_x , des_y):
            print(0)
        else:
            print(bfs(start_x, start_y, l))
        