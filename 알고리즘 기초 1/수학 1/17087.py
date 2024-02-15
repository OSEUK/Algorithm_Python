# 백준 17807, 숨바꼭질 6

import sys
input = sys.stdin.readline

def gcd(a, b):
    while b != 0:
        a, b = b, a%b
    return a

if __name__ == "__main__":
    N, S = map(int, input().split())
    A = list(map(int, input().split()))
    result = []
    for i in A:
        if S > i:
            result.append(S-i)
        else:
            result.append(i-S)

    res = result[-1]

    for i in result:
        if i != result[-1]:
            res = gcd(res, i)
    
    print(res)
    

