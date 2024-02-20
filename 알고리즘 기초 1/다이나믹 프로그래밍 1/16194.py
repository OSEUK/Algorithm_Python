# 백준 16194, 카드 구매하기 2

import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    costs = list(map(int, input().split()))
    dp = [0]*(N)

    for i in range(N):
        minn = 10001
        
        for j in range(0, (i+1)//2):
            temp = dp[j] + dp[i-j-1]
            if temp < minn:
                minn = temp

        dp[i] = min(minn, costs[i])

    print(dp[-1]) 
