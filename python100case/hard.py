'''
题目一：编写一个程序，根据给定的公式计算并打印值： Q = [(2 * C * D)/H] 的平方根
以下是 C 和 H 的固定值：C 为 50。H 为 30 . D 是变量，其值应该以逗号分隔的顺序输入到您的程序中。
示例 让我们假设以下逗号分隔的输入序列被提供给程序：100,150,180 程序的输出应该是：18,22,24
'''
import math
c = 50
h = 30
value = []
items = [x for x in input().split()]
for d in items:
    value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))

print(value)
