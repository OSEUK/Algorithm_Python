# 백준 1699, 제곱수의 합

import math

def min_squares(n):
    dp = [0] * (n+1)  # dp[i]는 i를 제곱수의 합으로 나타내는데 필요한 최소 제곱수의 개수를 저장
    for i in range(1, n+1):
        dp[i] = i  # 초기값으로 i는 최대값인 i개의 1의 제곱으로 이루어진 합으로 나타낼 수 있음
        for j in range(1, int(math.sqrt(i))+1):
            dp[i] = min(dp[i], dp[i - j*j] + 1)  # 현재의 최소값과 이전 값에 j의 제곱을 뺀 값의 최소값 + 1을 비교하여 갱신
    return dp[n]

n = int(input())
print(min_squares(n))
