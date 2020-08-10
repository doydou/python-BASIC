'''
Python中的集合跟数学上的集合是一致的，不允许有重复元素，而且可以进行交集、并集、差集等运算。
'''
set1 = {1,2,2,4,4}
print('length=',len(set1))
set2 = set(range(1,10))
print(set2)
#添加元素
set1.add(5)
set2.update([11,12])
print(set1)
print(set2)
#remove的元素如果不存在会引发KeyError
if 4 in set2:
    set2.remove(4)
print(set2)
# 集合的交集、并集、差集、对称差运算
print(set1 & set2)#set1.intersection(set2)
print(set1 | set2)#set1.union(set2)
print(set1 - set2)#set1.difference(set2)
print(set1 ^ set2)#set1.symmetric_difference(set2)
# 判断子集和超集
print(set2 <= set1)
# print(set2.issubset(set1))
print(set2 <= set1)
# print(set3.issubset(set1))
print(set1 >= set2)
# print(set1.issuperset(set2))
print(set1 >= set2)
# print(set1.issuperset(set3))
