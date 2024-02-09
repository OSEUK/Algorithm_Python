word = input().upper()  # 대소문자 구분을 없애기 위해 입력 받은 단어를 대문자로 변환
alphabet_count = [0] * 26  # 알파벳의 개수를 저장할 리스트 초기화

for char in word:
    if 'A' <= char <= 'Z':
        alphabet_count[ord(char) - ord('A')] += 1  # 각 알파벳의 등장 횟수 증가

max_count = max(alphabet_count)  # 가장 많이 등장하는 알파벳의 개수 찾기

if alphabet_count.count(max_count) > 1:
    print('?')  # 최댓값이 중복되면 '?' 출력
else:
    max_index = alphabet_count.index(max_count)  # 최댓값의 인덱스 찾기
    result_char = chr(max_index + ord('A'))  # 해당 인덱스를 알파벳으로 변환
    print(result_char)
