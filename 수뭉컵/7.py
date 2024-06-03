# 슈퍼넷팅

T = int(input())

for _ in range(T):
    num = int(input())
    addr = list()
    for i in range(num):
        addr.append(list(input().split('.')))
    
    for i in range(num):
        addr[i][-1].split('/')

    print(addr)