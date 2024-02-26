# 백준 1912, 연속합

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = [-1001]*(n+1)

dp[0] = arr[0]

for i in range(1, n):
    dp[i] = max(arr[i], dp[i-1] + arr[i])

print(max(dp))
