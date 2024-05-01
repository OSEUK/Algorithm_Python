# 백준 13549, 숨바꼭질 3 (GOLD V)

from collections import deque

def bfs(n, k):
    global min_time

    q = deque([(n, 0)])
    visited = [False] * 200001
    visited[n] = True

    while q:
        pos, time = q.popleft()

        if pos == k:
            if min_time > time:
                min_time = time

        if 0 <= 2 * pos <= 200000 and not visited[2 * pos]:
            visited[2 * pos] = True
            q.append((2 * pos, time))                
        
        if 0 <= pos-1 <= 200000 and not visited[pos-1]:
            visited[pos-1] = True
            q.append((pos-1, time + 1))
        
        if 0 <= pos+1 <= 200000 and not visited[pos+1]:
            visited[pos+1] = True
            q.append((pos+1, time + 1))
        
        

n, k = map(int, input().split())
min_time = 1000000

bfs(n, k)

print(min_time)