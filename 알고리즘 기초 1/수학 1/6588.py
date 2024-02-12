# 백준 6588, 골드바흐의 추측
# 개어렵다 이거
import sys

def is_prime(n):
    is_Prime = True
    for j in range(2, int(n**(1/2)) +1):
        if (n % j) == 0:
            is_Prime = False
            break
        else:
            continue

    return is_Prime

def Goldbach_conj(n,prime_num : list):
    for i in range(3, n):
        if prime_num[i] and prime_num[n-i]:
            return i, n-i
    
    return 0, 0
 
if __name__ == "__main__":
    prime_num = [False, False] + [True] * (1000000 - 1)
    for i in range(2, int(1000000 ** 0.5) + 1):
        if prime_num[i]:
            for j in range(i * 2, 1000000, i):
                prime_num[j] = False
  
    while True:
        n = int(sys.stdin.readline())
        
        if n == 0:
            break
        
        p1, p2 = Goldbach_conj(n, prime_num)
        if p1 == 0:
            print("GoldBach's conjecture is wrong.")
        else:
            print(str(n) + " = " + str(p1) + " + " + str(p2))
            
    