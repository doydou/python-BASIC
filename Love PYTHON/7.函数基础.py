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
