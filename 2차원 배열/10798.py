arr = []
maxLen = 0
for i in range(5):
    str = input()
    arr.append(str)
    if len(str) >= maxLen:
        maxLen = len(str)

result = ""

for i in range(maxLen):
    for j in range(5):
        if i < len(arr[j]):
            result += arr[j][i]

print(result)     
    