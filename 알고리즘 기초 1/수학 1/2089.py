# 백준 2089, -2진수

def to_negative_base_2(n):
    if n == 0:
        return "0"

    result = ""
    while n != 0:
        remainder = n % -2
        n //= -2

        if remainder < 0:
            remainder += 2
            n += 1
        
        result = str(remainder) + result
    
    return result

if __name__ == "__main__":
    decimal_number = int(input())
    negative_base_2 = to_negative_base_2(decimal_number)
    print(negative_base_2)