# 백준 15988, 1, 2, 3 더하기 3

MOD = 1000000009

if __name__ == "__main__":
    T = int(input()) # 테스트 케이스의 수
    result = []
    dp = [0] * (1000000 + 1)
    dp[0], dp[1], dp[2] = 1, 1, 2
    
    for i in range(3, 1000000 + 1):
        dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % MOD

    for _ in range(T):
        n = int(input()) # 각 테스트 케이스의 입력값
        result.append(dp[n])

    for i in result:
        print(i)

        