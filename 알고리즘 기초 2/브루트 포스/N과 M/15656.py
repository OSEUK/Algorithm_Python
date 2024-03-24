# 백준 15656, N과 M (7) (SILVER III)

def dfs():
    if len(result) == M:
        print(' '.join(map(str, result)))
        return
    
    for i in arr:
        result.append(i)
        dfs()
        result.pop()

N, M = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()

result = []

dfs()