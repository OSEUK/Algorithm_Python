# 백준 2750, 수 정렬하기

N = int(input())
lst = []

for i in range(N):
    lst.append(int(input()))

lst.sort()

for i in range(N):
    print(lst[i])
