# 백준 10819, 차이를 최대로 (SILVER II)

def dfs():
    if len(result) == N:
        sum = 0
        for i in range(1, N):
            sum += abs(result[i-1] - result[i])
        sums.append(sum)
        return
    
    for i in range(N):
        if not visited[i]:
            visited[i]=True
            result.append(arr[i])
            dfs()
            visited[i]=False
            result.pop()


N = int(input())
arr = list(map(int, input().split()))
result = []
visited = [False]*N
sums = []

dfs()
print(max(sums))