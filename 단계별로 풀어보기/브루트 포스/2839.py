# 백준 2839, 설탕 배달

N = int(input())
M = N
result = 0
succeed = True

# 5로 나눈 몫이 0이면 출력
if M % 5 == 0 and M >= 5:
    result += M // 5
else:
    result += M // 5
    M = N % 5

    # 3으로 나눠질 때 까지 반복한다.
    while M <= N:
        if M % 3 == 0:
            result += M // 3
            break
        else:
            result -= 1
            M = M + 5
    if M > N:
        succeed = False

if succeed:
    print(result)
else:
    print(-1)