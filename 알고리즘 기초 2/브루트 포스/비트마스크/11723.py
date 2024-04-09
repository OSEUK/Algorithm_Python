# 백준 11723, 집합 (SILVER V)

import sys
input = sys.stdin.readline

class sets:
    
    def __init__(self, S : list):
        self.S = S

    def add(self, x):
        if x not in self.S:
            self.S.append(x)

    def myremove(self, x):
        if x in self.S:
            self.S.remove(x)
    
    def check(self, x):
        if x in self.S:
            return 1
        else :
            return 0
    
    def toggle(self, x):
        if x in self.S:
            self.myremove(x)
        else:
            self.add(x)
    
    def all(self):
        self.S = [i for i in range(1, 21)]

    def empty(self):
        self.S.clear()

if __name__ == "__main__":
    M = int(input())
    result = sets([])

    for i in range(M):
        arr = list(input().split())
        cmd = arr[0]
        if cmd != "all" and cmd != "empty":
            x = arr[1]

        if cmd == "add":
            result.add(int(x))
        elif cmd == "remove":
            result.myremove(int(x))
        elif cmd == "check":
            print(result.check(int(x)))
        elif cmd == "toggle":
            result.toggle(int(x))
        elif cmd == "all":
            result.all()
        elif cmd == "empty":
            result.empty()


    