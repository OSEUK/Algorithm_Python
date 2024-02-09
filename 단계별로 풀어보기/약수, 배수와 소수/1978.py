N = int(input())

cnt = 0
lst = list(map(int, input().split()))
prime_count = 0
for i in lst:
    for j in range(1, i):
        if i % j == 0:
            cnt += 1
        if cnt > 1:
            break
    if cnt == 1:
        prime_count += 1
    cnt = 0

print(prime_count)
