# 백준 11724, 연결 요소의 개수 (SILVER II)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

def dfs(u):
    visited[u] = True
    
    for v in graph[u]:
        if not visited[v]:
            dfs(v)

if __name__ == "__main__":
    # 입력
    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    visited = [False] * (N+1)

    # 그래프 입력
    for i in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    # 연결 요소 
    connected_component = 0

    for i in range(1, N+1):
        if not visited[i]:
            dfs(i)
            connected_component += 1

    print(connected_component)
            

