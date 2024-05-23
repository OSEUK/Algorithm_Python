# 백준 1062, 가르침 (GOLD IV)

def dfs(index, count, mask): # count = 포함된 알파벳의 개수
    global max_count

    # 현재 포함한 알파벳들로만 구성된 단어 개수 찾기
    if count == K:
        readable = 0
        for word_mask in word_masks:
            if word_mask & mask == word_mask:
                readable += 1
        max_count = max(max_count, readable)
        return

    # 이미 지나간 인덱스 탐색 X, mask에 포함 안된 알파벳만 dfs
    for i in range(index, 26):
        if not mask & (1 << i):
            dfs(i + 1, count + 1, mask | (1 << i))                             

if __name__ == "__main__":
    N, K = map(int, input().split())

    words = [input()[4:-4] for _ in range(N)]
    visited = [False] * N
    alpha = "antic"
    
    if K < 5:
        print(0)
        exit()
    
    base_mask = 0
    for char in alpha:
        base_mask |= (1 << (ord(char) - ord('a')))
    
    word_masks = []
    for word in words:
        mask = 0
        for char in word:
            mask |= (1 << (ord(char) - ord('a')))
        word_masks.append(mask)
    
    print(word_masks)
    max_count = 0
    dfs(0, 5, base_mask)
    print(max_count)
    
    