# 백준 16929, Two Dots (GOLD IV)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

def dfs(start_x, start_y, curr_x, curr_y, cnt): # 시작 좌표, 현재 좌표, 방문한 점의 개수
    global ans

    # 사이클을 이미 찾았다면
    if ans: 
        return

    # 현재 탐색하고 있는 색 저장
    color = dots[start_x][start_y]
    visited[curr_x][curr_y] = True
    
    for i in range(4):
        nx = curr_x + dx[i]
        ny = curr_y + dy[i]

        if nx >= 0 and nx < N and ny >= 0 and ny < M:
            if dots[nx][ny] == color:
                # 처음 점으로 돌아왔다면 == 사이클을 만들었다면
                if visited[nx][ny] and cnt >= 4 and (nx, ny) == (start_x, start_y):
                    ans = True
                elif not visited[nx][ny]:
                    dfs(start_x, start_y, nx, ny, cnt + 1)

if __name__ == "__main__":
    N, M = map(int, input().split())

    dots = [list(input()) for _ in range(N)]
    visited = [[False]*M for _ in range(N)]

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    ans = False

    # 전체 탐색
    for i in range(N):
        for j in range(M):
            dfs(i, j, i, j, 1)
            if ans:
                break
            visited = [[False]*M for _ in range(N)]

    if ans:
        print("Yes")
    else:
        print("No")
