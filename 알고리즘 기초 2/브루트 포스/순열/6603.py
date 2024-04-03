# 백준 6603, 로또 (SILVER II)

def dfs(start, cnt):
    if cnt == 6:
        print(*result)
        return
    prev = 0
    for i in range(start, k):
        if prev < S[i] and not visited[i]:
            visited[i] = True
            result.append(S[i])
            dfs(i + 1,cnt + 1)
            visited[i] = False
            result.pop()
            
    
while True:
    arr = list(map(int, input().split()))
    k = arr[0]
    if k == 0:
        break
    
    S = arr[1:]
    result = []
    visited = [False] * k
    
    dfs(0, 0)
    print()
    