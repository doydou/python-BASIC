from function import gcd


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


    #将对象变成字符串的方法__str__
    def __str__(self):
        return str(self.num) + "/" + str(self.den)



    '''
    两个分数相加的话
    f1 = Fraction(1,4)
    f2 = Fraction(1,2)
    print(f1 + f2)#TypeError: unsupported operand type(s) for +: 'Fraction' and 'Fraction'
    '''
    #我们需要通过重写Fraction类来处理加法
    # def __add__(self , otherfraction):
    #
    #     newnum = self.num * otherfraction.den + \
    #                  self.den * otherfraction.num
    #
    #     newden = self.den * otherfraction.den
    #
    #     return Fraction(newnum , newden)

    #f1 = Fraction(1,4)
    #f2 = Fraction(1,2)
    #print(f1 + f2)



    #所以我们利用gcd函数可以改良__add__方法
    def __add__(self , otherfraction):

        newnum = self.num * otherfraction.den + \
                     self.den * otherfraction.num

        newden = self.den * otherfraction.den

        common = gcd (newnum , newden)#外部调用函数

        return Fraction(newnum//common , newden//common)



f1 = Fraction(1,4)
f2 = Fraction(1,2)
print(f1 + f2)