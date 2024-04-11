# 백준 14391, 종이 조각 (GOLD III)
# Fail

n, m = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(n)]

max_score = 0

# 가로로 나누는 경우의 수 탐색
for i in range(1 << (n * m)):
    total = 0
    for j in range(n):
        current = 0
        for k in range(m):
            idx = j * m + k
            if (i & (1 << idx)) == 0:  # 가로로 나뉘지 않은 경우
                current = current * 10 + board[j][k]
            else:  # 가로로 나뉜 경우
                total += current
                current = 0
        total += current
    # 남은 열들의 합 추가
    for k in range(m):
        current = 0
        for j in range(n):
            idx = j * m + k
            if (i & (1 << idx)) != 0:  # 세로로 나뉜 경우
                current = current * 10 + board[j][k]
            else:  # 세로로 나뉘지 않은 경우
                total += current
                current = 0
        total += current
    max_score = max(max_score, total)

print(max_score)

