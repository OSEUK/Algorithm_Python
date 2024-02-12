# 백준 1929, 소수 구하기

if __name__ == "__main__":
    M, N = map(int, input().split())

    result = []
    
    for i in range(M, N+1):
        is_prime = True
        for j in range(2, int(i**(1/2))+1):
            if (i%j) == 0:
                is_prime = False
                break
            else:
                continue
        
        if is_prime and i != 1:
            result.append(i)
    
    for r in result:
        print(r)