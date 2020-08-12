'''
方法和函数	        描述
len(dict)	        计算字典元素个数
str(dict)	        输出字典可打印的字符串表示
type(variable)	    返回输入的变量类型，如果变量是字典就返回字典类型
dict.clear()	    删除字典内所有元素
dict.copy()	        返回一个字典的浅复制
dict.values()	    以列表返回字典中的所有值
popitem()	        随机返回并删除字典中的一对键和值
dict.items()	    以列表返回可遍历的(键, 值) 元组数组
'''
#创建字典
dict1 = {1:'豆豆',2:'胖胖',3:'nene'}
#通过键可以获取字典中对应的值
print(dict1[1])
#对字典进行遍历
for i in dict1:
    print('%d--->%s' % (i,dict1[i]))
#对字典更新元素
dict1[1] = '糕糕'
dict2 = {4:'粤粤'}
dict1.update(dict2)
print(dict1)
#通过键获取对应的值
print(dict1.get(1))
#删除字典中的元素
print(dict1.pop(2))
print(dict1)