# P = 10 ** 7
# r = 5 / 100 / 12
# A = 450000
# n = 20 * 12
# A = P * r * (1 + r)**n / ((1 + r) **n- 1)
# print('P=', P)
# print('r=', r)
# print('n=', n)
# print('A=', A)

# print header
# print('Month	Instalment	Interest	Principal	Outstanding')
# print first data row
# month=0
# A:monthly payment
# outstanding = P
# def print_one_month(month,outstanding):
    # month= month + 1
    # interest = r * outstanding
    # principal = A - r * outstanding
    # outstanding = outstanding - principal
    # print('{0:03d}\t {1:.2f}\t {2:.2f}\t{3:.2f}\t{4:.2f}\t {1:.2f}'.format( month, A, interest, principal, outstanding ))
    # return month,outstanding

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

#repeat 5 times:
headers = ['month','Instalment','Interest','Principal','Outstanding']
for i in range(5):
    #print(i,'th','header')
#refer the ith element in the list'headers'
    print(headers[i],'\t',end='')
    # end=" " in one line 每个的结束后都会有的内容 不写end就换行

parameter1 = {
    'principal': 10 ** 7,
    'interest': 5 / 100 / 12,
    'period': 20 * 12
}

parameter2 = {
    'principal': 10 ** 7,
    'interest': 5 / 100 / 12,
    'period': 30 * 12
}

parameter3 = {
    'principal': 10 ** 7,
    'interest': 10 / 100 / 12,
    'period': 30 * 12
}

parameters = [parameter1, parameter2, parameter3]

parameters = [
    {
    'principal': 0.5 * 10 ** 7,
    'interest': 5 / 100 / 12,
    'period': 20 * 12
    },
    {
    'principal': 10 ** 7,
    'interest': 5 / 100 / 12,
    'period': 30 * 12
    },
    # {
    # 'principal': 10 ** 7,
    # 'interest': 10 / 100 / 12,
    # 'period': 30 * 12
    # },
    # {
    # 'principal': 10 ** 7,
    # 'interest': 10 / 100 / 12,
    # 'period': 40 * 12
    # },
]



# ==== following are generic === 

for i in range(len(parameters)):
    parameter = parameters[i]

    P = parameter['principal']
    r = parameter['interest']
    n = parameter['period']
    A = P * r * (1 + r) ** n / ((1 + r) ** n - 1)

    print(parameter)
    print('offer=', i, 'A=', A)
    print()



# while True:
#     month,outstanding = print_one_month(month,outstanding)
#     if outstanding <=0:
#         break


    