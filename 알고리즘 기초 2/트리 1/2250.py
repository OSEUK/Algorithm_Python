# 백준 2250, 트리의 높이와 너비 (GOLD II)

import sys
input = sys.stdin.readline

def inorder(node, level):
    global xpos, level_min_max
    if node == -1:
        return
    inorder(tree[node][0], level + 1)  # 왼쪽 자식 노드 방문
    if level not in level_min_max:
        level_min_max[level] = [xpos, xpos]
    else:
        level_min_max[level][0] = min(level_min_max[level][0], xpos)
        level_min_max[level][1] = max(level_min_max[level][1], xpos)
    xpos += 1
    inorder(tree[node][1], level + 1)  # 오른쪽 자식 노드 방문

if __name__ == "__main__":
    sys.setrecursionlimit(10**6)  # 재귀 깊이 제한 확장
    N = int(input().strip())
    tree = {}
    parent = {}
    for _ in range(N):
        node, left, right = map(int, input().strip().split())
        tree[node] = (left, right)
        parent[left] = node
        parent[right] = node

    # 루트 노드 찾기
    root = next(node for node in tree if node not in parent)

    xpos = 1
    level_min_max = {}  # 각 레벨의 최소 x 위치와 최대 x 위치 저장
    inorder(root, 1)  # 중위 순회로 각 노드 위치 결정

    # 가장 넓은 레벨과 너비 계산
    max_width = 0
    level_with_max_width = 0
    for level in sorted(level_min_max):
        width = level_min_max[level][1] - level_min_max[level][0] + 1
        if width > max_width:
            max_width = width
            level_with_max_width = level

    print(level_with_max_width, max_width)



    
    