# 백준 15664, N과 M (10) (SILVER II)
# combination 모듈사용해서 풀어보기

from  itertools import combinations

n, m = map(int, input().split())
numbers = sorted(list(map(int, input().split())))

result = sorted(set(combinations(numbers, m)))

for sequence in result:
    print(*sequence)