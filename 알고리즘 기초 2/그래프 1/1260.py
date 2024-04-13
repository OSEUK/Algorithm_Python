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
    queue = deque([v])
    visited[v] = True
    
    while queue:
        v = queue.popleft()
        arr.append(v)

        for node in graph[v]:
            if not visited[node]:
                queue.append(node)
                visited[node] = True
                
    
    
    
if __name__ == "__main__":
    N, M, V = map(int, input().split())
    graph = [[] for _ in range(N+1)]

    dArr = []
    bArr = []
    visited = [False] * (N+1)
    for i in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    for i in graph:
        i.sort()

    dfs(V, dArr)
    visited = [False] * (N + 1)
    bfs(V, bArr)

    print(*dArr)
    print(*bArr)
    

    
    
    