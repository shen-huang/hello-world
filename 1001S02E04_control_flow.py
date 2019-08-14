# -*- coding: UTF-8 -*-

# Filename : 1001S02E03_calculator.py
# author by : @shen-huang

# 打印两种九九乘法表

for i in range(1,10):
    for j in range(1,10):
        if(j<=i):
            print("{0}×{1}={2}".format(i, j, i*j), end='\t')
    print()
print()


for i in range(1,10):
    # while i%2==0:
    #     print(end="")
    #     break
    while i%2!=0:
        for j in range(1,i+1):
            print("{0}×{1}={2}".format(i, j, i*j), end='\t')
        print()
        break
print()

# for i in range(1,10):
#         for j in range(1,10):
#             while i%2!=0:
#                 if(j<=i):
#                     print("{0}×{1}={2}".format(j, i, i*j), end='\t')
#         print()
#         break

for i in range(1,10):
    while i%2!=0:
        for j in range(1,10):
            if(j<=i):
                print("{0}×{1}={2}".format(i, j, i*j), end='\t')
        print()
        break
print()