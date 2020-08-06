#注意1.in range(2,2)会生成nothing，直接跳过这个循环。
for i in range(2, 2):
    if i is None:
        print('none')
    print(type(i))
    print(i)
print(type(i))

#注意2.在for循环完整完成后才执行else；如果中途从break跳出，则连else一起跳出。
#特别需要注意的是如果for中有if语句，else的缩进一定要和for对齐，如果和if对齐，则变成if－else语句


