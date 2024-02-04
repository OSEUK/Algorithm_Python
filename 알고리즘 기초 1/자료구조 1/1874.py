# 백준 1874, 스택 수열

import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())

    stk = []
    cnt = 1
    result = []
    possible = True
    for _ in range(n):
        num = int(input())

        if stk and stk[-1] == num:
            stk.pop()
            result.append('-')
        else :
            while cnt <= num:
                stk.append(cnt)
                cnt += 1
                result.append('+')
            if stk.pop() == num:
                result.append('-')
            else:
                possible = False
            
    if possible == True:
        for r in result:
            print(r)
    else:
        print("NO")


