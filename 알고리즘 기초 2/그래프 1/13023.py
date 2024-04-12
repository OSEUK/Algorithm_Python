# 백준 13023, ABCDE (GOLD V)

def dfs(start, depth):
    global arrive

    visited[start] = True

    if depth == 5:
        arrive = True
        return
    
    for node in graph[start]:
        if not visited[node]:
            dfs(node, depth + 1)
    
    visited[start] = False

if __name__ == "__main__":

    N, M = map(int, input().split())

    graph = [[] for _ in range(N)]
    visited = [False] * N
    arrive = False

    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(N):
        dfs(i, 1)
        if arrive:
            break

    if arrive:
        print(1)
    else:
        print(0)
