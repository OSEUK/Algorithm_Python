# 백준 28278, 스택 2

import sys
input = sys.stdin.readline

class stack:

    def __init__(self):
        self.stk = []
    
    def push(self, num):
        self.stk.append(num)

    def pop(self):
        if not self.stk:
            print(-1)
        else:
            print(self.stk[-1])
            del self.stk[-1]
    
    def print_length(self):
        print(len(self.stk))
    
    def is_empty(self):
        if not self.stk:
            print(1)
        else :
            print(0)
    
    def print_top(self):
        if not self.stk:
            print(-1)
        else:
            print(self.stk[-1])

stk = stack()

N = int(input())

for i in range(N):
    lst = list(map(int, input().split()))

    cmd = lst[0]

    if cmd == 1:
        stk.push(lst[1])
    elif cmd == 2:
        stk.pop()
    elif cmd == 3:
        stk.print_length()
    elif cmd == 4:
        stk.is_empty()
    else:
        stk.print_top()

