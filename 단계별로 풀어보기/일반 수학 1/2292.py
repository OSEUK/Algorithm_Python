N = int(input())

start = 1
count = 0

while N > start:
    count += 1
    start += 6*count

# 마지막 방 더함
print(count + 1)