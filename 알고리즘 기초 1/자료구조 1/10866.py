# 백준 10866, 덱

class Deque:
    
    def __init__(self):
        self.deq = []

    def push_front(self, x):
        self.deq.insert(0, x)
    
    def push_back(self, x):
        self.deq.append(x)
    
    def pop_front(self):
        if self.deq:
            return self.deq.pop(0)
        else:
            return -1
    
    def pop_back(self):
        if self.deq:
            return self.deq.pop()
        else:
            return -1
    
    def size(self):
        return len(self.deq)
    
    def is_empty(self):
        if self.deq:
            return 0
        else:
            return 1
    
    def front(self):
        if self.deq:
            return self.deq[0]
        else:
            return -1
    
    def back(self):
        if self.deq:
            return self.deq[-1]
        else:
            return -1
        
if __name__ == "__main__":
    
    N = int(input())
    deq = Deque()
    result = []
    for _ in range(N):
        command = list(input().split())
        cmd = command[0]

        if cmd == "push_front":
            deq.push_front(int(command[1]))
        elif cmd == "push_back":
            deq.push_back(int(command[1]))
        elif cmd == "pop_front":
            result.append(deq.pop_front())
        elif cmd == "pop_back":
            result.append(deq.pop_back())
        elif cmd == "size":
            result.append(deq.size())
        elif cmd == "empty":
            result.append(deq.is_empty())
        elif cmd == "front":
            result.append(deq.front())
        elif cmd == "back":
            result.append(deq.back())
        
    for num in result:
        print(num)
        
