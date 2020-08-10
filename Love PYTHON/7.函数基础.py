'''
def 函数名 （参数1，参数2 ...）
    函数体
    return 语句
'''
#一个简单的例子
def add(num1,num2):
    return (num1+num2)
#调用函数
print(add(1,2))

#python中的函数可以返回多个值

'''
函数的参数
设置与传递参数是函数的重点，而 Python 的函数对参数的支持非常的灵活。
主要的参数类型有：默认参数、关键字参数（位置参数）、不定长参数。
下面我们将一一了解这几种参数。
'''
#默认参数-只要在构造函数的时候，给参数赋值就可以了
def print_user_info(name,age,sex='男'):
    #打印用户信息
    print('昵称：{}'.format(name),end=' ')
    print('年龄：{}'.format(age),end=' ')
    print('性别：{}'.format(sex))
    return


#调用 print_user_info函数
#不能声明函数形参的时候，先声明有默认值的形参，后声明没有默认值的形参
print_user_info('糕糕','23','女')

#关键字参数（位置参数）
# 不定长参数
# 只接受关键字参数


#函数的传值问题
def change_num( b ):
    b = 1000

b = 1
change_num(b)
print(b)#b还是等于1
# 变量赋值 a = 1,其实就是生成一个整形对象 1 ,然后变量 a 指向 1,
# 当 a = 1000 其实就是再生成一个整形对象 1000,然后改变 a 的指向,
# 不再指向整形对象 1 ,而是指向 1000,最后 1 会被丢弃

'''
匿名函数
python中使用后lambda创建匿名函数
lambda 只是一个表达式，函数体比 def 简单很多。
lambda 的主体是一个表达式，而不是一个代码块。仅仅能在 lambda 表达式中封装有限的逻辑进去。
lambda 函数拥有自己的命名空间，且不能访问自有参数列表之外或全局命名空间里的参数。
'''
#基本语法lambda [arg1 [,arg2,.....argn]]:expression

sum = lambda num1 , num2 : num1+num2;
print(sum(1,2))



#练习：
#写一个函数，判断用户传入的列表长度是否大于2，如果大于2，只保留前两个，并将新内容返回给调用者
def func(list):
    if len(list) > 2:
        return list[0:2]
    else:
        return list

print(func([1,2,3,4]))


#写函数，统计字符串中有几个字母，几个数字，几个空格，几个其他字符，并返回结果
def func1(s):#形参传递内容
    alpha = 0
    number = 0
    space = 0
    other = 0
    for i in s:
        if i.isalpha(): #检查字符串是否由数字组成
            alpha += 1
        elif i.isdigit():
            number += 1
        elif i.isspace():
            space += 1
        else:
            other += 1
    return [alpha,number,space,other]

r= func1("qwer 123")
print(r)

#写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新的列表返回给调用
def func2(p,q):
    result = []
    for i in range(len(p)):
        if i % 2 == 1:
            result.append(p[i])
    for j in range(len(q)):
        if j % 2 == 1:
            result.append(q[j])
    return result

text = func2([1,3,5,10],(1,6,123,7,4))
print(text)