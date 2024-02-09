# 백준 1764, 듣보잡

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

noListens = set()
result = []
for _ in range(N):
    noListens.add(input())

for _ in range(M):
    name = input()
    if name in noListens:
        result.append(name)

result.sort()
print(len(result))
for name in result:
    print(name, end="")
