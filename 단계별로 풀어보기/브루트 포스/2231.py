N = int(input())

finded = False

for i in range(1, N+1):
    divide_sum = i + sum(map(int, str(i)))
        
    if divide_sum == N:
        print(i)
        finded = True
        break

if not finded:
    print(0)