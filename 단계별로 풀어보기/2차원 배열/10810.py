# 백준 10810, 공 넣기

N, M = map(int, input().split())
arr = [0]*N
for _ in range(M):
    i, j, k = map(int, input().split())

    for num in range(i-1, j):
        arr[num] = k

print(*arr)

