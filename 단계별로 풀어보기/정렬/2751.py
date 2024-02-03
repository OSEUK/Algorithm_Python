# 백준 2751, 수 정렬하기 2

# 입력을 단순 input()으로 받을 시 시간 초과.
import sys
input = sys.stdin.readline

N = int(input())
nums = []

for i in range(N):
    nums.append(int(input()))

nums.sort()

for i in range(len(nums)):
    print(nums[i])
