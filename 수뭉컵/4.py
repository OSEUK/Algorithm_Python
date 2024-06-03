import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))

M = int(input())
for _ in range(M):
    s, e = map(int, input().split())
    if numbers[s-1:e-1] == numbers[e-1:s-1:-1]:
        print("YES")
    else:
        print("NO")