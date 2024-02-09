# 백준 1427, 소트인사이드 (문자열, 정렬)

import sys
input = sys.stdin.readline

N = input()
lst = []
for i in range(len(N)):
    lst.append(N[i])

lst.sort(reverse = True)

for num in lst:
    print(num, end="")


