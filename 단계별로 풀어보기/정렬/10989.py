# 백준 10989, 수 정렬하기 3 (카운팅 정렬)

import sys
input = sys.stdin.readline

N = int(input())
count = [0] * 10001
for i in range(N):
    count[int(input())] += 1

for i in range(1, 10001):
    for _ in range(count[i]):
        print(i)