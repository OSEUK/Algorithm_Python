# 백준 1373, 2진수 8진수

import sys
input = sys.stdin.readline

if __name__ == "__main__":
    binary = input()  # 이진수 입력 받기
    decimal = int(binary, 2)  # 이진수를 10진수로 변환
    octal = oct(decimal)  # 10진수를 8진수 문자열로 변환
    print(octal[2:])  # '0o' 부분은 출binary = input()  # 이진수 입력 받기