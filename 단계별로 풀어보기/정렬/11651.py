# 백준 11651, 좌표 정렬하기 2

N = int(input())
lst = []
for i in range(N):
    x, y = map(int, input().split())
    lst.append((y, x))

lst.sort()

for tup in lst:
    print(tup[1], tup[0])

    
    