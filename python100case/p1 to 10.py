'''
001题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
程序分析：遍历所有可能 掉不满足条件的排列
'''
count = 0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if (i != j) and (i != k) and (j != k):
                print(i,k,j)
                count += 1

'''
002题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，
奖金可提10%；利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；
60万到100万之间时，高于60万元的部分，可提成1.5%，
高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
程序分析：请利用数轴来分界，定位。

while True:
    profit = int(input('the profit is：'))
    print("利润是%d万元" % profit)
    bonus = 0
    if profit <= 10:
        bonus = profit*0.1
    elif profit <= 20 and profit > 10:
        bonus = profit*0.075
    elif profit >= 20 and profit < 40:
            bonus = 10 * 0.1 + (20 - 10) * 0.075 + 0.05 * (profit - 20)
    elif profit >= 40 and profit < 60:
            bonus = 10 * 0.1 + (20 - 10) * 0.075 + 0.05 * (40 - 20) + 0.03 * (profit - 40)
    elif profit >= 60 and profit < 100:
            bonus= 10 * 0.1 + (20 - 10) * 0.075 + 0.05 * (40 - 20) + 0.03 * (60 - 40) +\
                   (100 - 60) * 0.015 +(profit - 100) * 0.01
    else:
        bonus = 10 * 0.1 + (20 - 10) * 0.075 + 0.05 * (40 - 20) + 0.03 * (60 - 40) + (100 - 60) * 0.015 +\
                (profit - 100) * 0.01
    print("奖金是 %f 万元" % bonus)
'''

#上面的方法比较笨。下面为更简洁高效的方案
#从上面代码我们可以发现，上面利润的计算方法有一个通式
#就是（a-b）*c————如：10 * 0.1=（10-0）*0.1
profit = int(input('the profit is：'))
thresholds = [1000000, 600000, 400000, 200000, 100000, 0]
rates = [0.1, 0.075, 0.05, 0.03, 0.015, 0.01]
rates.reverse()
bonus = 0
for i in range(len(thresholds)):
    if profit > thresholds[i]:
        bonus += (profit - thresholds[i]) * rates[i]
        print("区间提成：", (profit - thresholds[i]) * rates[i])
        profit = thresholds[i]
print(bonus)


"""
003题目：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
程序分析：因为168对于指数爆炸来说实在太小了，所以可以直接省略数学分析，用最朴素的方法来获取上限:
"""
n = 0
while (n+1)**2 - n ** 2 <= 168:
    n += 1

    print(n+1)

for i in range((n+1)**2):
    if (i + 168)** 0.5 == int((i + 168)** 0.5):
        print(i-100)

'''
题目：输入某年某月某日，判断这一天是这一年的第几天？
程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，
特殊情况，闰年且输入月份大于2时需考虑多加一天
'''
