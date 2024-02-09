# 백준 2609, 최대공약수와 최소공배수

def GCD(x, y):
    a, b = max(x, y), min(x, y)

    if b == 0:
        return a
    else:
        return GCD(b, a%b)
    
def LCM(x, y):
    return (x*y) // GCD(x, y)

if __name__ == "__main__":
    x, y = map(int, input().split())

    print(GCD(x, y))
    print(LCM(x, y))

