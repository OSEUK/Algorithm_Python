# 백준 18870, 좌표 압축 (어려움)

N = int(input())

numbers = list(map(int, input().split()))

sorted_numbers = sorted(set(numbers))

coordinate_dic = {value: index for index, value in enumerate(sorted_numbers)}

result = [coordinate_dic[number] for number in numbers]
print(*result)

