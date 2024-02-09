# 백준 17413, 단어 뒤집기 2

import sys
input = sys.stdin.readline

if __name__ == "__main__":

    s = input()
    result = []
    stk = []
    reversed = True

    for char in s:
        if char == '<':
            for _ in range(len(stk)):
                result.append(stk.pop())
            reversed = False
            result.append(char)
        elif char == '>':
            reversed = True
            result.append(char)
        elif reversed == False:
            result.append(char)
        elif (char == ' ' or char == '\n') and reversed == True:
            for _ in range(len(stk)):
                result.append(stk.pop())
            result.append(' ')
        else :
            stk.append(char)
    
    for ch in result:
        print(ch, end = '')