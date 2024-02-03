# 백준 10815, 숫자 카드

import sys
input = sys.stdin.readline


N = int(input())
Narr = set(map(int,input().split()))

M = int(input())
Marr = list(map(int, input().split()))

for i in Marr:
    if i in Narr:
        print(1, end=" ")
    else:
        print(0, end=" ")