# 어떤 수 n이 소수가 아니라면 반드시 n의 약수 중 하나는 n의 제곱근 이하에 존재합니다. 

M = int(input())
N = int(input())

prime_lst  = []
prime_ok = True

for num in range(M, N+1):
    if num > 1:
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_lst.append(num)

if not prime_lst:
    print(-1)
else:
    print(sum(prime_lst))
    print(min(prime_lst))
        