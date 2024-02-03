# 백준 9093, 단어 뒤집기

def reverse_word(lst):
    result = []
    for word in lst:
        reversed_word = ''.join(reversed(word))
        result.append(reversed_word)
    
    return result

if __name__ == "__main__":
    T = int(input())

    for _ in range(T):
        lst = list(map(str, input().split()))
        print(*reverse_word(lst))