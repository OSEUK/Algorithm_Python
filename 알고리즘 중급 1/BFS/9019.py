# 백준 9019, DSLR (GOLD IV)

import sys
input = sys.stdin.readline
from collections import deque

def D(n : int) -> int:
    result = (n * 2) % 10000
    return result

def S(n : int) -> int:
    if n == 0:
        result = 9999
    else:
        result = n - 1
    return result

def split_number(n : int) -> tuple:
    d1 = int(n / 1000)
    mod = n % 1000
    d2 = int(mod / 100)
    mod = mod % 100
    d3 = int(mod / 10)
    mod = mod % 10
    d4 = int(mod)
    return d1, d2, d3, d4

def L(n : int) -> int:
    d1, d2, d3, d4 = split_number(n)
    result = int(str(d2) + str(d3) + str(d4) + str(d1))
    return result

def R(n : int) -> int:
    d1, d2, d3, d4 = split_number(n)
    result = int(str(d4) + str(d1) + str(d2) + str(d3))
    return result


def bfs(A : int, B : int) -> str:
    visited = [False] * 10000
    numbers = [(0, "")] * 4
    q = deque()
    q.append((A, ""))

    while q:
        n, command = q.popleft()

        if n == B:
            return command
        
        numbers[0] = (D(n) , 'D')
        numbers[1] = (S(n) , 'S')
        numbers[2] = (L(n) , 'L')
        numbers[3] = (R(n) , 'R')

        for num in numbers:
            if not visited[num[0]]:
                q.append((num[0], command + num[1]))
                visited[num[0]] = True
    

if __name__ == "__main__":
    T = int(input())

    for _ in range(T):
        A, B = map(int, input().split())

        print(bfs(A, B))

