# 백준 11866, 요세푸스 문제 0

from collections import deque

def josephus(n, k):
    result = []
    people = deque(range(1, n+1))

    while people:
        people.rotate(-k+1)
        result.append(people.popleft())

    return result

if __name__ == "__main__":
    N, K = map(int, input().split())
    answer = josephus(N, K)
    print("<" + ", ".join(map(str, answer)) + ">")



