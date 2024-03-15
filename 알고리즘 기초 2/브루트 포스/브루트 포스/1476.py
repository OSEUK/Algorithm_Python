# 백준 1476, 날짜 계산

E, S, M = map(int, input().split())
Ex, Sx, Mx = 1, 1, 1

result = 1

while True:
    if Ex == E and Sx == S and Mx == M:
        break
    else:
        if Ex < 15:
            Ex += 1
        else:
            Ex = 1
        if Sx < 28:
            Sx += 1
        else:
            Sx = 1
        if Mx < 19:
            Mx += 1
        else:
            Mx = 1
        result += 1

print(result)
        