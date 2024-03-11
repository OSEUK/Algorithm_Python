# 백준 2309, 일곱 난쟁이

import sys
input = sys.stdin.readline

keys = []

for i in range(9):
    keys.append(int(input()))

keys.sort()

result = sum(keys)
found = False
for i in range(9):
    for j in range(i+1, 9):
        if result - keys[i] - keys[j] == 100:
            rem_i, rem_j = i, j
            found = True
    if found == True:
        break

for i in range(9):
    if i == rem_i or i == rem_j:
        continue
    print(keys[i])