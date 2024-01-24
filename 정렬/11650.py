# 백준 11650, 좌표 정렬하기 
N = int(input())

lst = []

for i in range(N):
    x, y = map(int, input().split())

    lst.append((x, y))

lst.sort()

for tup in lst:
    print(tup[0], tup[1])