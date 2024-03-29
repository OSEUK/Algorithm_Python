# 백준 15650, N과 M(2) (SILVER III)

def dfs(start):
    if len(s) == M:
        print(' '.join(map(str, s)))
        return
    
    for i in range(start, N+1):
        if i not in s:
            s.append(i)
            dfs(i+1)
            s.pop()

N, M = list(map(int, input().split()))
s = []

dfs(1)
