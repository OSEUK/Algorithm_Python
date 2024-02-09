x, y, w, h = map(int,input().split())

xmin = min(w-x, x)
ymin = min(h-y, y)

print(min(xmin, ymin))