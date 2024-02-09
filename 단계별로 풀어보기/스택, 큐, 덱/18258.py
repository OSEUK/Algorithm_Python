# 백준 18258, 큐 2

from collections import deque
import sys
input = sys.stdin.readline

q = deque()
        
N = int(input())

for i in range(N):
    lst = input().split()
    cmd = lst[0]
    if cmd == "push":
        q.append(lst[1])
    elif cmd == "pop":
        if q:
            num = q.popleft()
            print(num)
        else :
            print(-1)
    elif cmd == "size":
        print(len(q))
    elif cmd == "empty":
        if not q:
            print(1)
        else:
            print(0)
    elif cmd == "front":
        if q:
            print(q[0])
        else:
            print(-1)
    elif cmd == "back":
        if q:
            print(q[-1])
        else :
            print(-1)