repeat_num = int(input())
count_group_word = 0 
alphabet_count = [0] * 26
group_ok = True

for i in range(repeat_num):
    str = input()
    for char in str:
        if alphabet_count[ord(char) - ord('a')] == 1 and p != char:
            group_ok = False    
            break
        p = char    
        alphabet_count[ord(char) - ord('a')] = 1
    
    if group_ok == True:
        count_group_word += 1
    
    group_ok = True
    alphabet_count = [0]*26

print(count_group_word) 