a, b, c, d, e, f = map(int, input().split())

# ax + by = c
# dx + ey = f
# (a-d)x + (b-e)y = c - f

for x in range(-999, 1000):
    for y in range(-999, 1000):
        if (a*x + b*y == c and d*x + e*y == f):
            print('%d %d' %(x, y))
            break