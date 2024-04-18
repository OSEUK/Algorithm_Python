# 백준 4963, 섬의 개수 (SILVER II)
import sys
sys.setrecursionlimit(10 ** 5)

def dfs(n_x, n_y):
    
    visited[n_x][n_y] = True

    for x in dx:
        for y in dy:
            nx = nx + x
            ny = ny + y

            if nx >= 0 and nx < h and ny >= 0 and ny < w:
                if not visited[nx][ny] and islands[nx][ny] == 1:
                    dfs(nx, ny)

if __name__ == "__main__":

    dx = [-1, 0, 1]
    dy = [-1, 0, 1]
    
    while True:
        w, h = map(int, input().split())
        
        if w == 0 and h == 0:
            break
        
        islands = [list(map(int, input().split())) for _ in range(h)]
        visited = [[False] * w for _ in range(h)]
        cnt = 0

        for i in range(h):
            for j in range(w):
                if not visited[i][j] and islands[i][j] == 1:
                    dfs(i, j)
                    cnt += 1
        
        print(cnt)

