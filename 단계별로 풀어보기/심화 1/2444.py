N = int(input())

for i in range(N):
    for j in range(N-1-i, 0, -1):
        print(" ", end="")
    print((2*i+1)*'*')

for i in range(N-1, 0, -1):
    for j in range(N-i):
        print(" ", end="")
    print((2*i-1)*'*')