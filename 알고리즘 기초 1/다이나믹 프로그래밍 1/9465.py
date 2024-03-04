# 백준 9465.py, 스티커

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())

    arr = [[0]*n for _ in range(2)]
    arr[0] = list(map(int, input().split()))
    arr[1] = list(map(int, input().split()))

    # 0 = 첫 번째 줄에서 선택
    # 1 = 두 번째 줄에서 선택
    # 선택 안함
    dp = [[0]*3 for _ in range(n)]
    dp[0][0] = arr[0][0]
    dp[0][1] = arr[1][0]
    dp[0][2] = 0

    for i in range(1, n):
        dp[i][0] = max(dp[i-1][1], dp[i-1][2]) + arr[0][i]
        dp[i][1] = max(dp[i-1][0], dp[i-1][2]) + arr[1][i]
        dp[i][2] = max(dp[i-1][0], dp[i-1][1])
        
    print(max(dp[n-1]))