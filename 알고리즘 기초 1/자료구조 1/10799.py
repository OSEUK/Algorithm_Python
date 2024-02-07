# 백준 10799, 쇠막대기
# 못풀었다. 인덱스를 활용한 스택으로 레이저와 쇠막대기 구분

import sys
input = sys.stdin.readline

s = input().strip()
stk = []
result = 0

for i in range(len(s)):
    if s[i] == '(':
        stk.append(i)
    else:
        if stk[-1] == i-1:
            stk.pop()
            result += len(stk)
        else:
            stk.pop()
            result += 1

print(result)
