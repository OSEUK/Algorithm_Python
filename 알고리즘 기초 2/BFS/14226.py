# 백준 14226, 이모티콘 (GOLD IV)
# 방문 여부를 2차원 배열로 설정하는게 중요했음

import sys
input = sys.stdin.readline
from collections import deque

    
def bfs(dest):
    time = 0
    clipboard = 0

    q = deque()
    q.append((1, clipboard, time))

    while q:
        num, clip, cnt = q.popleft()


        if num == dest:
            return cnt 
        
        # 클립보드에 복사
        if not visited[num][num]:
            visited[num][num] = True
            q.append((num, num, cnt + 1))
        
        # 클립보드 내용 붙여넣기
        if clip > 0 and num + clip < 2001 and not visited[num + clip][clip]:
            visited[num + clip][clip] = True
            q.append((num + clip, clip, cnt + 1))
        
        # 이모티콘 1개 삭제
        if num > 1 and not visited[num-1][clip]:
            visited[num-1][clip] = True
            q.append((num-1,clip, cnt+1))
        
 

if __name__ == "__main__":
    
    S = int(input())
    visited = [[False] * 2001 for _ in range(2001)]
    
    
    print(bfs(S))