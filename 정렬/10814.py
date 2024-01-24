# 백준 10814, 나이순 정렬

N = int(input())
lst = []

for i in range(N):
    mapping = list(input().split())
    age = int(mapping[0])
    name = mapping[1]
    lst.append((age, name))

lst.sort(key = lambda x: x[0])

for tup in lst:
    print(tup[0], tup[1])

