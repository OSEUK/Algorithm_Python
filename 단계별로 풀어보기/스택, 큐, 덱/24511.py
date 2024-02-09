# 백준 24511, queuestack 

from collections import deque
import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())

    checkDS = list(map(int, input().split()))

    queuestack = list(map(int, input().split()))
    qs = deque()

    # 스택에서는 자기 자신만 POP되므로 큐만 남김 
    # O(N*M) -> O(N+M)
    for i in range(len(checkDS)):
        if checkDS[i] == 0:
            qs.append(queuestack[i])

    M = int(input())
    
    numbers = list(map(int, input().split()))
    result = []  

    if qs:
        for num in numbers:
            result.append(qs.pop())
            qs.appendleft(num)
    else:
        result = numbers

    print(*result)
