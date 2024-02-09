# 백준 10828, 스택
import sys
input = sys.stdin.readline

class stack:
    
    def __init__(self) -> None:
        self.stk = []
    
    def push(self, X):
        self.stk.append(X)
    
    def pop(self):
        if self.is_empty() == 0:
            return self.stk.pop()
        else:
            return -1

    def size(self):
        return len(self.stk)
    
    def top(self):
        if self.is_empty() == 0:
            return self.stk[-1]
        else:
            return -1
    
    def is_empty(self):
        if self.stk:
            return 0
        else:
            return 1
    
if __name__ == "__main__":
    N = int(input())

    stk = stack()
    result = []

    for _ in range(N):
        lst = list(map(str, input().split()))
        cmd = lst[0]
        
        if cmd == "push":
            stk.push(int(lst[1]))
        elif cmd == "pop":
            result.append(stk.pop())
        elif cmd == "size":
            result.append(stk.size())
        elif cmd == "empty":
            result.append(stk.is_empty())
        elif cmd == "top":
            result.append(stk.top())
    
    for num in result:
        print(num)


