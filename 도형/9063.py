N = int(input())
x_lst = []
y_lst = []
for i in range(N):
    x, y = map(int, input().split())

    x_lst.append(x)
    y_lst.append(y)

min_x = min(x_lst)
max_x = max(x_lst)
min_y = min(y_lst)
max_y = max(y_lst)

print((max_x-min_x) * (max_y-min_y))


