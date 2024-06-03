# 수뭉이의 참치캔 빼기

import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())
arr = list()
cnt = 0

def check_arr(arrs, top):
    for arr in arrs:
        if arr[0] == top:
            arr.popleft()
            return True
    return False

for i in range(K):
    num = int(input())
    arr.append(deque(map(int, input().split())))

is_success = True
while(N > 0):
    if check_arr(arr, N):
        N = N-1
    else:
        is_success = False
        break

if is_success:
    print("SUCCESS")
else:
    print("FAIL")