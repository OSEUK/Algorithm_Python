N, M = map(int,input().split())
cards = list(map(int, input().split()))

min_result = 100000
result = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            
            result = cards[i] + cards[j] + cards[k]
            
            if M-result >= 0:
                if M - result < min_result:
                    min_result = M - result
                    ans = result

print(ans)
