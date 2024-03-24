# 백준 15656, N과 M (9) (SILVER III)

def dfs():
    if len(result) == M:
        print(*result)
        return
    rem = 0

    for i in range(N):
        if not visited[i] and rem != arr[i]:
            visited[i] = True
            result.append(arr[i])
            rem = arr[i]
            dfs()
            visited[i] = False
            result.pop()

N, M = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()

visited = [False] * N
result = []

dfs()