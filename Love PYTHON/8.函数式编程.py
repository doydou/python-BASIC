'''
返回函数
高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。
'''
def get_name(frist_name,last_name):












# 练习：
# 写一个函数，判断用户传入的列表长度是否大于2，如果大于2，只保留前两个，并将新内容返回给调用者
def func(list):
    if len(list) > 2:
        return list[0:2]
    else:
        return list

print(func([1, 2, 3, 4]))

# 写函数，统计字符串中有几个字母，几个数字，几个空格，几个其他字符，并返回结果
def func1(s):  # 形参传递内容
    alpha = 0
    number = 0
    space = 0
    other = 0
    for i in s:
        if i.isalpha():  # 检查字符串是否由数字组成
            alpha += 1
        elif i.isdigit():
            number += 1
        elif i.isspace():
            space += 1
        else:
            other += 1
    return [alpha, number, space, other]

r = func1("qwer 123")
print(r)

# 写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新的列表返回给调用
def func2(p, q):
    result = []
    for i in range(len(p)):
        if i % 2 == 1:
            result.append(p[i])
    for j in range(len(q)):
        if j % 2 == 1:
            result.append(q[j])
    return result

text = func2([1, 3, 5, 10], (1, 6, 123, 7, 4))
print(text)