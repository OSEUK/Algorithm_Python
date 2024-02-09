lst = []
for i in range(3):
    lst.append(int(input()))

if lst[0] == lst[1] == lst[2] == 60:
    print("Equilateral")
elif sum(lst) == 180 and (lst[0] == lst[1] or lst[0] == lst[2] or lst[1] == lst[2]):
    print("Isosceles")
elif sum(lst) == 180:
    print("Scalene")
else:
    print("Error")