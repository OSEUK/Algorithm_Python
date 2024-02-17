# 백준 17103, 골드바흐 파티션
import sys
input = sys.stdin.readline

def Goldbach_Partition(n, primeNum : list):
    if n == 1 or n == 2:
        return 0
    cnt = 0
    for i in range(2, n//2 + 1):
        if primeNum[i] and primeNum[n-i]:
            cnt += 1

    return cnt

if __name__ == "__main__":
    primeNum = [False, False] + [True]*(1000000 - 1)

    for i in range(2, int(1000000 ** 0.5) + 1):
        if primeNum[i]:
            for j in range(i * i, 1000000, i):
                primeNum[j] = False
  
    T = int(input())
    result = []

    for i in range(T):
        N = int(input())

        result.append(Goldbach_Partition(N, primeNum))

    for res in result:
        print(res)
        
