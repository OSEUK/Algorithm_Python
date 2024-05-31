# 백준 16928, 뱀과 사다리 게임 (GOLD V)

import sys
input = sys.stdin.readline
from collections import deque

def bfs(start_num : int, moves : dict): 
    q = deque()

    visited = [False] * 101
    q.append((start_num, 0))
    visited[start_num] = True
    
    while q:
        n, cnt = q.popleft()

        if n <= 0 or n > 100:
            continue
        
        if n == 100:
            return cnt

        for dice in range(1, 7):
            if n + dice <= 100:
                if n + dice in moves:
                    if not visited[moves[n + dice]]:
                        q.append((moves[n + dice], cnt + 1))
                        visited[moves[n + dice]] = True
                else:
                    if not visited[n + dice]:
                        q.append((n + dice , cnt + 1))
                        visited[n + dice] = True
        

if __name__ == "__main__":
    N, M = map(int, input().split())

    moves = {}

    for _ in range(N):
        x, y = map(int, input().split())

        moves[x] = y
    
    for _ in range(M):
        u, v = map(int, input().split())
        
        moves[u] = v

    print(bfs(1, moves))