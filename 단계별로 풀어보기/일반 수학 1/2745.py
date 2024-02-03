A = input().split()
N = A[0]
B = int(A[1])

result = 0

# 거꾸로 반복하여 더해줌
for i in range(len(N) - 1, -1, -1):
    if 'A' <= N[i] <= 'Z':
        result += int(N[i], B) * (B**(len(N) - 1 - i))
    elif N[i] == '0':
        continue
    else:
        result += int(N[i]) * (B**(len(N) - 1 - i))

print(result)
