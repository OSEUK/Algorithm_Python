# 백준 13913, 숨바꼭질 4 (GOLD IV)
# PyPy3로만 정답됨

from collections import deque

def bfs(n, k):
    queue = deque()
    queue.append((n, 0))
    visited = [False] * 100001
    visited[n] = True

    while queue:
        pos, time = queue.popleft()

        if pos == k:
            return time

        for next_pos in (pos - 1, pos + 1, pos * 2):
            if 0 <= next_pos <= 100000 and not visited[next_pos]:
                if next_pos not in parent:
                    parent[next_pos] = pos
                visited[next_pos] = True
                queue.append((next_pos, time + 1))

n, k = map(int, input().split())
parent = dict()
result = bfs(n, k)
ans = [k]

while n not in ans:
    ans.append(parent[ans[-1]])

ans.reverse()

print(result)
print(*ans)