'''
第三节：元组
tuple 和 List 非常类似，但是 tuple 一旦初始化就不能修改。 也就是说元组（tuple）是不可变的，那么不可变是指什么意思呢？
元组（tuple） 不可变是指当你创建了 tuple 时候，它就不能改变了，也就是说它也没有 append()，insert() 这样的方法，
但它也有获取某个索引值的方法，但是不能赋值。
那么为什么要有 tuple 呢？
那是因为 tuple 是不可变的，所以代码更安全。
所以建议能用 tuple 代替 list 就尽量用 tuple 。
'''
#创建元组(tuple)
tuple1 = ('糕糕','shuangshuang','nene','宁宁','972126')
tuple2 = ('潇潇','凡凡','丑丑')
list = [1,2,3,4,5]
#计算元素个数
print(len(tuple1))
#获取元组中的元素
print(tuple1[0])
#连接，两个元素相加
print(tuple1+tuple2)
#复制元组
print(tuple1*2)
#元素是否存在糕糕
print('糕糕' in tuple1)
# 将列表转换为元组
print(tuple(list))

'''
方法	    描述
len(tuple)	计算元组元素个数
max(tuple)	返回元组中元素最大值
min(tuple)	返回元组中元素最小值
tuple(seq)	将列表转换为元组
'''