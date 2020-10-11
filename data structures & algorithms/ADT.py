#python面对对象编程：定义类
'''
每当需要实现抽象数据类型时，就可以穿件新类
'''
#1、Fraction类
class Fraction:

    def __init__(self,top,bottom):

        self.num = top #分子
        self.den = bottom #分母

    def show(self):
        print(self.num , '/', self.den)


myfraction = Fraction(3,5)
myfraction.show()