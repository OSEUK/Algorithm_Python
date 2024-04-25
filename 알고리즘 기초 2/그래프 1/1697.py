# 백준 1697, 숨바꼭질 (SILVER I)

from collections import deque

def bfs(curr, end, cnt):
    q = deque()
    q.append((curr, cnt))
    visited[curr] = True

    while q:
        pos = q.popleft()
        now = pos[0]
        curr_cnt = pos[1]
        
        if now == end:
            return curr_cnt
        
        for next_pos in (now+1, now-1, now * 2):
            if 0<=next_pos <= 100000 and not visited[next_pos]:
                visited[next_pos] = True
                q.append((next_pos, curr_cnt+1))

        
        
if __name__ == "__main__":
    N, K = map(int, input().split())

    visited = [False]*100001

    print(bfs(N, K, 0))
