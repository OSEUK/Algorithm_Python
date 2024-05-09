# 백준 14888, 연산자 끼워넣기 (SILVER I)

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
operations = list(map(int, input().split()))
max_num = -1000000000
min_num = 1000000000

def dfs(curr_idx, curr_reslut):
    global operations, max_num, min_num
    
    if curr_idx + 1 >= N:
        if curr_reslut > max_num:
            max_num = curr_reslut
        if curr_reslut < min_num:
            min_num = curr_reslut
        return
    current_result = 0
    for i in range(4):
        if operations[i] != 0:
            if i == 0:
                current_result = curr_reslut + arr[curr_idx + 1]
            elif i == 1:
                current_result = curr_reslut - arr[curr_idx + 1]
            elif i == 2:
                current_result = curr_reslut  * arr[curr_idx + 1]
            else:
                current_result = int(curr_reslut / arr[curr_idx + 1])

            operations[i] -= 1
            dfs(curr_idx + 1, current_result)
            operations[i] += 1

dfs(0, arr[0])
print(max_num)
print(min_num)