# 백준 15651, N과 M (3)

def dfs():
    if len(arr) == M:
        print(' '.join(map(str, arr)))
        return
    
    for i in range(1, N+1):
        arr.append(i)
        dfs()
        arr.pop()
    
N, M = map(int, input().split())
arr = []
dfs()