# 백준 16198, 에너지 모으기 (SILVER I)

N = int(input())
weight = list(map(int, input().split()))
max_weight = 0

def dfs(arr : list, curr_weight):
    global max_weight

    if len(arr) == 2:
        if max_weight < curr_weight:
            max_weight = curr_weight
        return 

    for i in range(1, len(arr) - 1):
        next_weight = curr_weight + (arr[i-1] * arr[i+1])
        n = arr[i]
        arr.pop(i)
        dfs(arr, next_weight)
        arr.insert(i, n)

dfs(weight, 0)

print(max_weight)