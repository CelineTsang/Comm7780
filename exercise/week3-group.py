studentslist = [
18421111,
18421112,
18421113,
18421114,
18421115,
18421116,
18421117,
18421118,
18421119,
18421120,
18421121,
18421122,
18421123,
18421124,
18421125,
18421126,
18421127,
18421128,
18421129,
18421130,
18421131,
18421132,
18421133,
18421134,
18421135,
18421136,
18421137,
18421138,
18421139,
18421140,
18421141,
18421142,
18421143,
18421144,
18421145,
18421146,
18421147,
18421148,
18421149,
18421150,
18421151,
18421152,
18421153,
18421154,
18421155,
18421156,
18421157,
18421158,
18421159,
18421160,
]
import random
random.shuffle(studentslist)

caselist =[
'case1 - build a calculator to evaluate your business model',
'case2 - build a automatic earthquake robot to broadcast the new earthquake',
'case3 - evaluate social media performance of a luxury brand',
'case4 - study movie blockbuster \'Dying to Survive\'',
'case5 - invest your money like the Internet giant, Tencent',
'case6 - where are the 200,000 inferior vaccines flowing?',
'case7 - study classics, Who control the discourse power in \'Dream of the Red Chamber\'',
'case8 - research about Didi-driver crimes in China',
'case9 - \'Me too\' analysis',
'case10 - what is hip-hop in china?'
]

random.shuffle(caselist)
i = 0
for i in range(0, 10):
    print('group{}'.format(i+1))
    print("student ID {}".format(studentslist[i*5]))
    print("student ID {}".format(studentslist[i*5+1]))
    print("student ID {}".format(studentslist[i*5+2]))
    print("student ID {}".format(studentslist[i*5+3]))
    print("student ID {}".format(studentslist[i*5+4]))
    print("assigned case {}".format(caselist[i]))
    print("======================")


output

group1
student ID 18421131
student ID 18421114
student ID 18421141
student ID 18421143
student ID 18421121
assigned case case10 - what is hip-hop in china?
======================
group2
student ID 18421153
student ID 18421160
student ID 18421136
student ID 18421137
student ID 18421117
assigned case case6 - where are the 200,000 inferior vaccines flowing?
======================
group3
student ID 18421127
student ID 18421149
student ID 18421142
student ID 18421144
student ID 18421130
assigned case case3 - evaluate social media performance of a luxury brand
======================
group4
student ID 18421159
student ID 18421124
student ID 18421150
student ID 18421126
student ID 18421158
assigned case case1 - build a calculator to evaluate your business model
======================
group5
student ID 18421128
student ID 18421123
student ID 18421154
student ID 18421125
student ID 18421132
assigned case case5 - invest your money like the Internet giant, Tencent
======================
group6
student ID 18421129
student ID 18421155
student ID 18421156
student ID 18421122
student ID 18421147
assigned case case8 - research about Didi-driver crimes in China
======================
group7
student ID 18421119
student ID 18421112
student ID 18421152
student ID 18421157
student ID 18421146
assigned case case2 - build a automatic earthquake robot to broadcast the new earthquake
======================
group8
student ID 18421135
student ID 18421115
student ID 18421133
student ID 18421113
student ID 18421151
assigned case case4 - study movie blockbuster 'Dying to Survive'
======================
group9
student ID 18421139
student ID 18421118
student ID 18421145
student ID 18421138
student ID 18421134
assigned case case9 - 'Me too' analysis
======================
group10
student ID 18421148
student ID 18421120
student ID 18421140
student ID 18421116
student ID 18421111
assigned case case7 - study classics, Who control the discourse power in 'Dream of the Red Chamber'
======================



