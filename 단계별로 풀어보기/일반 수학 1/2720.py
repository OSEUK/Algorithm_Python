T = int(input())

for i in range(T):
    C = int(input())

    quotient = C // 25
    remainder = C % 25    

    print(quotient, end = " ")

    quotient = remainder // 10
    remainder = remainder % 10
    

    print(quotient, end = " ")

    quotient = remainder // 5
    remainder = remainder % 5
    
    print(quotient, end = " ")

    quotient = remainder

    print(quotient)
