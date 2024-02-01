# 백준 28279, 덱 2

from collections import deque
import sys

input = sys.stdin.readline
deq = deque()

for _ in range(int(input())):
    lst = list(map(int, input().split()))
    cmd = lst[0]
    
    if cmd == 1:
        deq.appendleft(lst[1])
    elif cmd == 2:
        deq.append(lst[1])
    elif cmd == 3:
        if deq:
            print(deq.popleft())
        else:
            print(-1)
    elif cmd == 4:
        if deq:
            print(deq.pop())
        else:
            print(-1)
    elif cmd == 5:
        print(len(deq))
    elif cmd == 6:
        if deq:
            print(0)
        else:
            print(1)
    elif cmd == 7:
        if deq:
            print(deq[0])
        else:
            print(-1)
    elif cmd == 8:
        if deq:
            print(deq[-1])
        else:
            print(-1)
    