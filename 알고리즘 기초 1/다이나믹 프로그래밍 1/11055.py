# 백준 11055, 가장 큰 증가하는 부분 수열

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

dp = arr[:]

for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + arr[i])

print(max(dp))