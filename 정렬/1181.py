# 백준 1181, 단어 정렬

N = int(input())

lst = []

for i in range(N):
    a = input()
    if a not in lst:
        lst.append(a)

lst.sort(key = lambda x : (len(x), x))

for str in lst:
    print(str)