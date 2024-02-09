# 백준 17299 , 오등큰수
# Ai가 수열 A에서 등장한 횟수를 F(Ai)라고 했을 때, Ai의 오등큰수는 오른쪽에 있으면서 수열 A에서 등장한 횟수가 F(Ai)보다 큰 수 중에서 가장 왼쪽에 있는 수를 의미한다. 

from collections import Counter
import sys
input = sys.stdin.readline

def NGF(lst: list, lstCount: list):
    result = [-1]*len(lst)
    stk = []

    for i in range(len(lst)):
        while stk and lstCount[lst[i]] > lstCount[lst[stk[-1]]]:
            result[stk.pop()] = lst[i]
        stk.append(i) 

    return result

if __name__ == "__main__":
    N = int(input())
    lst = list(map(int, input().split()))
    lstCount = [0]*1000001
    for i in lst:
        lstCount[i] += 1

    result = NGF(lst, lstCount)

    print(*result)