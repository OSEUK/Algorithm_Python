# 백준 2004, 조합 0의 개수

def count_twos(n):
    count = 0
    while n >= 2:
        count += n // 2
        n //= 2
    return count

def count_fives(n):
    count = 0
    while n >= 5:
        count += n // 5
        n //= 5
    return count

def count_zeros_in_combination(n, m):
    twos = count_twos(n) - count_twos(m) - count_twos(n-m)
    fives = count_fives(n) - count_fives(m) - count_fives(n-m)
    return min(twos, fives)

if __name__ == "__main__":
    n, m = map(int, input().split())
    print(count_zeros_in_combination(n, m))