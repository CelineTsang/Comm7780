P = 10 ** 7
r = 5 / 100 / 12
A = 45000
# n = 20 * 12
# A = P * r * (1 + r)**n / ((1 + r) **n- 1)
print('P=', P)
print('r=', r)
# print('n=', n)
# print('A=', A)

# print header
print('Month	Instalment	Interest	Principal	Outstanding')
# print first data row
month=0
# A:monthly payment
outstanding = P
def print_one_month(month,outstanding):
    month= month + 1
    interest = r * outstanding
    principal = A - r * outstanding
    outstanding = outstanding - principal
    print('{0:03d}\t {1:.2f}\t {2:.2f}\t{3:.2f}\t{4:.2f}'.format( month, A, interest, principal, outstanding ))
    return month,outstanding

# month,outstanding = print_one_month(month,outstanding)
# # paste once repeat once

# for i in range(999):
#     month,outstanding = print_one_month(month,outstanding)
    #if outstanding <=0 then stop the loop
    # if outstanding <=0:
    #     break
# i = 0
# while i < 99999
#     i = i+1
while True:
    month,outstanding = print_one_month(month,outstanding)
    if outstanding <=0:
        break


    
