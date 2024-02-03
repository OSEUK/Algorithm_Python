N = int(input())

prime_lst = []

for i in range(2, N+1):
    while N % i == 0:
        print(i)
        N //= i
