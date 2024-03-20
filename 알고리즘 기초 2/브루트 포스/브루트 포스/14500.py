# 백준 14500, 테트로미노 (GOLD IV)
# fail

# 보드 범위 체크
def is_valid(x, y, n, m):
    return 0 <= x < n and 0 <= y < m

def dfs(x, y, count):
    global max_sum
    if count == 4:
        max_sum = max(max_sum, sum(cur_tetromino))
        return
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if is_valid(nx, ny, N, M) and not visited[nx][ny]:
            visited[nx][ny] = True # 방문 여부
            cur_tetromino.append(board[nx][ny])
            dfs(nx, ny, count+1) 
            visited[nx][ny] = False
            cur_tetromino.pop()

# 가운데 튀어나온 모양 예외처리
def exception_cases(x, y):
    global max_sum
    # 예외적인 모양에 대한 경우의 수 처리
    # 각 테트로미노 모양에 따라 특별한 패턴으로 합을 계산하여 최댓값 갱신
    if x >= 1 and y >= 1 and y < M - 1:
        max_sum = max(max_sum, board[x][y] + board[x - 1][y] + board[x][y - 1] + board[x][y + 1])
    if x >= 1 and x < N - 1 and y < M - 1:
        max_sum = max(max_sum, board[x][y] + board[x - 1][y] + board[x + 1][y] + board[x][y + 1])
    if x < N - 1 and y >= 1 and y < M - 1:
        max_sum = max(max_sum, board[x][y] + board[x + 1][y] + board[x][y - 1] + board[x][y + 1])
    if x >= 1 and x < N - 1 and y >= 1:
        max_sum = max(max_sum, board[x][y] + board[x - 1][y] + board[x + 1][y] + board[x][y - 1])


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
max_sum = 0
cur_tetromino = []  # 현재 테트로미노의 블록들을 저장할 리스트
dx = [1, -1, 0, 0]  # 상하좌우 이동을 위한 방향 배열
dy = [0, 0, 1, -1]

for i in range(N):
    for j in range(M):
        visited[i][j] = True
        cur_tetromino.append(board[i][j])
        dfs(i, j, 1)
        visited[i][j] = False
        cur_tetromino.pop()
        exception_cases(i, j)

print(max_sum)