# 백준 1759, 암호 만들기 (GOLD V)

def dfs(start):
    global result
    
    # 최소 1개의 모음, 최소 2개의 자음 체크
    if len(result) == L:
        cnt = 0
        if 'a' in result:
            cnt += 1
        if 'e' in result:
            cnt += 1
        if 'i' in result:
            cnt += 1
        if 'o' in result:
            cnt += 1
        if 'u' in result:
            cnt += 1
        if L - cnt >= 2 and cnt >= 1:
            print(''.join(map(str, result)))
            return
    
    # 백트래킹
    for i in range(start, C):
        if arr[i] not in result:
            result.append(arr[i])
            dfs(i + 1)
            result.pop()


L, C = map(int, input().split())
arr = sorted(list(map(str, input().split())))
result = []
dfs(0)
