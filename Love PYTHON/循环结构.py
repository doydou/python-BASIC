'''for-in循环
如果明确的知道循环执行的次数或者是要对一个容器进行迭代
那么我们推荐使用for-in循环'''
"""
用for循环实现1~100求和
"""
sum = 0
for i in range(1,101):
    sum = sum + i
print(sum)

"""
用for循环实现1~100之间的偶数求和
"""
sum = 0
for i in range(2, 101, 2):
    sum += i
print(sum)

"""
While循环
猜数字游戏
计算机出一个1~100之间的随机数由人来猜
计算机根据人猜的数字分别给出提示大一点/小一点/猜对了
"""
import random
answer = random.randint(1,100)
times = 0
while True:
    times = times + 1
    num = int(input("请输入："))
    if num < answer:
        print("小了")
    elif num > answer:
        print("大了")
    else:
        print("恭喜你猜对了")
        break
print("你一共猜了%d次"%times)
if times > 7:
    print("你太笨了")
else:
    print("你太厉害了")

#练习：1输出乘法口诀表(九九表)
for i in range(1,10):
    for j in range(1,i+1):
        print("%d*%d=%d\t"%(i,j,i*j),end='')
    print()

#2.判断是否是闰年
year = int(input("请输入一个年份: "))
if (year % 4) == 0 and (year % 100) != 0 or (year % 400) == 0:
    print('{0} 是闰年' .format(year))
else:
    print('{0} 不是闰年' .format(year))

#3.计算100以内素数
primenumber = []
for i in range(2,101):
    for j in range(2,i):#当i=2时，值为nothing，会直接跳过这个循环
        if (i % j == 0):
            break
    else:
        primenumber.append(i)
print(primenumber)



