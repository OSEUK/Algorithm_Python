# 백준 7785, 회사에 있는 사람

N = int(input())

dic = {}
for i in range(N):
    name, log = map(str, input().split())
    dic[name] = log

sorted_dic = sorted(dic.items(), key=lambda x: x[0], reverse=True)

for person, status in sorted_dic:
    if status == "enter":
        print(person)
    else:
        pass
        