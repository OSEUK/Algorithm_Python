# 백준 1748, 수 이어 쓰기 1

N = int(input())

length = len(str(N))

result = length * (N - (10**(length-1)-1)) 
for i in range(length - 1, 0, -1):
     result += i * (9 * 10**(i-1))
    
print(result)