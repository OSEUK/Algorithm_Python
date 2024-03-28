# 백준 15666, N과 M (12)

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
temp = []

def dfs(start):
    if len(temp) == M:
        print(*temp)
        return
    
    prev = 0
    
    for i in range(start, N):
        if prev != nums[i]:
            temp.append(nums[i])
            prev = nums[i]
            dfs(i)
            temp.pop()

dfs(0)