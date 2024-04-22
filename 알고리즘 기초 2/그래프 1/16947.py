# 백준 16947, 서울 지하철 2호선

import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

def dfs(start_node, curr_node, cnt):
    global is_cycle
    visited[curr_node] = True

    if is_cycle:
        return 
    
    for node in graph[curr_node]:
        if visited[node] and start_node == node and cnt >= 3:
            is_cycle = True
            return
        elif not visited[node]:
            dfs(start_node, node, cnt + 1)  


def bfs():
    q = deque()
    for i in range(N):
        if cycle[i]:
            result[i] = 0
            q.append(i)

    while q:
        now = q.popleft()

        for i in graph[now]:
            if result[i] == -1:
                result[i] = result[now] + 1
                q.append(i)

if __name__ == "__main__":
    N = int(input())

    graph = [[] for _ in range(N)]
    for i in range(N):
        a, b = map(int, input().split())
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    
    visited = [False] * N
    cycle = [False] * (N)


    for i in range(N):
        visited = [False] * (N)
        is_cycle = False
        
        dfs(i, i, 1)
        if is_cycle:
            cycle[i] = True
    
    result = [-1] * (N)
    
    bfs()
    for i in range(N):
        print(result[i], end=' ')

    
    

