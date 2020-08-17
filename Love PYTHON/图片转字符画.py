'''
图片转字符画的关键思想是将图片的灰度值与自己设定的字符集之间建立映射关系
1.先将彩色图片转换为黑白图片，然后直接将每个像素点的灰度值与字符集建立映射
2.获取图片的RGB值，利用公式：
Gray = R*0.299 + G*0.587 + B*0.114
计算可得每个像素点的灰度值，之后再建立映射即可。
'''
from PIL import Image

czx = Image.open("C:\\Users\\双宁\\Desktop\\czx.jpg")
print(czx.mode)
czx_1 = czx.convert("1")
print(czx_1.mode)
Image.show(czx_1)