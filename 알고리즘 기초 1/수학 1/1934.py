# 백준 1934, 최소공배수

def GCD(x, y):
    a, b = max(x, y), min(x, y)

    if b == 0:
        return a
    else:
        return GCD(b, a%b)
    
def LCM(x, y):
    return (x*y) // GCD(x, y)

T = int(input())

for _ in range(T):
    x, y = map(int, input().split())

    result = LCM(x, y)

    print(result)
