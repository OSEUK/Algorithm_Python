# 백준 15665, N과 M (11)

N, M = map(int, input().split())
nlist = list(map(int, input().split()))

arr = [0]*M
ans = set()

def dfs(cnt):
    if cnt == M:
        ans.add(' '.join(map(str, arr)))
        return
    
    for i in range(N):
        arr[cnt] = nlist[i]
        dfs(cnt + 1)

dfs(0)

for s in sorted(ans, key=lambda x:list(map(int, x.split(' ')))):
    print(s)