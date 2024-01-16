sizeOfMatrix = input().split()
N = int(sizeOfMatrix[0])
M = int(sizeOfMatrix[1])

A = [[0]*M for _ in range(N)]
for i in range(N):
    row = list(map(int, input().split()))
    A[i] = row

B = [[0]*M for _ in range(N)]
for i in range(N):
    row = list(map(int, input().split()))
    B[i] = row

C = [[0]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        C[i][j] = A[i][j] + B[i][j]
        print(C[i][j], end = " ")
    print()


