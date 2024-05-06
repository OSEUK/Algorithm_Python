# 백준 1167, 트리의 지름 (GOLD II)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def dfs(curr_node, visited, curr_dist):
    global V, nodes_dist, max_dist, max_node

    visited[curr_node] = True
    
    for node, dist in nodes_dist[curr_node]:
        if not visited[node]:
            if curr_dist + dist > max_dist:
                max_node, max_dist = node , curr_dist + dist
            dfs(node, visited, curr_dist+dist)

if __name__ == "__main__":
    V = int(input())

    nodes_dist = [[] for _ in range(V + 1)]
    for _ in range(V):
        i, *temp = list(map(int, input().split()))[:-1]
        for j in range(len(temp) // 2):
            nodes_dist[i].append((temp[2*j], temp[2*j + 1]))
    
    max_dist = 0
    max_node = 1
    visited = [False] * (V + 1)
    dfs(1, visited, 0)

    # dfs를 통해 시작 노드부터 최대 거리만큼 이동하고, 
    # 다시 해당 노드부터 이동한다면 트리의 최대 지름이 된다
    visited = [False] * (V + 1)
    dfs(max_node, visited, 0)
    
    print(max_dist)