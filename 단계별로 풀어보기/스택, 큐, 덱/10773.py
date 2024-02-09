# 백준 10773, 제로

import sys
input = sys.stdin.readline

class stack:

    def __init__(self):
        self.stk = []
    
    def push(self, money):
        self.stk.append(money)
    
    def pop(self):
        del self.stk[-1]
    
    def print_sum(self):
        return sum(self.stk)

book = stack()

K = int(input())

for i in range(K):
    num = int(input())

    if num == 0:
        book.pop()
    else:
        book.push(num)

print(book.print_sum())


