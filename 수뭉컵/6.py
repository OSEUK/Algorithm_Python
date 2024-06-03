# 미스터 추

from collections import deque

k = int(input())
numbers = list(map(int, input().split()))
size = sum(numbers)
visited = [False] * (size + 1)
visit = [False] * k
def dfs(num):

    for i in range(k):
        if not visit[i]:
            visit[i] = True
            x = num + numbers[i]
            y = num - numbers[i]

            if x >= 1 and x <= size and not visited[x]:
                visited[x] = True
                dfs(x)
                
            if y >= 1 and y <= size and not visited[y]:
                visited[y] = True
                dfs(y)
            
            visit[i] = False


dfs(0)


cnt = 0
for i in range(1, (sum(numbers) + 1)):
    if not visited[i]:
       cnt += 1
print(cnt) 



