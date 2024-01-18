
while True:
    n = int(input())

    if n == -1:
        break

    lst = []
    for i in range(1, n):
        if n % i == 0:
            lst.append(i)
    
    result = 0
    for i in lst:
        result += i

    if result == n:
        print(str(n) + ' = ' + str(lst[0]), end=" ")
        for i in lst:
            if i != 1:
                print('+ ' + str(i), end= " ")
        print()
    else:
        print(str(n) + " is NOT perfect.")


