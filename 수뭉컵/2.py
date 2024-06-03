N = int(input())

arr = [list(input()) for _ in range(N)]

for i in range(N-1, -1, -1):
    for j in range(N):
        print(arr[j][i], end="")
    print()