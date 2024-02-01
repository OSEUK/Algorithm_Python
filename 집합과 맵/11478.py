# 백준 11478, 서로 다른 부분 문자열의 개수

def substring(s, l):
    subs = set()
    for i in range(len(s)-(l-1)):
        subs.add(s[i:i+l])
    return subs

S = input()
count_subs = 0
for i in range(len(S)):
    count_subs += len(substring(S, i+1))
print(count_subs)