# 백준 15654, N과 M (5)  (SILVER III)

def dfs():
    if len(result) == M:
        print(' '.join(map(str, result)))
        return 
    
    for i in arr:
        if i not in result:
            result.append(i)
            dfs()
            result.pop()

N , M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
result = []

dfs()


