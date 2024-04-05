# 백준 14501, 퇴사 (SILVER III)
# weighted intervel scheduling

def max_profit(N, schedule):
    dp = [0] * (N + 1)  # dp[i]: i일부터 마지막 날까지 얻을 수 있는 최대 수익

    for i in range(N - 1, -1, -1):  # 역순으로 DP 테이블을 채워나감
        if i + schedule[i][0] <= N:  # 상담이 기간 내에 끝날 경우
            dp[i] = max(schedule[i][1] + dp[i + schedule[i][0]], dp[i + 1])
        else:  # 상담 기간이 퇴사일을 넘어가는 경우
            dp[i] = dp[i + 1]

    return dp[0]

if __name__ == "__main__":
    N = int(input())  # 퇴사까지 남은 일수
    schedule = [list(map(int, input().split())) for _ in range(N)]  # 상담 일정과 보상

    print(max_profit(N, schedule))


