# K진법 책 페이지

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    
    length = len(str(N))

    counts = [0] * K

    for i in range(1, 10):
        counts[i] += int(K**(length-2)) * (length-1)
    counts[0] += K**(length-1) - 1

    for i in range(K**(length-1), N+1):
        num = i
        while (num):
            counts[num % K] += 1
            num = num // K
    
    print(*counts)