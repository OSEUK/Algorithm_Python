# 백준 2193, 이친수

import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())

    dp = [[0]*2 for _ in range(91)]

    # [자릿수][끝나는 수]
    dp[1][1] = 1
    dp[2][0] = 1
    dp[3][0] = 1
    dp[3][1] = 1

    for i in range(4, 91):
        dp[i][0] = dp[i-1][0] + dp[i-1][1]
        dp[i][1] = dp[i-1][0]
    
    res = sum(dp[N])

    print(res)
