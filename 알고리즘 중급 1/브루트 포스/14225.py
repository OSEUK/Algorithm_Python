# 백준 14225, 부분수열의 합 (SILVER I)

N = int(input())

S = list(map(int, input().split()))
visited = [False] * N
used_sum = [False] * 10000000

def dfs(index, current_sum):
    if index == N:
        if current_sum > 0:
            used_sum[current_sum] = True
        return
    
    dfs(index + 1, current_sum + S[index])
    dfs(index + 1, current_sum)

dfs(0,0)

for i in range(1, 10000000):
    if not used_sum[i]:
        print(i)
        break 
