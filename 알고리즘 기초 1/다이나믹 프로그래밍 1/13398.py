# 백준 13398, 연속합 2

import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))

# 0 = 제거된 수열
# 1 = 아직 제거 안한거
dp = [[-1001]*2 for _ in range(n)]
dp[0][0] = dp[0][1] = arr[0]

for i in range(1, n):
    dp[i][0] = max(dp[i-1][1], dp[i-1][0] + arr[i])
    dp[i][1] = max(dp[i-1][1] + arr[i], arr[i])

print(max(max(dp)))