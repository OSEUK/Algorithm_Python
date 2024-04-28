# 백준 2146, 다리 만들기

import sys
input = sys.stdin.readline
from collections import deque

# 상하좌우로만 이동
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# 띄어져 있는 나라들을 숫자로 구분하는 함수 (bfs)
def set_current_country(x, y, num):
    q = deque()
    q.append((x, y))
    colors[x][y] = num

    while q:
        pos = q.popleft()
        
        for i in range(4):
            nx = pos[0] + dx[i]
            ny = pos[1] + dy[i]

            if nx < 0 or nx >= size or ny < 0 or ny >= size:
                continue
            if colors[nx][ny] == 0 and countries[nx][ny] == 1:
                q.append((nx, ny))
                colors[nx][ny] = num
            
# 가까운 다리를 갱신하는 함수 (bfs)
def find_short_bridge(color):
    global min_bridges
    visited = [[False] * size for _ in range(size)]

    q = deque()

    for i in range(size):
        for j in range(size):
            if colors[i][j] == color:
                q.append((i, j, 0))
                visited[i][j] = True

    while q:
        pos = q.popleft()

        for i in range(4):
            nx = pos[0] + dx[i]
            ny = pos[1] + dy[i]
            bridge_cnt = pos[2]

            if bridge_cnt >= min_bridges:
                return
            if nx < 0 or nx >= size or ny < 0 or ny >= size:
                continue

            if colors[nx][ny] != 0 and colors[nx][ny] != color:
                if bridge_cnt < min_bridges:
                    min_bridges = bridge_cnt
            elif visited[nx][ny] == 0:
                q.append((nx, ny, bridge_cnt + 1))
                visited[nx][ny] = True
            

if __name__ == "__main__":
    size = int(input())

    countries = [list(map(int, input().split())) for _ in range(size)]
    colors = [[0]* size for _ in range(size)]
    min_bridges = 10000 # 입력크기의 최대 크기인 100*100로 기본설정

    # 순서대로 번호를 매김
    color = 1
    for i in range(size):
        for j in range(size):
            if countries[i][j] == 1 and colors[i][j] == 0:
                set_current_country(i, j, color)
                color += 1

    # 각 나라는 한번씩만 방문
    visited_countries = []
    for i in range(size):
        for j in range(size):
            if colors[i][j] != 0 and colors[i][j] not in visited_countries:
                find_short_bridge(colors[i][j])
                visited_countries.append(colors[i][j])
    
    print(min_bridges)
                


