str = input()
count_croatia = 0
i = 0

while i < len(str):
    if i < len(str) - 1 and str[i:i+2] in ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']:
        count_croatia += 1
        i += 2
    elif i < len(str) - 2 and str[i:i+3] == 'dz=':
        count_croatia += 1
        i += 3
    else:
        count_croatia += 1
        i += 1

print(count_croatia)
