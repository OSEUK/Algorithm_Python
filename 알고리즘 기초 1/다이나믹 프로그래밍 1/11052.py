# 백준 11052, 카드 구매하기

import sys
input = sys.stdin.readline


if __name__ == "__main__":
    N = int(input())
    costs = list(map(int, input().split()))
    dp = [0]*(N)

    # 1~n 개까지 최대값을 구할 것
    for i in range(N):
        maxx = 0
        # 절반 이상의 값은 중복비교가되므로 의미 X
        for j in range(0, (i+1)//2):
            temp = dp[j] + dp[i-j-1]
            if temp > maxx:
                maxx = temp
        dp[i] = max(maxx, costs[i])
    
    print(dp[-1])

   