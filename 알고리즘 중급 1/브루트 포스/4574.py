# 백준 4574, 스노미도쿠 (GOLD I)
import sys
input = sys.stdin.readline

def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    
    start_row, start_col = 3 * (row // 3), 3 * (col //3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    
    return True

def dfs(board, domino_used):
    empty = [(i, j) for i in range(9) for j in range(9) if board[i][j] == 0]
    if not empty:
        return True
    
    r, c = empty[0]

    for num in range(1, 10):
        if is_valid(board, r, c, num):
            board[r][c] = num
            for dr, dc in [(0, 1), (1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < 9 and 0 <= nc < 9 and board[nr][nc] == 0:
                    for nnum in range(1, 10):
                        if num != nnum and is_valid(board, nr, nc, nnum) and not domino_used[num-1][nnum-1] and not domino_used[nnum-1][num-1]:
                            board[nr][nc] = nnum
                            domino_used[num-1][nnum-1] = domino_used[nnum-1][num-1] = True
                            if dfs(board, domino_used):
                                return True
                            board[nr][nc] = 0
                            domino_used[num-1][nnum-1] = domino_used[nnum-1][num-1] = False
            board[r][c] = 0

    return False
while True:
    N = int(input())
    
    if N == 0:
        break

    board = [[0] * 9 for _ in range(9)]
    visited = [[False] * 9 for _ in range(9)]

    for _ in range(N):
        x1, pos1, x2, pos2 = input().split()
        x1, x2 = int(x1), int(x2)
        r1, c1 = ord(pos1[0]) - ord('A'), int(pos1[1]) - 1
        r2, c2 = ord(pos2[0]) - ord('A'), int(pos2[1]) - 1

        board[r1][c1] = x1
        board[r2][c2] = x2
        visited[x1-1][x2-1] = visited[x2-1][x1-1] = True
    
    poses = list(input().split())
    num = 1
    for pos in poses:
        r, c = ord(pos[0]) - ord('A'), int(pos[1]) - 1

        board[r][c] = num
        num += 1
    
    if dfs(board, visited):
        for row in board:
            print("".join(map(str, row)))
    



        