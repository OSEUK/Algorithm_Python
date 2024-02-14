# 백준 9613, GCD 합
# GCD = 최대공약수

import sys
input = sys.stdin.readline

def gcd(a, b):
    while b != 0:
        a, b = b, a%b
    return a

def gcd_sum(arr):
    n = len(arr)
    total = 0
    for i in range(n):
        for j in range(i+1, n):
            total += gcd(arr[i], arr[j])
    return total

if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        lst = list(map(int, input().split()))
        result = gcd_sum(lst[1:])
        print(result)



