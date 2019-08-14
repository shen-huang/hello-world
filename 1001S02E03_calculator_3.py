# import sys
import math

ALLOWED = {v: getattr(math, v)
for v in filter(lambda x: not x.startswith('_'), dir(math))
}

# def calculate():
# while 1 :
#     str = input("请输入要计算的算式，回车进行计算，退出请输入“Q”：\n")
#     try:
#         if str =="Q":
#             print("感谢您的使用！再见！")
#             break
#             # sys.exit()
#         else:
#             print(eval(str, ALLOWED, {}))
#     except:
#         print("输入错误！")

# def again():
#     calculate()

# calculate()

print(eval(input()))