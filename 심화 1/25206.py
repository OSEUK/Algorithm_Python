def calc_credit(credit):
    if credit == 'A+':
        credit_score = 4.5
    elif credit == 'A0':
        credit_score = 4.0
    elif credit == 'B+':
        credit_score = 3.5
    elif credit == 'B0':
        credit_score = 3.0
    elif credit == 'C+':
        credit_score = 2.5
    elif credit == 'C0':
        credit_score = 2.0
    elif credit == 'D+':
        credit_score = 1.5
    elif credit == 'D0':
        credit_score = 1.0
    elif credit == 'F':
        credit_score = 0.0
    
    return float(credit_score)

total_count = 0
total_score = 0

for i in range(20):
    subject_list = input().split()
    
    count = float(subject_list[1])
    credit = subject_list[2]

    if credit == 'P':
        continue
    
    total_count += count
    credit_score = calc_credit(credit)
    total_score += count * credit_score

result = total_score / total_count
print('%.6f' %result)