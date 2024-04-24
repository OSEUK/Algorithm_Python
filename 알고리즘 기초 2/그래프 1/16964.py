# 백준 16964, DFS 스페셜 저지 ( GOLD III )

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

def dfs(x):
    if visited[x] == True:
        return
    visited[x] = True
    
    for node in tree[x]:
        if not visited[node]:
            children[x].add(node)
            parents[node].add(x)
            dfs(node)

if __name__ == "__main__":
    N = int(input())

    tree = [[] for _ in range(N+1)]
    visited = [False] * (N+1)
    children = [set() for _ in range(N+1)]
    parents = [set() for _ in range(N+1)]

    for _ in range(N-1):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)

    test_arr = list(map(int, input().split()))

    if test_arr[0] != 1:
        print(0)
        exit()
    
    dfs(1)

    


    