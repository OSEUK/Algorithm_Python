# 백준 1018, 체스판 다시 칠하기

N, M = map(int, input().split())

# 8X8 체스판의 첫번째 문자가 B인경우, W인 경우
firstBLine = ['BW'*4, 'WB'*4]
firstWLine = ['WB'*4, 'BW'*4]
bCount = 0
wCount = 0
lst = []
minCount = N*M

for i in range(N):
    lst.append(input())

# M*N 크기의 체스판 반복
for i in range(N-7):
    for j in range(M-7):

        # 해당 위치에서 8X8을 B type과 W type 각각 카운트
        for k in range(8):
            if k % 2 == 0:
                for r in range(8):
                    if lst[i+k][j+r] != firstBLine[k%2][r]:
                        bCount += 1
                    if lst[i+k][j+r] != firstWLine[k%2][r]:
                        wCount += 1
            else:
                for r in range(8):
                    if lst[i+k][j+r] != firstBLine[k%2][r]:
                        bCount += 1
                    if lst[i+k][j+r] != firstWLine[k%2][r]:
                        wCount += 1
   
        minCount = min(minCount, bCount, wCount)
        
        bCount = 0
        wCount = 0

print(minCount)