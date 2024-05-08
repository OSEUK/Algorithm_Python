# 백준 1339, 단어 수학 (GOLD IV)
# fail
# 단어 길이 기준이 아닌, 각 문자를 10^n으로 매핑해 value 순서대로 큰숫자 매칭

n = int(input())
words = []
alpha_value = {}
for _ in range(n):
    words.append(list(input().rstrip()))

for word in words:
    for i in range(len(word)):
        if word[i] not in alpha_value:
            alpha_value[word[i]] = 10 ** (len(word) - 1 - i)
        
        else:
            alpha_value[word[i]] += 10 ** (len(word) - 1 - i)

alpha_value = sorted(alpha_value.items(), key=lambda x: x[1], reverse=True)

alpha_to_num = {}

num = 9
for alpha in alpha_value:
    alpha_to_num[alpha[0]] = num
    num -= 1

ans = 0
for word in words:
    num = ""
    for alpha in word:
        num += str(alpha_to_num[alpha])
    
    ans += int(num)

print(ans)