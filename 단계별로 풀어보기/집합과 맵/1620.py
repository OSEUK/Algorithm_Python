# 백준 1620, 나는야 포켓몬 마스터 이다솜

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

nameToNum = {}
numToName = {}

for i in range(N):
    name = input().rstrip()  # 줄 바꿈 문자 제거
    nameToNum[name] = i + 1
    numToName[i + 1] = name

for _ in range(M):
    finding = input().rstrip()  # 줄 바꿈 문자 제거
    if finding.isdigit():
        print(numToName[int(finding)])
    else:
        print(nameToNum[finding])
