# 백준 1707, 이분 그래프 (GOLD IV)
# 그래프의 정점의 집합을 둘로 분할하여, 각 집합에 속한 정점끼리는 서로 인접하지 않도록 분할할 수 있을 때, 그러한 그래프를 특별히 이분 그래프 (Bipartite Graph) 라 부른다.
# 인접한 노드를 다른 색으로 칠하고, 색깔 두개로 나눠지는 경우가 있는 지 확인

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

def dfs(start, num):
    visited[start] = num

    for node in graph[start]:
        if visited[node] == 0:
            if num == 1:
                dfs(node, 2)
            else:
                dfs(node, 1)

def isBipartiteGraph():
    for i in range(1, V+1):
        for node in graph[i]:
            if visited[i] == visited[node]:
                return False
    return True

if __name__ == "__main__":
    K = int(input())
    
    for i in range(K):
        V, E = map(int, input().split())

        graph = [[] for _ in range(V+1)]
        visited = [0] * (V+1)
        
        for j in range(E):
            u, v = map(int, input().split())
            graph[u].append(v)
            graph[v].append(u)
        

        for n in range(1, V+1):
            if visited[n] == 0:
                dfs(n, 1)
        
        if isBipartiteGraph():
            print("YES")
        else:
            print("NO")
        