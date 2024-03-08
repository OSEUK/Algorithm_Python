# 백준 11054, 가장 긴 바이토닉 부분 수열

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
rev_arr = arr[::-1]

inc = [1]*n
dec = [1]*n

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            inc[i] = max(inc[i], inc[j]+1)
        if rev_arr[i] > rev_arr[j]:
            dec[i] = max(dec[i], dec[j]+1)

result = [0]*n
for i in range(n):
    result[i] = inc[i] + dec[n-i-1] -1

print(max(result))
