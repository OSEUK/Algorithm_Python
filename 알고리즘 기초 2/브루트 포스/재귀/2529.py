# 백준 2529, 부등호 (SILVER I)

# 부등호 검사 로직
def check_arr():

    satisfied = True
        
    for i in range(k):
        if compare[i] == '>':
            if result[i] < result[i+1]:
                satisfied = False
                break
        else:
            if result[i] > result[i+1]:
                satisfied = False
                break

    return satisfied

# 백트래킹 
def dfs():

    if len(result) == k+1:
        satisfied = check_arr()
        if satisfied:
            nums.append(''.join(map(str, result)))
        return

    for i in range(10):
        if not visited[i]:
            visited[i] = True
            result.append(i)
            dfs()
            visited[i] = False
            result.pop() 

k = int(input())
compare = list(input().split())
result = []
visited = [False] * (10)

nums = []

dfs()

print(nums[-1])
print(nums[0])
