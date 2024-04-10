# 백준 1182, 부분수열의 합

import sys
input = sys.stdin.readline

def dfs(idx, sum):
    global cnt

    if idx >= N:
        return 
    
    sum += arr[idx]

    if sum == S:
        cnt += 1

    # arr[idx]를 선택한 경우
    dfs(idx + 1, sum)
    
    # arr[idx]를 선택 안 한 경우
    dfs(idx + 1, sum - arr[idx])
            
N, S = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0

dfs(0, 0)

print(cnt)

