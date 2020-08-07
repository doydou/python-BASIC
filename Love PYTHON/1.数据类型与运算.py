'''第一节 对象及数字对象
在程序设计中，变量是一种存储数据的载体。
计算机中的变量是实际存在的数据或者说是存储器中存储数据的一块内存空间，变量的值可以被读取和修改，这是所有计算和控制的基础。
计算机能处理的数据有很多中类型，除了数值之外还可以处理文本、图形、音频、视频等各种各样的数据，
那么不同的数据就需要定义不同的存储类型。'''

"""
使用input函数输入
使用int()进行类型转换
用占位符格式化输出的字符串
"""
a = int(input('a = '))
b = int(input('b = '))
print('%d + %d = %d' % (a, b, a + b))
print('%d - %d = %d' % (a, b, a - b))
print('%d * %d = %d' % (a, b, a * b))
print('%d / %d = %f' % (a, b, a / b))
print('%d // %d = %d' % (a, b, a // b))
print('%d %% %d = %d' % (a, b, a % b))
print('%d ** %d = %d' % (a, b, a ** b))

"""
使用type()检查变量的类型
"""
a = 100
b = 12.345
c = 1 + 5j
d = 'hello, world'
e = True
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))


#字符串的使用
str1 = "hello,world!"
#通过len函数计算字符串的长度
print(len(str1))#13
#字符串的首字母大写
print(str1.capitalize())#HELLO, WORLD!
#获得字符串所有字母变大写
print(str1.upper())
#从字符串中查找子串的位置
print(str1.find('or'))#7
print(str1.find('shit'))#-1

str2 = 'abc123456'
#从字符串中取出指定位置的字符
print(str2[2])
#字符串切片(从指定的开始索引到指定的结束索引)
print(str2[2:5])#c12
print(str2[2:])
print(str2[2::2])#2 to the end，step=2
print(str2[::2])#step=2
print(str2[::-1])#逆
print(str2[-3:-1])#45

#练习
"""
1。计算并打印出 993 + 196 的和， 乘以 7 的积， 然后除以3
2.计算并打印出 993 + 196 的和，乘以 7 的积， 然后除以3 的 商 和 余数
3.将华氏温度转换为摄氏温度（F = 1.8C + 32）
4.输入半径计算圆的周长和面积
5.输入年份，判断是否是闰年
"""
f = float(input("请输入华式温度为："))
c = (f-32)/1.8
print("%.1f华式度=%.1f摄氏度"%(f,c))


import math
radius = float(input("请输入半径："))
perimeter = 2*math.pi*radius
area = math.pi*radius*radius
print("园的周长为{:.2}，面积为{:.2}".format(perimeter,area))

year = int(input("请输入年份:"))
if year % 3 == 0 and year % 100 == 0 and year % 400 != 0:
    print("{}是闰年".format(year))
else:
    print("{}不是闰年".format(year))


print((993 + 136)*7/3)#"/"是除号
print((993+136)*7//3)#商
print((993+196)*7%3)#余数