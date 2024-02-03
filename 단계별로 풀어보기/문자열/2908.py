str = input()
result = 0
for i in range(len(str)):
    if 'A' <= str[i] <= 'C':
        result += 3
    elif 'D' <= str[i] <= 'F':
        result += 4
    elif 'G' <= str[i] <= 'I':
        result += 5
    elif 'J' <= str[i] <= 'L':
        result += 6
    elif 'M' <= str[i] <= 'O':
        result += 7
    elif 'P' <= str[i] <= 'S':
        result += 8
    elif 'T' <= str[i] <= 'V':
        result += 9
    elif 'W' <= str[i] <= 'Z':
        result += 10

print(result)