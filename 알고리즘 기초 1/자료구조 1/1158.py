# 백준 1158, 요세푸스 문제

from collections import deque
import sys

input = sys.stdin.readline

if __name__ == "__main__":

    N, K = map(int, input().split())

    q = deque(range(1, N+1))
    result = []
    
    while q:
        q.rotate(-K+1)
        result.append(q.popleft())
        
    print('<'+ ', '.join(map(str, result)) + '>')
