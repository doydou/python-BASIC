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
tuple1=('糕糕','shuangshuang','nene','宁宁','972126')
