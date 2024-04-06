# 백준 14889, 스타트와 링크 (SILVER I)

import sys
input = sys.stdin.readline


def dfs():
    global minAns
    if len(teamS) == N//2:
        startSum = 0
        linkSum = 0
        
        for i in range(N):
            if i not in teamS:
                teamL.append(i)
        
        for i in range(N//2 - 1):
            for j in range(i+1, N//2):
                startSum += S[teamS[i]][teamS[j]] + S[teamS[j]][teamS[i]]
                linkSum += S[teamL[i]][teamL[j]] + S[teamL[j]][teamL[i]]
        
        diff = abs(linkSum - startSum)
        if minAns > diff:
            minAns = diff

        teamL.clear()
        return

    for i in range(N):
        if i in teamS: continue
        if len(teamS)>0 and teamS[len(teamS)-1] > i : continue

        teamS.append(i)
        dfs()
        teamS.pop()
        

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
teamL = []
teamS = []
minAns = float('Inf')


dfs()
print(minAns)
