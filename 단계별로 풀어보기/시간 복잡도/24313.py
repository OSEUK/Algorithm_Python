a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

f = a1 * n0 + a0
g = c * n0

if f > g:
    print(0)
else : 
    result1 = g-f

    f = a1 * (n0 + 1) + a0
    g = c * (n0 + 1)

    result2 = g-f

    if result2 >= result1:
        print(1)
    else:
        print(0)