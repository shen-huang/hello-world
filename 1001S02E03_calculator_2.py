import math
ALLOWED = {v: getattr(math, v)
for v in filter(lambda x: not x.startswith('_'), dir(math))
}

def calculate():
    print("请输入要计算的算式：")
    try:
        print(eval(input(), ALLOWED, {}))
    except:
        print("输入错误！")
    again()

def again():
    print("是否需要计算其他算式？是请输入 Y，退出请输入 N：")
    if input()=="Y":
        calculate()
    else:
        print("感谢您的使用！再见！")

calculate()
