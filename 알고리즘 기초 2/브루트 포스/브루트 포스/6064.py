# 백준 6064, 카잉 달력 (SILVER I)
def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def lcm(a, b):
    return a*b // gcd(a,b)

def find_date(M, N, x, y):
    max_year = lcm(M, N)

    while x <= max_year and y <= max_year:
        if x == y:
            return x
        elif x < y:
            x += M
        else:
            y += N
    
    return -1

T = int(input())

for _ in range(T):
    M, N, x, y = map(int, input().split())

    print(find_date(M, N, x, y))

