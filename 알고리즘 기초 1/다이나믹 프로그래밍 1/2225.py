# 백준 2225, 합분해

MOD = 1000000000
N, K = map(int, input().split())

arr = [[0]*201 for _ in range(201)]

for i in range(1, 201):
    arr[1][i] = i
    arr[i][1] = 1

if K == 1:
    print(1)
else:
    for n in range(2, N+1):
        for k in range(2, K+1):
            arr[n][k] = arr[n-1][k] + arr[n][k-1]

    print(arr[N][K] % MOD) 
    print(*arr)