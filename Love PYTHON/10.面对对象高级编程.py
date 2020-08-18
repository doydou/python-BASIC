#面对对象的三大支柱：封装，继承和多态
'''在类中定义的方法其实就是把数据和对数据的操作封装起来了，在我们创建了对象之后，只需要给对象发送一个消息（调用方法）
就可以执行方法中的代码，也就是说我们只需要知道方法的名字和传入的参数（方法的外部视图）
而不需要知道方法内部的实现细节（方法的内部视图）。
'''

#访问可见性问题
"""
在python中，属性和方法的访问权限只有两种，也就是公开的（public）和私有的（privacy）。
如果希望属性是私有的，在给属性命名时可以用两个下划线作为开头。
"""
class Test(object):

    def __init__(self,name):
        self.__name = name

    def print_name(self):
        print(' %s ' % (self.__name))

def main():
    test = Test('hello,world')
    '''test.__name()'''  #AttributeError: 'Test' object has no attribute '__name'

if __name__== "__main__":
    main()


'''
@property装饰器
如果想访问属性可以通过属性的getter（访问器）和setter（修改器）方法进行对应的操作。
如果要做到这点，就可以考虑使用@property包装器来包装getter和setter方法，使得对属性的访问既安全又方便，代码如下所示。
'''

class Person(object):
    def __init__(self,name,age):
        self._name = name
        self._age = age
    #访问器-getter方法
    @property
    def name(self):
        return self._name

    #访问器-getter方法
    @property
    def age(self):
        return self._age
    #修改器-setter方法
    @age.setter
    def age(self,age):
        self._age = age

    def play(self):
        if self._age < 16:
            print('%s玩象棋' % self._name)
        else:
            print('%s玩大象' % self._name)

def main():
    person = Person('糕糕',23)
    person.play()
    person.age=12
    person.play()
     #person.name = '豆豆'  #AttributeError: can't set attribute
    person.play()

if __name__ == '__main__':
    main()


'''
__slots__魔法
动态语言允许在程序运行时给对象绑定新的属性或方法，
当然也可以对已经绑定的属性和方法进行解绑定。但是如果需要限定自定义类型的对象只能绑定某些属性，
可以通过在类中定义__slots__变量来进行限定。需要注意的是__slots__的限定只对当前类的对象生效，对子类并不起任何作用。
'''
