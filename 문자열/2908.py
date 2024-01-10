lst = input().split()
a = lst[0]
b = lst[1]
reversed_a = int(a[::-1])
reversed_b = int(b[::-1])
print(max(reversed_a, reversed_b))