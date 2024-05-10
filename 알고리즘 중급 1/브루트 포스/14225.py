# 백준 14225, 부분수열의 합 (SILVER I)

N = int(input())

S = list(map(int, input().split()))
visited = [False] * N
used_sum = [False] * 10000000

def dfs(S, used_sum, sum):

    used_sum[sum] = True

    for i in range(N):
        if not visited[i]:
            next_sum = sum + S[i]
            if next_sum < len(used_sum) and not used_sum[sum + S[i]]:
                visited[i] = True
                dfs(S, used_sum, sum + S[i])        
                visited[i] = False

dfs(S, 0)

for i in range(1, 10000000):
    if not used_sum[i]:
        print(i)
        break 
