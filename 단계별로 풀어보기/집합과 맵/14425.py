# 백준 14425, 문자열 집합

N, M = map(int, input().split())

Narr = []
for i in range(N):
    Narr.append(input())

count = 0
for i in range(M):
    if input() in Narr:
        count += 1

print(count)
