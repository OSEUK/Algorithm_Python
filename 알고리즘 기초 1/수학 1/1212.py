# 백준 1212, 8진수 2진수

import sys
input = sys.stdin.readline

def octToBin(octal):
    binary = []
    for digit in octal:
        binary.append(bin(int(digit, 8))[2:].zfill(3))
    
    return binary


if __name__ == "__main__":
    oct_num = input().strip()

    binary = octToBin(oct_num)
    res = "".join(binary).lstrip("0")
    if res == "":
        res = 0
    print(res)