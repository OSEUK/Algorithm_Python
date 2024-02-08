# 백준 17298, 오큰수


def NGE(lst : list):
    stk = []
    result = [-1] * len(lst)

    for i in range(len(lst)):
        # 탐색하고있는 현재 값이 리스트 전 값보다 크다면
        while stk and lst[i] > lst[stk[-1]]:
            # 그 값을 이전 인덱스의 오큰수로 지정
            result[stk.pop()] = lst[i]
        stk.append(i)

    return result

if __name__ == "__main__":
    N = int(input())
    lst = list(map(int, input().split()))   

    result = NGE(lst)

    print(*result)