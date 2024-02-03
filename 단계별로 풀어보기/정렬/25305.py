# 백준 25305, 커트라인

N, K = map(int, input().split())
x = []
lst = list(map(int, input().split()))
for i in range(N):
    x.append(lst[i])

x.sort(reverse=True)

print(x[K-1])