# 백준 14002, 가장 긴 증가하는 부분 수열 4 ( LIS )

n = int(input())
arr = list(map(int, input().split()))

dp = [1] * n
# 이전에 해당하는 인덱스를 저장
prev = [-1] * n

for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
            prev[i] = j

max_length = max(dp)
max_index = dp.index(max_length)
result = []

while max_index != -1:
    result.append(arr[max_index])
    max_index = prev[max_index]

result.reverse()

print(max_length)
print(*result)
