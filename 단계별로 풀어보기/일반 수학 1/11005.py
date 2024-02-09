A = input().split()
N = int(A[0])
B = int(A[1])

result = ""
while N > 0:
    remainder = N % B
    if remainder < 10:
        result = str(remainder) + result
    else:
        result = chr(ord('A') + remainder - 10) + result
    N //= B

print(result)
