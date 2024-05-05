# 백준 11725, 트리의 부모 찾기 (SILVER II)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def dfs(root):
    global visited, parents
    visited[root] = True
    
    for node in graph[root]:
        if not visited[node]:
            parents[node] = root
            dfs(node)


if __name__ == "__main__":
    N = int(input())

    graph = [[] for _ in range(N+1)]
    visited = [False] * (N+1)
    parents = [-1] * (N+1)
    for _ in range(N-1):
        a, b = map(int, input().split())

        graph[a].append(b)
        graph[b].append(a)

    dfs(1)

    for i in range(2, N+1):
        print(parents[i])
    
