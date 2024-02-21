# 백준 15990, 1,2,3 더하기 5

import sys
input = sys.stdin.readline

MOD = 1000000009

if __name__ == "__main__":
    T = int(input())
    dp = [[0]*4 for _ in range(100001)]
    dp[1][1] = 1
    dp[2][2] = 1
    dp[3][1] = 1
    dp[3][2] = 1
    dp[3][3] = 1

    for i in range(4, 100001):
        dp[i][1] = (dp[i-1][2] + dp[i-1][3]) % MOD
        dp[i][2] = (dp[i-2][1] + dp[i-2][3]) % MOD
        dp[i][3] = (dp[i-3][1] + dp[i-3][2]) % MOD

    for _ in range(T):
        n = int(input())
        print(sum(dp[n]) % MOD)
