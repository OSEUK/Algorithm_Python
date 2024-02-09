# 백준 2164, 카드 2

from collections import deque

q = deque()

N = int(input())

for i in range(1, N+1):
    q.append(i)

while len(q) > 1:
    q.popleft()

    toBottom = q.popleft()
    q.append(toBottom)


print(q.pop())
