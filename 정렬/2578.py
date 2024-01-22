# 백준 2587, 대표값2
nums = []
for i in range(5):
    nums.append(int(input()))

nums.sort()

average = sum(nums) / 5
print('%.0f' %average)
print(nums[2])