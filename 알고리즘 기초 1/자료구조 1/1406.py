# 백준 1406, 에디터
# 커서라는 요소를 스택 두개로 나누는 발상이 중요한 것 같다.

import sys

input = sys.stdin.readline

class Editer:

    def __init__(self, s):
        self.left_stk = list(s)
        self.right_stk = []        

    def toLeft(self):
        if self.left_stk:
            self.right_stk.append(self.left_stk.pop())
    
    def toRight(self):
        if self.right_stk:
            self.left_stk.append(self.right_stk.pop())
    
    def delete(self):
        if self.left_stk:
            self.left_stk.pop()
    
    def push(self, chr):
        self.left_stk.append(chr)
    
    def print_string(self):
        print(''.join(self.left_stk + self.right_stk[::-1]))        

if __name__ == "__main__":
    s = input().rstrip()

    editor = Editer(s)
    
    M = int(input())
    for _ in range(M):
        command = list(map(str,input().split()))
        cmd = command[0]

        if cmd == 'L':
            editor.toLeft()
        elif cmd == 'D':
            editor.toRight()
        elif cmd == 'B':
            editor.delete()
        elif cmd == 'P':
            editor.push(command[1])
    
    editor.print_string()