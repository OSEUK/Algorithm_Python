# 백준 2667, 단지번호붙이기 (SILVER I)

def dfs(now_X, now_Y):
    global cnt

    visited[now_X][now_Y] = True

    for i in range(4):
        nx = now_X + dx[i]
        ny = now_Y + dy[i]
        if nx >= 0 and nx < N and ny >= 0 and ny < N:
            if not visited[nx][ny] and graph[nx][ny] == '1':
                dfs(nx, ny)
                cnt += 1

if __name__ == "__main__":
    N = int(input())

    graph = [list(input()) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    cnt = 1

    result = []
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and graph[i][j] == '1':
                dfs(i, j)
                result.append(cnt)
                cnt = 1
    
    print(len(result))
    
    for num in sorted(result):
        print(num)



