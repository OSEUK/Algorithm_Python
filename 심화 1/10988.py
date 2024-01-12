str = input()
result = True
for i in range(int(len(str)/2)):
    if str[i] == str[len(str)-1-i]:
        continue
    else:
        result = False
        break

if result == True:
    print(1)
else :
    print(0)
