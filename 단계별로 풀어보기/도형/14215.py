lst = list(map(int, input().split()))

if max(lst) >= sum(lst) - max(lst):
    print(2*sum(lst) - 2*max(lst) - 1)
else:
    print(sum(lst))

