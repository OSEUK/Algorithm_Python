# 백준 1697, 숨바꼭질
# bfs, 한번에못품
from collections import deque

def bfs(n, k):
    queue = deque([(n, 0)])
    visited = [False] * 100001
    visited[n] = True

    while queue:
        pos, time = queue.popleft()

        if pos == k:
            return time
        
        for next_pos in (pos - 1, pos + 1, pos * 2):
            if 0 <= next_pos <= 100000 and not visited[next_pos]:
                visited[next_pos] = True
                queue.append((next_pos, time + 1))

n, k = map(int, input().split())

result = bfs(n, k)
print(result)