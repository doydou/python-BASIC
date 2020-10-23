'''
类是对象的蓝图和模板，而对象是类的实例。
这个解释虽然有点像用概念在解释概念，但是从这句话我们至少可以看出，类是抽象的概念，而对象是具体的东西。
在面向对象编程的世界中，一切皆为对象，对象都有属性和行为，每个对象都是独一无二的，而且对象一定属于某个类（型）。
当我们把一大堆拥有共同特征的对象的静态特征（属性）和动态特征（行为）都抽取出来后，就可以定义出一个叫做“类”的东西。
'''
##使用类和实例--创建car类
class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_num = 0 #给属性指定默认的值

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        full_name = str(self.year) + ' ' + self.model + ' ' + self.make
        return full_name

    def read_odometer(self):
        print('this car has ' + str(self.odometer_num) + ' miles on road')

    """2.方法
    对car类添加一个新的方法
    """
    def update_odometer(self,mileage):
        """将里程数设置为指定的值"""
        self.odometer_num = mileage
    """3.方法
    对属性的值进行递增
    """
    def increment_odometer(self,miles):
        self.odometer_num += miles

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

#修改属性的值
#1.直接修改属性的值
my_new_car.odometer_num = 33
my_new_car.read_odometer()
#2.通过方法修改属性的值
my_new_car.update_odometer(23)
my_new_car.read_odometer()
#3.通过方法对属性的值进行递增
my_new_car.increment_odometer(10)
my_new_car.read_odometer()

'''
继承——一个类继继承承 另一个类时，它将自动获得另一个类的所有属性和方法；原有的 类称为父父类类 ，而新类称为子子类类 。
子类继承了其父类的所有属性和方法，同时还可以定义自己的属性和方法。
'''
#创建子类
# class ElectricCar(Car):
#
#     def __init__(self,make,model,year):#初始化父类的属性
#         #调用父类
#         super().__init__(make,model,year)
#
# my_Tesla = ElectricCar('tesla',"model's",2020)
# print(my_Tesla.get_descriptive_name())

#将实例用作属性
class Battery():#定义一个新的类，他没有继承任何类

    def __init__(self,battery_size = 70):#初始化电瓶的属性
        self.battery_size = battery_size

    def describe_battey(self):
        """描述电瓶的容量"""
        print("这是个含有" + str(self.battery_size) + "容量的电池")


class ElectricCar(Car):

    def __init__(self,make,model,year):#初始化父类的属性
        #调用父类
        super().__init__(make,model,year)
        self.battery = Battery()#添加了一个名为self.battery的属性，将Battery实例储存再属性self.battert中

my_Tesla = ElectricCar('tesla',"model's",2020)
print(my_Tesla.get_descriptive_name())
my_Tesla.battery.describe_battey()



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
class Distance():
    #定义一个类
    def __init__(self, x, y):
        self.x = x
        self.y = y



