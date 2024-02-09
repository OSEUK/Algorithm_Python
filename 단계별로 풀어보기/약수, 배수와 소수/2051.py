N, K = map(int, input().split())

result = 0
count = 0
num = 1
while num <= N:
    if N % num == 0:
        count += 1
        result = num

        if count == K:
            break

    num += 1

if count == K:
    print(result)
else:
    print(0)