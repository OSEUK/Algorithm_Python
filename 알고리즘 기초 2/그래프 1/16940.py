# 백준 16940, BFS 스페셜 저지

import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    q = deque()
    q.append(1)
    visited[1] = True

    while q:
        x = q.popleft()

        # 부모 x의 아이들 node
        for node in tree[x]:
            if not visited[node]:
                q.append(node)
                children[x].add(node) 
                visited[node] = True
    
if __name__ == "__main__":
    N = int(input())

    tree = [[] for _ in range(N+1)]
    visited = [False] * (N+1)
    children = [set() for _ in range(N+1)]

    for _ in range(N-1):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)
    
    test_arr = list(map(int, input().split()))
    bfs()

    if test_arr[0] != 1:
        print(0)
        exit()
    
    result = 1
    next_index = 1
    for i in test_arr:
        if next_index == N:
            break
        
        # i의 자식노드 수  
        c_length = len(children[i])
        
        # i의 자식 노드들이 test_arr과 현재 값 이후 같은 개수의 자식 노드들과 같은지
        c1 = set(test_arr[next_index : next_index + c_length])
        c2 = children[i]
        if c1 != c2:
            result = 0
        
        next_index += c_length
    
    print(result)


    
            


