# 백준 1107, 리모컨 (GOLD V)
# fail 

# 누를 수 있는지
def possible(num, broken):
    for digit in str(num):
        if digit in broken:
            return False
    return True

# 최소단위 계산
def min_press(target, broken):
    min_press_cnt = abs(target - 100)

    for num in range(1000001):
        if possible(num, broken):
            min_press_cnt = min(min_press_cnt, len(str(num)) + abs(num - target))

    return min_press_cnt

if __name__ == "__main__":
    target = int(input()) # 목표 채널
    n = int(input()) # 고장난 버튼의 개수
    broken = set(input().split()) if n > 0 else set()

    result = min_press(target, broken)
    print(result)

               