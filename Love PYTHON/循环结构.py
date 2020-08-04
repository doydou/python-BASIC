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


