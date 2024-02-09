N = int(input())
filled_color = [[0]*100 for _ in range(100)]

for i in range(N):
    number = input().split()
    left = int(number[0])
    under = int(number[1])

    for j in range(10):
        for k in range(10):
            filled_color[left + j][under + k] = 1

result = 0
for i in range(100):
    for j in range(100):
        if filled_color[i][j] == 1:
            result += 1

print(result) 

