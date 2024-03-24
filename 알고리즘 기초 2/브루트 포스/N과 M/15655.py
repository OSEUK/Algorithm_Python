# 백준 15655, N과 M (6)  (SILVER III)

def dfs(start):
    if len(result) == M:
        print(' '.join(map(str, result)))
        return
    
    for i in range(start, len(arr)):
        if arr[i] not in result:
            result.append(arr[i])
            dfs(i)
            result.pop()

N, M = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()

result = []

dfs(0)