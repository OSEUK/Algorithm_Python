# 백준 2133, 타일 채우기

import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * 31
dp[2] = 3
for i in range(4, 31, 2):
    dp[i] = dp[i-2]*dp[2]
    # 이거 이해 잘 안됨.
    for j in range(4, i, 2):
        dp[i] += dp[i-j] * 2
    dp[i] += 2

print(dp[n])