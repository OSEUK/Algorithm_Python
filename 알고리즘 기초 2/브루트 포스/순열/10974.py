# 백준 10974, 모든 순열 (SILVER III)


def dfs():
    if len(result) == N:
        print(*result)
        return
    
    for i in range(1, N+1):
        if i not in result:
            result.append(i)
            dfs()
            result.pop()

N = int(input())
result = []

dfs()