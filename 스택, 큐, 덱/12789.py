# 백준 12789, 도키도키 간식드리미

from collections import deque

def check_queue(arr):
    stack = []
    queue = deque(arr)

    target = 1
    while queue or stack:
        if stack and stack[-1] == target:
            target += 1
            stack.pop()
        elif queue:
            stack.append(queue.popleft())
        else:
            break

    if target == len(arr) + 1:
        return "Nice"
    else:
        return "Sad"
    

N = int(input())
line = list(map(int, input().split()))

print(check_queue(line))