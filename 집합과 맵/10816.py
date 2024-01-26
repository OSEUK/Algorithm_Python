# 백준 10816, 숫자 카드 2

import sys
input = sys.stdin.readline

from collections import defaultdict
N = int(input())

count_dic = defaultdict(int)

values = map(int, input().split())

for value in values:
    count_dic[value] += 1

M = int(input())

find_nums = map(int,input().split())

for find_num in find_nums:
    print(count_dic[find_num], end=" ")