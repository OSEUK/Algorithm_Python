# 백준 2346, 풍선 터뜨리기

from collections import deque
import sys

input = sys.stdin.readline

def popBallon(deq : deque):
    result = []

    while deq:
        idx, poped = deq.popleft()
        result.append(idx+1)
        if poped > 0:
            deq.rotate(-poped+1)
        elif poped < 0:
            deq.rotate(-poped)

    return result

if __name__ == "__main__":
    N = int(input())
    deq = deque(enumerate(map(int, input().split())))
    result = popBallon(deq)

    print(*result)
    