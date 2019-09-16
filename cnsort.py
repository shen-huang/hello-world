# coding: utf-8
# 中文排序样例
# Sorting Chinese Character
# henrysting@163.com
# 2009-12-25

# import re

# 建立拼音辞典
dic_py = dict()
f_py = open('py.txt', 'r', encoding='UTF-8')
content_py = f_py.read()
lines_py = content_py.split('\n')
n = len(lines_py)
# 将line用\t进行分割，最多分一次变成两块，保存到word和mean中去
for i in range(0, n-1):
    word_py, mean_py = lines_py[i].split('\t', 1)
    dic_py[word_py] = mean_py
f_py.close()

# 建立笔画辞典
dic_bh = dict()
f_bh = open('bh.txt', 'r', encoding='UTF-8')
content_bh = f_bh.read()
lines_bh = content_bh.split('\n')
n = len(lines_bh)
# 将line用\t进行分割，最多分一次变成两块，保存到word和mean中去
for i in range(0, n-1):
    word_bh, mean_bh = lines_bh[i].split('\t', 1)
    dic_bh[word_bh] = mean_bh
f_bh.close()


# 辞典查找函数
def searchdict(dic, uchar):
    if isinstance(uchar, str):
        uchar_h = uchar.encode('unicode_escape').decode("utf-8")
        if uchar_h >= '\\u4e00' and uchar_h <= '\\u9fa5':
            value = dic.get(uchar)
            if value is None:
                value = '*'
        else:
            value = uchar
    else:
        value = uchar
    return value


# 比较单个字符
def comp_char_PY(A, B):
    if A == B:
        return -1
    pyA = searchdict(dic_py, A)
    pyB = searchdict(dic_py, B)
    if pyA > pyB:
        return 1
    elif pyA < pyB:
        return 0
    else:
        bhA = int(searchdict(dic_bh, A))
        bhB = int(searchdict(dic_bh, B))
        if bhA > bhB:
            return 1
        elif bhA < bhB:
            return 0
        else:
            uniA = A.encode('unicode_escape').decode("utf-8")
            uniB = B.encode('unicode_escape').decode("utf-8")
            if uniA > uniB:
                return 1
            elif uniA < uniB:
                return 0
            else:
                return "Are you kidding?"


# 比较字符串
def comp_char(A, B):
    charA = A
    charB = B
    n = min(len(charA), len(charB))
    i = 0
    while i < n:
        dd = comp_char_PY(charA[i], charB[i])
        if dd == -1:
            i = i + 1
            if i == n:
                dd = len(charA) > len(charB)
        else:
            break
    return dd


# 排序函数
def cnsort(nline):
    n = len(nline)
    # lines = "\n".join(nline)
    for i in range(1, n):  # 插入法
        tmp = nline[i]
        j = i
        while j > 0 and comp_char(nline[j-1], tmp):
            nline[j] = nline[j-1]
            j = j - 1
        nline[j] = tmp
    return nline
