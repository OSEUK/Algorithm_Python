# 백준 10872, 팩토리얼

N = int(input())

result = 1
for i in range(1, N+1):
    result *= i

print(result)