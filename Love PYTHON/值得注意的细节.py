'''注意1.
in range(2,2)会生成nothing，直接跳过这个循环。
for i in range(2, 2):
    if i is None:
        print('none')
    print(type(i))
    print(i)
print(type(i))'''

'''
注意2.
在for循环完整完成后才执行else；如果中途从break跳出，则连else一起跳出。
#特别需要注意的是如果for中有if语句，else的缩进一定要和for对齐，如果和if对齐，则变成if－else语句
'''


'''
注意3.
isinstance() 函数来判断一个对象是否是一个已知的类型，类似 type()。 
isinstance() 与 type() 区别：
type() 不会认为子类是一种父类类型，不考虑继承关系。
isinstance() 会认为子类是一种父类类型，考虑继承关系。 
如果要判断两个类型是否相同推荐使用 isinstance()。
'''

'''
注意4.
在 Python 中，字符串，整形，浮点型，tuple 是不可更改的对象，而 list ， dict 等是可以更改的对象。
'''
