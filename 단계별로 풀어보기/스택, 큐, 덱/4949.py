# 백준 4949, 균형잡힌 세상
def checkBal(s):
    stk = []
    balancedString = True
    
    for ch in s:
        if ch == '(' or ch == '[':
            stk.append(ch)
        elif ch == ')':
            if len(stk) > 0 and stk[-1] == '(':
                stk.pop()
            else:
                balancedString = False
                break
        elif ch == ']':
            if len(stk) > 0 and stk[-1] == '[':
                stk.pop()
            else:
                balancedString = False
                break
    
    if len(stk) != 0:
        balancedString = False

    return balancedString

while True:
    s = input()
    
    if s == '.':
        break
    
    balancedString = checkBal(s)
    
    if balancedString:
        print("yes")
    else:
        print("no")


    
