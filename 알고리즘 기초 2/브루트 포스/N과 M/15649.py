# 백준 15649, N과 M (1)  (SILVER III)

def permutation(arr, result, n, m):
    if len(result) == m:  # 결과 배열의 길이가 M이 되면 출력
        print(' '.join(map(str, result)))
        return

    for i in range(len(arr)):
        next_arr = arr[:i] + arr[i+1:]  # 현재 원소 제외한 배열
        permutation(next_arr, result + [arr[i]], n, m)

if __name__ == "__main__":
    n, m = map(int, input().split())
    numbers = [i for i in range(1, n+1)]
    permutation(numbers, [], n, m)
