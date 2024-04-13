# 백준 1260, DFS와 BFS (SILVER II)

import sys
from collections import deque
input = sys.stdin.readline

def dfs(v, arr: list):
    visited[v] = True
    arr.append(v)

    for node in graph[v]:
        if not visited[node]:
            dfs(node, arr)

def bfs(v, arr: list):
    q = deque()
    q.append(v)

    while ()
    
    
    
if __name__ == "__main__":
    N, M, V = map(int, input().split())
    graph = [[] for _ in range(N)]

    dArr = []
    bArr = []
    visited = [False] * N
    for i in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    