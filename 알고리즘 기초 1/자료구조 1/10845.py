# 백준 10845, 큐

import sys
input = sys.stdin.readline

class Queue:

    def __init__(self):
        self.q = []
    
    def push(self, x):
        self.q.append(x)
    
    def pop(self):
        if self.q:
            return self.q.pop(0)
        else :
            return -1

    def size(self):
        return len(self.q)
    
    def is_empty(self):
        if self.q:
            return 0
        else:
            return 1
    
    def front(self):
        if self.q:
            return self.q[0]
        else:
            return -1
    
    def back(self):
        if self.q:
            return self.q[-1]
        else:
            return -1

if __name__ == "__main__":
    N = int(input())

    q = Queue()
    result = []

    for _ in range(N):
        command = list(input().split())
        cmd = command[0]

        if cmd == "push":
            q.push(int(command[1]))
        elif cmd == "pop":
            result.append(q.pop())
        elif cmd == "size":
            result.append(q.size())
        elif cmd == "empty":
            result.append(q.is_empty())
        elif cmd == "front":
            result.append(q.front())
        elif cmd == "back":
            result.append(q.back())
    
    for num in result:
        print(num)