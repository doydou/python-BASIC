'''
类是对象的蓝图和模板，而对象是类的实例。
这个解释虽然有点像用概念在解释概念，但是从这句话我们至少可以看出，类是抽象的概念，而对象是具体的东西。
在面向对象编程的世界中，一切皆为对象，对象都有属性和行为，每个对象都是独一无二的，而且对象一定属于某个类（型）。
当我们把一大堆拥有共同特征的对象的静态特征（属性）和动态特征（行为）都抽取出来后，就可以定义出一个叫做“类”的东西。
'''
#定义类
class Student(object):

    #__init__是一个特殊方法用于在创建对象时进行初始化操作
    #通过这个方法我们可以为学生对象绑定name和age两个属性
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def study(self,course_name):
        print('%s正在学习%s' % (self.name,course_name))
    #标识符全小写用下划线连接
    def watch_film(self):
        if self.age < 18:
            print('%s只能看小电影' % self.name)
        else:
            print('%s可以看动作片' % self.name)

#创建和使用对象
def main():
    #创建学生对象
    student1 = Student('糕糕',23)
    #给对象发study消息
    student1.study('math')
    #给对象发watch——film消息
    student1.watch_film()


if __name__ == '__main__':
    main()


#练习1：定义一个类描述数字时钟
from time import sleep

class Clock():

    def __init__(self,hour=0,minute=0,second=0):
        self.hour = hour
        self.minute = minute
        self.second = second


    def runtime(self):
        #走字
        self.second += 1
        if self.second == 60:
            self.minute += 1
            self.second = 0
            if self.minute == 60:
                self.hour += 1
                self.minute = 0
                if self.hour == 24:
                    self.hour = 0

    def show(self):
        #显示时间
        return '%.2d:%.2d:%.2d' % \
                (self.hour,self.minute,self.second)

#调用函数
def main():
    clock = Clock(23, 59, 59)
    while True:
        print(clock.show())
        clock.runtime()
        sleep(1)

if __name__ == '__main__':
    main()


# 定义一个类描述平面上的点并提供移动点和计算到另一个点距离的方法。
