import sys
input = sys.stdin.readline

N, M = map(int, input().split())
weight = [0]*N

for i in range(N):
    weight[i] = int(input())

max_weight = 0
member_size = 0
curr_weight = 0

for i in range(N):
    curr_weight += weight[i]
    if i >= M:
        curr_weight -= weight[i-M]

    if curr_weight > max_weight:
        max_weight = curr_weight

print(max_weight)
    

