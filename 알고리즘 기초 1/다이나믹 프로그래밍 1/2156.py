# 백준 2156, 포도주 시식

import sys
input = sys.stdin.readline

n = int(input())

arr = []
for _ in range(n):
    arr.append(int(input()))

dp = [0] * n

dp[0] = arr[0]
if n > 1:
    dp[1] = arr[0] + arr[1]

# i번째 포도주 안마실때, i-1 건너뛸 때, i-2 건너뛸때
for i in range(2, n):
    dp[i] = max(dp[i-1], dp[i-2] + arr[i], dp[i-3] + arr[i-1] + arr[i])

print(dp[n-1])