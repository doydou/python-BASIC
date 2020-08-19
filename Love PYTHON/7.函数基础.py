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

'''
函数的参数
设置与传递参数是函数的重点，而 Python 的函数对参数的支持非常的灵活。
主要的参数类型有：默认参数、关键字参数（位置参数）、不定长参数。
下面我们将一一了解这几种参数。
'''
##默认参数-只要在构造函数的时候，给参数赋值就可以了
def print_user_info(name,age,sex='男'):
    #打印用户信息
    print('昵称：{}'.format(name),end=' ')
    print('年龄：{}'.format(age),end=' ')
    print('性别：{}'.format(sex))
    return


#调用 print_user_info函数
#不能声明函数形参的时候，先声明有默认值的形参，后声明没有默认值的形参
print_user_info('糕糕','23','女')

##关键字参数（位置参数）
'编写一个名为make_shirt() 的函数，它接受一个尺码以及要印到T恤上的字样。'
def make_shirt(word,size):
    print("衣服上印着{}".format(word))
    print("依附的大小是{}".format(size))


make_shirt(24,'L')#位置实参
make_shirt(word='糕糕',size='L')#关键字实参


'''函数的传值问题'''
def change_num( b ):
    b = 1000

b = 1
change_num(b)
print(b)#b还是等于1
# 变量赋值 a = 1,其实就是生成一个整形对象 1 ,然后变量 a 指向 1,
# 当 a = 1000 其实就是再生成一个整形对象 1000,然后改变 a 的指向,
# 不再指向整形对象 1 ,而是指向 1000,最后 1 会被丢弃

##返回简单值
def get_name(first_name,last_name):
    """返回名字"""
    full_name = first_name + ' ' + last_name
    return full_name.title()

czx = get_name('kristal','chan')
print(czx)

##返回字典
def build_person(first_name,last_name,age=' '):
    person = {'first':first_name,'last':last_name}
    if age:#age为可选形参....if age 表示True，继续运行
         person['age'] = age
    return person

czx = build_person('kristal','chan')
print(czx)

    #结合函数使用while循环
while True:
    print("\nPlease tell me your name")
    print("enter 'q' at any time to quit")

    f_name = input("first name: ")
    if f_name == 'q':
        break

    l_name = input("last name: ")
    if l_name == 'q':
        break

    xm = get_name(f_name,l_name)
    print("\nHello," + xm + "!")


##传递列表
    #打印列表中的信息
def say_hello(users):
    for name in users:
        message = "hello:" + name + '!'
        print(message)

usernames = ['糕糕','nene','墩墩']
say_hello(usernames)


    #在函数中修改列表




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