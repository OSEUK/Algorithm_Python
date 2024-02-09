# 백준 1436, 영화감독 숌
N = int(input())
count = 0

# N이 10000보다 작으므로 적당한 범위 설정
for i in range(10000000):
    if '666' in str(i):
        count += 1

    if count == N:
        result = i
        break

print(result)