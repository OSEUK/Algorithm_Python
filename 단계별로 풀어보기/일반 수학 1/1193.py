X = int(input())

line = 1
while X > line:
    X -= line
    line += 1

if line % 2 == 0:
    numerator = line - X + 1
    denominator = X

else :
    numerator = X
    denominator = line - X + 1

print(f"{denominator}/{numerator}")