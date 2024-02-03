T = int(input())
result = []

for i in range(T):
    lst = input().split()
    R = int(lst[0])
    S = list(lst[1])
    
    str = ""
    for j in range(len(S)):
        for k in range(R):
            str += S[j]

    result.append(str)

for i in result:
    print(i) 