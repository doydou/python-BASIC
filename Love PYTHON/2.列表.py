'''
第二节：列表（List）是 Python 内置的一种数据类型。 它是一种有序的集合，可以随时添加和删除其中的元素。
'''
#1.创建列表
name=['糕糕','饼饼','nene','宁宁','胖胖']
#2.通过索引来访问列表
print(name[2])
#3.通过【】的形式来截取列表中的数据
print(name[0:2])#左闭右开区间
#4.更新列表(使用append()方法来添加列表项)
name.append("凡凡")
print(name)
name.insert(1,400)
#5.删除列表中的元素，使用del语句来删除列表中的元素
del name[3]
print(name)
#6删除末尾元素用pop()
name.pop()
print(name)
#7删除指定位置元素
name.pop(1)
print(name)
#8下标（索引）运算
print(name[0])
print(name[-1])
# 清空列表元素
"name.clear()"
#对列表进行切片
fruits = ['grape','apple','strawberry']
fruits += ['pitaya','pear','watermelon']
#循环遍历列表元素
for fruit in fruits:
        print(fruit.title(),end= '\t')
#列表切片
fruits2 = fruits[1:4]
print(fruits2)
#可以通过完整切片来复制列表
fruits3 = fruits[:]
print(fruits3)
#反向切片
fruits5 = fruits[::-1]
print(fruits5)
#对列表的排序
list1 =['orange','apple','zoo','internationalization','blueberry']
list2 = sorted(list1)
#给列表对象发出排序消息直接再列表对象上排序
list1.sort(reverse=True)#按照倒序，reverse=false，正序
print(list1)
'''
函数&方法	                    描述
len(list)	                    列表元素个数
max(list)	                    返回列表元素最大值
min(list)	                    返回列表元素最小值
list(seq)	                    将元组转换为列表
list.append(obj)	            在列表末尾添加新的对象
list.count(obj)	                统计某个元素在列表中出现的次数
list.extend(seq)	            在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
list.index(obj)	                从列表中找出某个值第一个匹配项的索引位置
list.insert(index, obj)	        将对象插入列表
list.pop(obj=list[-1])	        移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
list.remove(obj)	            移除列表中的一个元素（参数是列表中元素），并且不返回任何值
list.reverse()	                反向列表中元素
list.sort([func])	            对原列表进行排序
'''
