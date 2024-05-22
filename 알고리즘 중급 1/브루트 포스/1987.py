# 백준 1987, 알파벳 (GOLD IV)

from collections import deque


def bfs(original, x, y):
    max_len = 1
    q = set([(x, y, original[y][x])])  # set로 변경
    while q:
        x, y, alpha = q.pop()  # pop으로 변경
        max_len = max(max_len, len(alpha))

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < c and 0 <= ny < r and original[ny][nx] not in alpha:
                q.add((nx, ny, alpha + original[ny][nx]))  # add로 변경

    return max_len


r, c = map(int, input().split())
original = []
for _ in range(r):
    original.append(list(input()))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

print(bfs(original, 0, 0))

""" 시간초과 코드
import sys
input = sys.stdin.readline

R, C = map(int, input().split())

board = [list(input()) for _ in range(R)]
visited = [[False] * C for _ in range(R) ]
alphabets = dict()

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
max_count = 0

def dfs(x : int, y : int, curr_count : int, board : list, alphabets : dict, visited : list):
    global dx, dy, max_count

    visited[x][y] = True

    if curr_count > max_count:
        max_count = curr_count

    if board[x][y] not in alphabets:
        alphabets[board[x][y]] = 1
    elif board[x][y] in alphabets:
        alphabets[board[x][y]] += 1
 
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            continue
        
        if visited[nx][ny]:
            continue

        if board[nx][ny] not in alphabets or alphabets[board[nx][ny]] == 0:
            dfs(nx, ny, curr_count + 1, board, alphabets, visited)
            visited[nx][ny] = False
            alphabets[board[nx][ny]] -= 1


dfs(0, 0, 1, board, alphabets, visited)

print(max_count)
"""