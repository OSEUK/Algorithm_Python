# 백준 1967, 트리의 지름 (GOLD IV)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def dfs(parent_node, visited, tree, curr_weight):
    global max_node, max_weight

    visited[parent_node] = True
    
    # 시작 노드로부터 총 가중치가 가장 클때의 노드와 가중치 저장
    if curr_weight > max_weight:
        max_weight = curr_weight
        max_node = parent_node

    for node in tree[parent_node]:
        child_node, weight = node
        if not visited[child_node]:
            dfs(child_node, visited, tree, curr_weight + weight)

if __name__ == "__main__":
    n = int(input())
    tree = [[] for _ in range(n+1)]

    for _ in range(n-1):
        parent_node, child_node, weight = map(int, input().split())
        tree[parent_node].append((child_node, weight))
        tree[child_node].append((parent_node, weight))  # 무방향 그래프로 한번만 주어지기 때문

    max_weight = -1
    max_node = -1
    visited = [False] * (n+1)
    dfs(1, visited, tree, 0)

    # 저장된 최대 가중치 노드로부터 탐색 시작
    visited = [False] * (n+1)
    dfs(max_node, visited, tree, 0)

    print(max_weight)
    