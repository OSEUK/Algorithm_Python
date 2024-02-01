# 백준 9012, 괄호

# 스택 클래스
class stack:

    def __init__(self):
        self.stk = []

    def pop(self):
        if self.stk:
            return self.stk.pop(-1)
        else :
            return 0
    
    def push(self, item):
        self.stk.append(item)

    def clear(self):
        self.stk.clear()

# VPS인지 검사
def check_VPS(string):
    is_VPS = True
    stk = stack()
    for ch in string:
        if ch == '(':
            stk.push(ch)
        else:
            if stk.pop() == 0:
                return False
    if not stk.stk:
        return is_VPS
    else:
        return False

# 메인
T = int(input())

for _ in range(T):
    string = input()

    if check_VPS(string):
        print("YES")
    else:
        print("NO")



