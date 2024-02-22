# 백준 10844, 쉬운 계단 수

import sys
input = sys.stdin.readline

MOD = 1000000000

if __name__ == "__main__":
    dp = [[0]*10 for _ in range(101)]
    dp[1] = [1] * 10
    dp[1][0] = 0

    for i in range(2,101):
         for j in range(10):
                if j == 0:
                    dp[i][j] = dp[i-1][1] % MOD
                elif j == 9:
                    dp[i][j] = dp[i-1][8] % MOD
                else:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1] % MOD
    
    n = int(input())
    count = sum(dp[n]) % MOD
    print(count)
