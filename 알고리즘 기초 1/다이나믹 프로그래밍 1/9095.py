# 백준 9095, 1,2,3 더하기

dic = {1:1, 2:2, 3:4}
def sumOf123(n):
    if n in dic:
        return dic[n]
    
    dic[n] = sumOf123(n-1) + sumOf123(n-2) + sumOf123(n-3)
    return dic[n]

if __name__ == "__main__":
    T = int(input())
    result = []

    for i in range(T):
        n = int(input())
        
        result.append(sumOf123(n))

    for i in result:
        print(i)

        