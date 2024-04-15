# 백준 1707, 이분 그래프

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
        